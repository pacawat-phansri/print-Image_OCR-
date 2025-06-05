from tkinter import ttk
import tkinter as tk

def apply_modern_theme(root):
    """Apply a modern theme to the application with soft blue tones and rounded corners"""
    style = ttk.Style()
    
    # Modern color palette with blue tones
    colors = {
        'primary': '#2196F3',  # Material Blue
        'primary_light': '#64B5F6',
        'primary_dark': '#1976D2',
        'background': '#EBF5FB',  # Very light blue
        'secondary_bg': '#E3F2FD',  # Lighter blue
        'card_bg': '#FFFFFF',
        'text': '#1A237E',  # Dark blue text
        'text_secondary': '#3949AB'  # Secondary blue text
    }
    
    # Configure colors
    style.configure(".",
        background=colors['background'],
        foreground=colors['text'],
        font=("Segoe UI", 10),
        borderwidth=0
    )
    
    # Super rounded button style
    style.configure("Rounded.TButton",
        padding=(20, 10),
        background=colors['primary'],
        foreground="white",
        font=("Segoe UI", 10, "bold"),
        borderwidth=0,
        relief="flat",
        borderradius=20  # Maximum rounding
    )
    style.map("Rounded.TButton",
        background=[("active", colors['primary_dark']), ("disabled", colors['primary_light'])],
        foreground=[("disabled", "white")]
    )
    
    # Frame styles with light blue background
    style.configure("Card.TFrame",
        background=colors['secondary_bg'],
        relief="flat",
        borderwidth=0
    )
    
    # LabelFrame style with rounded corners and blue tones
    style.configure("Card.TLabelframe",
        background=colors['card_bg'],
        relief="flat",
        borderwidth=0,
        padding=15
    )
    style.configure("Card.TLabelframe.Label",
        font=("Segoe UI", 11, "bold"),
        foreground=colors['primary_dark'],
        background=colors['card_bg'],
        padding=(15, 5)
    )
    
    # Label style with blue background
    style.configure("TLabel",
        background=colors['card_bg'],
        foreground=colors['text'],
        font=("Segoe UI", 10)
    )
    
    # Combobox style with rounded look
    style.configure("TCombobox",
        background=colors['card_bg'],
        fieldbackground=colors['card_bg'],
        foreground=colors['text'],
        arrowcolor=colors['primary'],
        padding=5,
        relief="flat",
        borderwidth=0
    )
    style.map("TCombobox",
        fieldbackground=[("readonly", colors['card_bg'])],
        selectbackground=[("readonly", colors['primary'])],
        selectforeground=[("readonly", "white")]
    )
    
    # Checkbutton style with blue accents
    style.configure("TCheckbutton",
        background=colors['card_bg'],
        foreground=colors['text'],
        font=("Segoe UI", 10)
    )
    style.map("TCheckbutton",
        background=[("active", colors['card_bg'])],
        foreground=[("disabled", colors['text_secondary'])]
    )
    
    # Configure root window with light blue background
    root.configure(bg=colors['background'])
    
    # Configure colors for text widgets with rounded appearance
    text_config = {
        "bg": colors['card_bg'],
        "fg": colors['text'],
        "font": ("Segoe UI", 11),
        "selectbackground": colors['primary'],
        "selectforeground": "white",
        "insertbackground": colors['text'],
        "relief": "flat",
        "padx": 15,
        "pady": 15,
        "borderwidth": 0,
        "highlightthickness": 0  # Remove border highlight
    }
    
    return text_config, colors 