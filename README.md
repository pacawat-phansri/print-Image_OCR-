# Modern OCR Application | แอปพลิเคชัน OCR สมัยใหม่

A modern desktop application for Optical Character Recognition (OCR) with support for both English and Thai languages.

แอปพลิเคชันเดสก์ท็อปสมัยใหม่สำหรับการรู้จำตัวอักษร (OCR) รองรับทั้งภาษาอังกฤษและภาษาไทย

![Application Screenshot](docs/screenshot.png)

- 🖼️ Modern and intuitive user interface | อินเตอร์เฟซที่ทันสมัยและใช้งานง่าย
- 🌏 Support for English and Thai languages | รองรับภาษาอังกฤษและภาษาไทย
- 🎯 Drag and drop image support | รองรับการลากและวางรูปภาพ
- 🔍 Image preprocessing for better accuracy | การประมวลผลรูปภาพเพื่อความแม่นยำที่ดีขึ้น
- 🖱️ Zoom and pan image controls | ควบคุมการซูมและเลื่อนรูปภาพ
- 📝 Clean text output with automatic formatting | ข้อความที่ได้มีการจัดรูปแบบอัตโนมัติ

## Requirements | ความต้องการของระบบ

- Python 3.7 or higher | Python 3.7 หรือสูงกว่า
- Tesseract OCR 5.0.0 or higher | Tesseract OCR 5.0.0 หรือสูงกว่า
- Windows 10/11 (Tested on) | Windows 10/11 (ทดสอบแล้ว)

## Installation | การติดตั้ง

1. Install Tesseract OCR | ติดตั้ง Tesseract OCR:
   ```bash
   # Download and install from:
   https://github.com/UB-Mannheim/tesseract/wiki
   
   # Important during installation:
   # - Install to default location: C:\Program Files\Tesseract-OCR
   # - Select "Thai" language during installation
   # - Check "Add to PATH" during installation
   ```

2. Clone the repository | โคลนโปรเจค:
   ```bash
   git clone https://github.com/yourusername/ocr_app.git
   cd ocr_app
   ```

3. Install Python dependencies | ติดตั้ง dependencies ของ Python:
   ```bash
   pip install -r requirements.txt
   ```

## Usage | วิธีใช้งาน

1. Start the application | เริ่มใช้งานแอปพลิเคชัน:
   ```bash
   python main.py
   ```

2. Use the application | ขั้นตอนการใช้งาน:
   - Drag and drop an image or click to select | ลากและวางรูปภาพหรือคลิกเพื่อเลือกรูปภาพ
   - Select language (English, Thai, or both) | เลือกภาษา (อังกฤษ, ไทย หรือทั้งสองภาษา)
   - Enable/disable preprocessing as needed | เปิด/ปิดการประมวลผลรูปภาพตามต้องการ
   - Click "Extract Text (OCR)" | คลิก "Extract Text (OCR)"
   - View and copy the extracted text | ดูและคัดลอกข้อความที่สกัดได้

## Features in Detail | รายละเอียดคุณสมบัติ

### Image Preprocessing | การประมวลผลรูปภาพ
- Automatic contrast enhancement | ปรับปรุงความคมชัดอัตโนมัติ
- Image sharpening | เพิ่มความคมชัดของรูปภาพ
- Grayscale conversion | แปลงเป็นภาพขาวดำ

### Text Processing | การประมวลผลข้อความ
- Automatic spacing correction for Thai text | แก้ไขการเว้นวรรคสำหรับข้อความภาษาไทยอัตโนมัติ
- Common OCR error correction | แก้ไขข้อผิดพลาด OCR ที่พบบ่อย
- Clean formatting | การจัดรูปแบบที่สะอาด

### User Interface | อินเตอร์เฟซผู้ใช้
- High DPI support | รองรับหน้าจอความละเอียดสูง
- Modern theme with clean design | ธีมสมัยใหม่ดีไซน์สะอาดตา
- Responsive layout | เลย์เอาต์ที่ปรับขนาดได้
- Image zoom and pan controls | ควบคุมการซูมและเลื่อนรูปภาพ

## Contributing | การมีส่วนร่วม

Contributions are welcome! Please feel free to submit a Pull Request.

ยินดีรับการมีส่วนร่วม! สามารถส่ง Pull Request ได้

## License | ลิขสิทธิ์

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

โปรเจคนี้ใช้ลิขสิทธิ์ MIT License - ดูรายละเอียดได้ที่ไฟล์ [LICENSE](LICENSE)

## Acknowledgments | ขอบคุณ

- Tesseract OCR team
- Python-tesseract developers
- TkinterDnD2 developers 
