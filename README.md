# Ghost Image Comparison Card

A lightweight before/after image slider for Ghost posts and pages. Save it as a reusable snippet, then pick **Image comparison** from the editor's card menu.

No external scripts, packages, or theme changes are needed.

![Two image comparison cards at different widths](image-comparison/preview.jpg)

## Features

- Drag the divider with a mouse or touch.
- Use Tab, the arrow keys, Page Up/Page Down, Home, and End to compare with a keyboard.
- Custom before/after labels, image descriptions, and an optional caption.
- Responsive sizing and independent sliders on the same page, including cards loaded after the page opens.
- Both images remain available when the script is absent.

## Install once

1. In Ghost, open **Settings → Advanced → Code Injection**.
2. Append all of [`image-comparison/footer-injection.html`](image-comparison/footer-injection.html) to **Site Footer**, keeping any existing code, and save.
3. Open a draft post or page, add an **HTML** card, and paste [`image-comparison/card.html`](image-comparison/card.html).
4. Select the card, click the snippet icon in its toolbar, and save it as **Image comparison**.

Ghost's [snippet documentation](https://ghost.org/help/snippets/) explains how snippets appear in the card menu. This is a reusable HTML card; a new native card with image upload controls would require modifying Ghost's editor.

## Use in a post or page

1. Type `/Image comparison` on a new line, or choose it from the **+** card menu.
2. Replace `BEFORE_IMAGE_URL` and `AFTER_IMAGE_URL` with your image URLs, and write useful `alt` descriptions.
3. Set `width` and `height` on both images to your images' pixel size. They reserve space while the images load, so the page does not jump.
4. Change the `data-before-label` and `data-after-label` values if needed. Edit or remove the `<figcaption>`.
5. Open Ghost's page/post **Preview** to try the slider. Site Footer code runs on the website; the editor canvas may show both images separately.

To get a Ghost image URL, upload an image using a normal Image card, then copy its image address from the preview. Use images with the same framing and aspect ratio: the first image sets the slider's height, and the second fills that area.

The divider starts halfway across. Visitors can drag it with a mouse, tap or swipe sideways on touch screens, or use Tab and the arrow keys (1%), Page Up/Page Down (10%), Home, and End. Vertical swipes scroll the page as usual. Multiple comparison cards work independently.

Screen readers announce the slider using the caption. If a post has no caption, or several comparisons share one, add a short `data-label="..."` to the `<figure>`. Without the injected code, the HTML contains both images so they remain readable. Email clients do not run the interactive script.

## Local preview

Clone or download the repository, then run this command from its root:

```sh
python3 image-comparison/preview.py
```

Open <http://127.0.0.1:8937>. Python 3 is only needed for this local preview, which uses the same card and injection files as the installation. Its sample images are generated locally; no network access is needed. Press Ctrl+C to stop the preview server. If port 8937 is already in use, pick another one with `--port`, for example `python3 image-comparison/preview.py --port 9000`.

## Verification and limitations

The slider is used on a live Ghost site and has been checked in the local preview with mouse and keyboard input, at narrow and wide layouts, with multiple cards on one page. It is a reusable HTML snippet, so image URLs are edited in HTML rather than through native image upload controls. Interactive comparisons run on the website, not in email newsletters.

## Contributing

Bug reports and improvements are welcome. Include your browser, Ghost version, theme, and steps to reproduce when reporting a problem. For changes, check dragging, keyboard controls, narrow layouts, and multiple cards in the local preview.

## License

[MIT](LICENSE) © 2026 Arda Celik.
