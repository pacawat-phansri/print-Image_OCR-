import re

def clean_thai_text(text):
    """
    Clean up Thai OCR text by:
    1. Removing circular marks (◌)
    2. Removing extra spaces
    3. Fixing common Thai OCR errors
    """
    # Remove circular marks and zero-width spaces
    text = re.sub(r'[◌\u200b]', '', text)
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)
    
    # Fix common Thai OCR errors
    text = text.replace('เ เ', 'เ')  # Fix duplicate Sara E
    text = text.replace('า า', 'า')  # Fix duplicate Sara Aa
    text = text.replace('ำ ำ', 'ำ')  # Fix duplicate Sara Am
    
    # Remove spaces between Thai characters
    text = re.sub(r'(?<=[\u0E00-\u0E7F])\s+(?=[\u0E00-\u0E7F])', '', text)
    
    return text.strip()

def process_ocr_result(text, lang='eng'):
    """Process OCR result based on language"""
    if 'tha' in lang:
        return clean_thai_text(text)
    return text.strip() 