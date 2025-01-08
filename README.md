# HighlightHarvester

HighlightHarvester is a streamlined web application that extracts highlighted text from PDF files. Upload multiple PDFs and receive a neatly formatted markdown document containing all your highlights, organized by file and page number.

![HighlightHarvester Demo](link-to-your-demo-image.gif)

## Features

- 📁 Multiple PDF upload support
- ✅ Automatic file validation
- 📝 Markdown-formatted output
- 📥 One-click markdown download
- 📊 Summary statistics
- 📱 Mobile-friendly interface
- ☁️ Cloud-ready (Streamlit Cloud compatible)

## Live Demo

Try HighlightHarvester now: [Live Demo](your-streamlit-cloud-url)

## Installation

To run HighlightHarvester locally:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/HighlightHarvester.git
cd HighlightHarvester
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run pdf_highlight_extractor.py
```

## Usage

1. Open the application in your web browser
2. Upload one or more PDF files using the file uploader
3. Wait for the extraction process to complete
4. View your highlights directly on the page
5. Download the formatted markdown file using the download button

## Project Structure

```
HighlightHarvester/
├── pdf_highlight_extractor.py   # Main application file
├── requirements.txt             # Project dependencies
├── README.md                    # This file
└── .gitignore                  # Git ignore file
```

## Dependencies

- Python 3.9+
- Streamlit
- PyMuPDF (fitz)

## Deployment

### Streamlit Cloud

1. Fork this repository
2. Sign up for [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app and connect it to your forked repository
4. Deploy using these settings:
   - Main file path: `pdf_highlight_extractor.py`
   - Python version: 3.9+

### Local Server

For local deployment, follow the installation instructions above.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Common Issues

- **PDF Upload Fails**: Ensure your PDF is not password protected
- **No Highlights Found**: Verify that your PDF contains actual highlight annotations
- **Processing Error**: Check that your PDF is not corrupted

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- PDF processing powered by [PyMuPDF](https://pymupdf.readthedocs.io/)

## Contact

Your Name - [@BenYoungs](https://twitter.com/benyoungs)

Project Link: [https://gitlab.com/byoungs32/pdf-highlight-harvester/](https://gitlab.com/byoungs32/pdf-highlight-harvester/)

---