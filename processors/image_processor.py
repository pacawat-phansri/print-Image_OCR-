from PIL import Image, ImageEnhance

def preprocess_image(image):
    """
    Preprocess image for better OCR results
    
    Args:
        image: PIL Image object
    
    Returns:
        PIL Image object: Processed image
    """
    # Make a copy of the image
    img = image.copy()
    
    # Convert to grayscale
    img = img.convert('L')
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)
    
    # Enhance sharpness
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(2.0)
    
    return img

def resize_image_for_display(image, max_size=(800, 600)):
    """
    Resize image while maintaining aspect ratio
    
    Args:
        image: PIL Image object
        max_size: Tuple of (max_width, max_height)
    
    Returns:
        PIL Image object: Resized image
    """
    # Calculate aspect ratio
    ratio = min(max_size[0] / image.width, max_size[1] / image.height)
    
    # Calculate new size
    new_size = (int(image.width * ratio), int(image.height * ratio))
    
    # Resize image
    return image.resize(new_size, Image.Resampling.LANCZOS) 