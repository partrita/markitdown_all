from markitdown import MarkItDown

markitdown = MarkItDown()
result = markitdown.convert("./input/test.pdf")
print(result.text_content)
