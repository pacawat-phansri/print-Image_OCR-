from tkinter import ttk
import tkinter as tk

def apply_modern_theme(root):
    """Apply a modern theme to the application"""
    style = ttk.Style()
    
    # Configure colors
    style.configure(".",
        background="#f0f0f0",
        foreground="#333333",
        font=("Segoe UI", 10)
    )
    
    # Modern Button style
    style.configure("TButton",
        padding=(20, 10),
        background="#007bff",
        foreground="white",
        font=("Segoe UI", 10, "bold")
    )
    style.map("TButton",
        background=[("active", "#0056b3"), ("disabled", "#cccccc")],
        foreground=[("disabled", "#666666")]
    )
    
    # Modern Frame style
    style.configure("TFrame",
        background="#ffffff"
    )
    
    # Modern LabelFrame style
    style.configure("TLabelframe",
        background="#ffffff",
        padding=10
    )
    style.configure("TLabelframe.Label",
        font=("Segoe UI", 11, "bold"),
        foreground="#333333",
        background="#ffffff"
    )
    
    # Modern Label style
    style.configure("TLabel",
        background="#ffffff",
        font=("Segoe UI", 10)
    )
    
    # Modern Combobox style
    style.configure("TCombobox",
        padding=5,
        selectbackground="#007bff",
        selectforeground="white"
    )
    
    # Modern Checkbutton style
    style.configure("TCheckbutton",
        background="#ffffff",
        font=("Segoe UI", 10)
    )
    
    # Configure root window
    root.configure(bg="#f0f0f0")
    
    # Configure colors for text widgets
    text_config = {
        "bg": "#ffffff",
        "fg": "#333333",
        "font": ("Segoe UI", 11),
        "selectbackground": "#007bff",
        "selectforeground": "white",
        "insertbackground": "#333333",
        "relief": "flat",
        "padx": 10,
        "pady": 10
    }
    
    return text_config 