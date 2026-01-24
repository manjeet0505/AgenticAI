from pathlib import Path

pdf_path = Path(__file__).parent / "story.pdf"

loader = PyPDFLoader(file_path=pdf)