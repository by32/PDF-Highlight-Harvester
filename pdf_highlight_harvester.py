import streamlit as st
import fitz  # PyMuPDF
import json
from datetime import datetime
import os
import tempfile
from pathlib import Path
import base64

class PDFHighlightExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)
        
    def extract_all_highlights(self):
        """Extract all highlights from the PDF with metadata."""
        all_highlights = []
        
        for page_num in range(len(self.doc)):
            page = self.doc[page_num]
            highlights = self._extract_page_highlights(page, page_num)
            all_highlights.extend(highlights)
            
        return all_highlights
    
    def _extract_page_highlights(self, page, page_num):
        """Extract highlights from a single page."""
        highlights = []
        annots = page.annots()
        
        if not annots:
            return highlights
            
        for annot in annots:
            if annot.type[0] == 8:  # Highlight annotation
                highlight_info = self._process_highlight(annot, page, page_num)
                highlights.append(highlight_info)
                
        return highlights
    
    def _process_highlight(self, annot, page, page_num):
        """Process a single highlight annotation."""
        rect = annot.rect
        highlight_text = page.get_text("text", clip=rect).strip()
        
        return {
            'page_number': page_num + 1,
            'text': highlight_text
        }
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.doc.close()

def validate_pdf(file):
    """Validate uploaded file is a PDF."""
    if file is None:
        return False
    return file.name.lower().endswith('.pdf')

def create_markdown(results):
    """Convert extraction results to markdown format."""
    markdown_text = ""
    for filename, highlights in results.items():
        markdown_text += f"# {filename}\n\n"
        if not highlights:
            markdown_text += "No highlights found in this document.\n\n"
            continue
            
        for highlight in highlights:
            markdown_text += f"- Page {highlight['page_number']}: {highlight['text']}\n"
        markdown_text += "\n"
    return markdown_text

def get_download_link(markdown_text, filename="highlights.md"):
    """Generate download link for markdown file."""
    b64 = base64.b64encode(markdown_text.encode()).decode()
    return f'<a href="data:file/markdown;base64,{b64}" download="{filename}">Download Markdown</a>'

def main():
    st.set_page_config(page_title="PDF Highlight Extractor", layout="wide")
    
    st.title("PDF Highlight Extractor")
    st.write("Upload PDFs to extract highlighted text")
    
    # File uploader
    uploaded_files = st.file_uploader(
        "Choose PDF files", 
        type=['pdf'], 
        accept_multiple_files=True
    )
    
    if uploaded_files:
        results = {}
        
        # Process each file
        with st.spinner('Extracting highlights...'):
            for uploaded_file in uploaded_files:
                if not validate_pdf(uploaded_file):
                    st.error(f"'{uploaded_file.name}' is not a valid PDF file.")
                    continue
                
                # Save uploaded file temporarily
                with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_path = tmp_file.name
                
                try:
                    with PDFHighlightExtractor(tmp_path) as extractor:
                        highlights = extractor.extract_all_highlights()
                        results[uploaded_file.name] = highlights
                except Exception as e:
                    st.error(f"Error processing {uploaded_file.name}: {str(e)}")
                    results[uploaded_file.name] = []
                
                # Clean up temporary file
                os.unlink(tmp_path)
        
        if results:
            # Create markdown
            markdown_text = create_markdown(results)
            
            # Display results
            st.subheader("Extracted Highlights")
            st.markdown(markdown_text)
            
            # Download button
            st.markdown(
                get_download_link(markdown_text),
                unsafe_allow_html=True
            )
            
            # Display summary statistics
            total_highlights = sum(len(highlights) for highlights in results.values())
            st.sidebar.subheader("Summary Statistics")
            st.sidebar.write(f"Total PDFs processed: {len(results)}")
            st.sidebar.write(f"Total highlights extracted: {total_highlights}")

if __name__ == "__main__":
    main()