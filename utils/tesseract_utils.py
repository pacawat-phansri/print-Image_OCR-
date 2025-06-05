import os
import subprocess
import pytesseract

def find_tesseract():
    """Find Tesseract executable in various possible locations"""
    possible_paths = [
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
        r"C:\Users\TEEREDCOM\AppData\Local\Programs\Tesseract-OCR\tesseract.exe",
        r"C:\Users\TEEREDCOM\AppData\Local\Tesseract-OCR\tesseract.exe"
    ]
    
    # Check if tesseract is in PATH
    try:
        result = subprocess.run(['where', 'tesseract'], 
                              capture_output=True, 
                              text=True)
        if result.returncode == 0:
            path = result.stdout.strip().split('\n')[0]
            if os.path.exists(path):
                return path
    except:
        pass
    
    # Check common installation paths
    for path in possible_paths:
        if os.path.exists(path):
            return path
            
    return None

def get_available_languages():
    """Get list of available Tesseract languages"""
    try:
        tesseract_path = find_tesseract()
        if tesseract_path:
            tesseract_dir = os.path.dirname(tesseract_path)
            tessdata_dir = os.path.join(tesseract_dir, 'tessdata')
            if os.path.exists(tessdata_dir):
                files = os.listdir(tessdata_dir)
                # Get language codes from .traineddata files
                languages = [f.replace('.traineddata', '') 
                           for f in files if f.endswith('.traineddata')]
                return sorted(languages)
    except Exception as e:
        print(f"Error getting languages: {e}")
    return ['eng']  # Return English as default

def initialize_tesseract():
    """Initialize Tesseract with the correct path"""
    tesseract_path = find_tesseract()
    if tesseract_path:
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
        return True
    return False 