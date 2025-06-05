import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
from PIL import Image, ImageTk
import os
from tkinterdnd2 import DND_FILES, TkinterDnD
import pytesseract
import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

from utils.tesseract_utils import get_available_languages
from processors.text_processor import process_ocr_result
from processors.image_processor import preprocess_image, resize_image_for_display
from .theme import apply_modern_theme

class ImageOCRApp:
    def __init__(self, root, tesseract_available=False):
        self.root = root
        self.root.title("Image OCR Application")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 700)  # Set minimum window size
        
        # Apply modern theme
        self.text_config = apply_modern_theme(self.root)
        
        # Show Tesseract status
        if not tesseract_available:
            self.show_tesseract_instructions()
        else:
            print("Tesseract is properly configured")
        
        self._init_ui()
        self._init_variables()
        self._bind_events()
    
    def _init_ui(self):
        """Initialize the user interface"""
        # Create main frame with padding
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Configure grid weights for responsive layout
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        
        # Create left and right frames
        self.left_frame = ttk.Frame(self.main_frame)
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        
        self.right_frame = ttk.Frame(self.main_frame)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        
        self._create_image_area()
        self._create_controls()
        self._create_text_area()
    
    def _create_image_area(self):
        """Create the image display area"""
        # Create drop zone with modern styling
        self.drop_frame = ttk.LabelFrame(self.left_frame, text="Image Preview")
        self.drop_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create canvas with modern background
        self.canvas = tk.Canvas(self.drop_frame, highlightthickness=0, bg="#ffffff")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Instructions label with modern font
        self.label = ttk.Label(self.drop_frame, 
                             text="Drag and drop an image here\nor click to select\n\nUse mouse wheel to zoom\nDrag with mouse to pan",
                             style="TLabel")
        self.label.place(relx=0.5, rely=0.5, anchor='center')
        
        # Status label
        self.status_label = ttk.Label(self.left_frame, text="")
        self.status_label.pack(pady=10)
    
    def _create_controls(self):
        """Create the control panel"""
        # OCR controls frame
        self.ocr_controls = ttk.LabelFrame(self.right_frame, text="OCR Controls")
        self.ocr_controls.pack(fill=tk.X, pady=(0, 15))
        
        # Add padding frame
        control_padding = ttk.Frame(self.ocr_controls)
        control_padding.pack(fill=tk.X, padx=10, pady=10)
        
        # Language selection with better layout
        self.lang_frame = ttk.Frame(control_padding)
        self.lang_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(self.lang_frame, text="Language:").pack(side=tk.LEFT, padx=(0, 10))
        
        # Language combobox with modern styling
        self.selected_lang = tk.StringVar(value='eng+tha')
        self.lang_combo = ttk.Combobox(self.lang_frame, 
                                     textvariable=self.selected_lang,
                                     values=['eng', 'tha', 'eng+tha'],
                                     width=15,
                                     state='readonly')
        self.lang_combo.pack(side=tk.LEFT)
        
        # Preprocessing option with modern styling
        self.preprocess_var = tk.BooleanVar(value=True)
        self.preprocess_check = ttk.Checkbutton(control_padding, 
                                              text="Preprocess Image",
                                              variable=self.preprocess_var)
        self.preprocess_check.pack(fill=tk.X, pady=(0, 10))
        
        # Buttons frame with better spacing
        self.button_frame = ttk.Frame(control_padding)
        self.button_frame.pack(fill=tk.X, pady=(5, 0))
        
        # OCR and Clear buttons with modern styling
        self.ocr_button = ttk.Button(self.button_frame, 
                                   text="Extract Text (OCR)",
                                   command=self.perform_ocr)
        self.ocr_button.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        
        self.clear_button = ttk.Button(self.button_frame,
                                     text="Clear Image",
                                     command=self.clear_image)
        self.clear_button.pack(side=tk.LEFT, padx=(5, 0), fill=tk.X, expand=True)
        
        # Disable buttons initially
        self.ocr_button.state(['disabled'])
        self.clear_button.state(['disabled'])
    
    def _create_text_area(self):
        """Create the text display area"""
        self.text_frame = ttk.LabelFrame(self.right_frame, text="Extracted Text")
        self.text_frame.pack(fill=tk.BOTH, expand=True)
        
        # Text area with modern styling
        self.text_area = scrolledtext.ScrolledText(
            self.text_frame,
            wrap=tk.WORD,
            **self.text_config
        )
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def _init_variables(self):
        """Initialize instance variables"""
        self.current_image = None
        self.current_image_path = None
        self.photo = None
        self.scale = 1.0
        self.image_on_canvas = None
        self.pan_start_x = 0
        self.pan_start_y = 0
    
    def _bind_events(self):
        """Bind all event handlers"""
        # Configure drag and drop
        self.drop_frame.drop_target_register(DND_FILES)
        self.drop_frame.dnd_bind('<<Drop>>', self.handle_drop)
        
        # Bind click and zoom events
        self.drop_frame.bind('<Button-1>', self.handle_click)
        self.label.bind('<Button-1>', self.handle_click)
        self.canvas.bind('<MouseWheel>', self.handle_zoom)
        self.canvas.bind('<Button-4>', self.handle_zoom)
        self.canvas.bind('<Button-5>', self.handle_zoom)
        
        # Bind pan events
        self.canvas.bind('<ButtonPress-1>', self.start_pan)
        self.canvas.bind('<B1-Motion>', self.pan)
    
    def show_tesseract_instructions(self):
        """Show instructions for installing Tesseract"""
        msg = """Tesseract OCR is not installed or not found!

Please follow these steps to install Tesseract:

1. Download Tesseract installer from:
   https://github.com/UB-Mannheim/tesseract/wiki
   
2. Run the installer:
   - Install to the default location: C:\\Program Files\\Tesseract-OCR
   - IMPORTANT: Select "Thai" language during installation
   - Check "Add to PATH" during installation
   
3. After installation:
   - Close all running Python programs
   - Open a new Command Prompt
   - Type 'tesseract --version' to verify installation
   
4. Restart this application"""
        
        messagebox.showwarning("Tesseract Not Found", msg)
    
    def handle_drop(self, event):
        """Handle drag and drop events"""
        file_path = event.data
        file_path = file_path.strip('{}')  # Remove curly braces (Windows)
        self.load_image(file_path)
    
    def handle_click(self, event):
        """Handle click events for image selection"""
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.tiff")]
        )
        if file_path:
            self.load_image(file_path)
    
    def handle_zoom(self, event):
        """Handle mouse wheel zoom events"""
        if not self.current_image:
            return
        
        # Calculate zoom factor
        if event.delta > 0 or event.num == 4:
            factor = 1.1  # Zoom in
        elif event.delta < 0 or event.num == 5:
            factor = 0.9  # Zoom out
        else:
            return
        
        # Update scale
        self.scale *= factor
        self.scale = min(max(0.1, self.scale), 5.0)
        
        # Update display
        self.display_image()
    
    def start_pan(self, event):
        """Record the position where panning starts"""
        self.canvas.scan_mark(event.x, event.y)
        self.pan_start_x = event.x
        self.pan_start_y = event.y
    
    def pan(self, event):
        """Pan (scroll) the image"""
        if self.image_on_canvas:
            self.canvas.scan_dragto(event.x, event.y, gain=1)
    
    def display_image(self):
        """Display the image at current scale"""
        if not self.current_image:
            return
        
        # Calculate new size
        new_width = int(self.current_image.width * self.scale)
        new_height = int(self.current_image.height * self.scale)
        
        # Resize image
        resized_image = self.current_image.resize((new_width, new_height),
                                                Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(resized_image)
        
        # Remove instruction label
        self.label.place_forget()
        
        # Update or create image on canvas
        if self.image_on_canvas:
            self.canvas.delete(self.image_on_canvas)
        
        # Center image
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        x = max(0, (canvas_width - new_width) // 2)
        y = max(0, (canvas_height - new_height) // 2)
        
        self.image_on_canvas = self.canvas.create_image(x, y,
                                                      anchor='nw',
                                                      image=self.photo)
        
        # Update scrollregion
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def load_image(self, file_path):
        """Load and display an image"""
        try:
            image = Image.open(file_path)
            
            # Store original image
            self.current_image = image
            self.current_image_path = file_path
            
            # Reset scale
            self.scale = 1.0
            
            # Display image
            self.display_image()
            
            # Update status and enable buttons
            self.status_label.configure(text=f"Image loaded: {os.path.basename(file_path)}")
            self.ocr_button.state(['!disabled'])
            self.clear_button.state(['!disabled'])
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")
            self.status_label.configure(text="Error loading image")
    
    def clear_image(self):
        """Clear the current image and reset the interface"""
        if self.current_image:
            # Clear image variables
            self.current_image = None
            self.current_image_path = None
            self.photo = None
            self.scale = 1.0
            
            # Clear canvas
            if self.image_on_canvas:
                self.canvas.delete(self.image_on_canvas)
                self.image_on_canvas = None
            
            # Reset text area
            self.text_area.delete(1.0, tk.END)
            
            # Show instruction label
            self.label.place(relx=0.5, rely=0.5, anchor='center')
            
            # Disable buttons
            self.ocr_button.state(['disabled'])
            self.clear_button.state(['disabled'])
            
            # Update status
            self.status_label.configure(text="Image cleared")
    
    def perform_ocr(self):
        """Perform OCR on the current image"""
        if not self.current_image:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            # Get a copy of the image
            image = self.current_image.copy()
            
            # Preprocess if enabled
            if self.preprocess_var.get():
                image = preprocess_image(image)
            
            # Perform OCR
            self.status_label.configure(text="Performing OCR...")
            self.root.update()
            
            try:
                # Get selected language
                lang = self.selected_lang.get()
                
                # Perform OCR
                text = pytesseract.image_to_string(image, lang=lang)
                
                # Process the result
                text = process_ocr_result(text, lang)
                
                if not text.strip():
                    messagebox.showwarning("OCR Result",
                                         "No text was detected in the image. "
                                         "Try enabling preprocessing or adjusting the image.")
                else:
                    # Update text area
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, text)
                    self.status_label.configure(text="OCR completed successfully")
                    
            except Exception as e:
                print(f"OCR Error: {str(e)}")
                self.show_tesseract_instructions()
            
        except Exception as e:
            messagebox.showerror("OCR Error", f"Error performing OCR: {str(e)}")
            self.status_label.configure(text="OCR failed") 