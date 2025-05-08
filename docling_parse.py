from docling.document_converter import DocumentConverter

#Local file to convert
source_file = "Users/giuliasolinas/Downloads/Colonil.pdf"

#Convert to markdown
converter = DocumentConverter()

# Convert the document to markdown
result = converter.convert(source_file, "markdown")
print(result.document.export_to_markdown())
