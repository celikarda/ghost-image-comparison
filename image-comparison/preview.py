"""Serve the actual Ghost card and injection together for local review."""

import argparse
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import quote

DIRECTORY = Path(__file__).resolve().parent


class Preview(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            self.send_error(404)
            return
        card = (DIRECTORY / "card.html").read_text(encoding="utf-8")
        # SVG fixtures keep the preview offline and make image alignment visible.
        scene = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800"><rect width="1200" height="800" fill="COLOR"/><circle cx="850" cy="220" r="100" fill="#ffe6a7"/><path d="M0 800V550L300 300L580 650L900 400L1200 700V800Z" fill="#263c48"/><path d="M0 800V650L350 520L700 780L1200 580V800Z" fill="#597f6a"/></svg>'
        before = "data:image/svg+xml," + quote(scene.replace("COLOR", "#758ea6"))
        after = "data:image/svg+xml," + quote(scene.replace("COLOR", "#e7a474"))
        card = card.replace("BEFORE_IMAGE_URL", before).replace("AFTER_IMAGE_URL", after)
        card = card.replace("Describe the before image", "Mountain scene with a cool sky")
        card = card.replace("Describe the after image", "The same mountain scene with a warm sky")
        injection = (DIRECTORY / "footer-injection.html").read_text(encoding="utf-8")
        document = f'''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Image comparison preview</title>
<style>body {{ max-width: 760px; margin: 48px auto; padding: 0 24px; font: 18px/1.6 system-ui; color: #222; }} h1 {{ line-height: 1.2; }} .small {{ max-width: 360px; }}</style>
<h1>Image comparison</h1><p>Drag the divider, or focus it and use the arrow keys. Both cards work independently.</p>
{card}<div class="small">{card}</div>{injection}</html>'''
        body = document.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8937, help="port to listen on (default: 8937)")
    port = parser.parse_args().port
    try:
        server = HTTPServer(("127.0.0.1", port), Preview)
    except OSError as error:
        sys.exit(f"Could not start the preview on port {port}: {error.strerror}. Try --port with another number.")
    print(f"Preview: http://127.0.0.1:{port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
