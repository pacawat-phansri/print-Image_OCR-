import sys
from pathlib import Path
import os

# Add current directory to Python path
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

from tkinterdnd2 import TkinterDnD
from gui.main_window import ImageOCRApp
from utils.tesseract_utils import initialize_tesseract

def main():
    # Initialize Tesseract
    tesseract_available = initialize_tesseract()
    
    # Create main window
    root = TkinterDnD.Tk()
    
    # Configure window scaling for high DPI displays
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
    
    # Set window icon (if available)
    try:
        root.iconbitmap("assets/icon.ico")
    except:
        pass
    
    # Create application instance
    app = ImageOCRApp(root, tesseract_available)
    
    # Start application
    root.mainloop()

if __name__ == "__main__":
    main() 