from setuptools import setup, find_packages

setup(
    name="ocr_app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pillow',
        'pytesseract',
        'tkinterdnd2'
    ]
)
