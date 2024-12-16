# MarkitDown_all

This repository uses the markitdown library to naively convert all convertible files within a folder into markdown files.

## How to use

Although the only dependency is markitdown, if you use uv, you can easily install it with the uv sync command.

1. Put every files into `input` folder.
2. Run `uv run src/markitdown_all.py`.
3. You can find the messy markdown files in `output` folder.

# MarkItDown

The [MarkItDown](https://github.com/microsoft/markitdown) library is a utility tool for converting various files to Markdown (e.g., for indexing, text analysis, etc.)

It presently supports:

- PDF (.pdf)
- PowerPoint (.pptx)
- Word (.docx)
- Excel (.xlsx)
- Images (EXIF metadata, and OCR)
- Audio (EXIF metadata, and speech transcription)
- HTML (special handling of Wikipedia, etc.)
- Various other text-based formats (csv, json, xml, etc.)
