# 📦 Install required packages (Run once in terminal or via pip)
# pip install qrcode opencv-python pyzbar pillow

# 📁 Import necessary modules
import qrcode
import cv2
from pyzbar.pyzbar import decode
from PIL import Image
import os

# 🧠 QR Code Generator Function
def generate_qr(data: str, filename: str = "qrcode.png"):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"[✅] QR Code generated and saved as '{filename}'.")

    # Display using PIL
    img.show()

# 🔍 QR Code Decoder Function
def decode_qr(image_path: str):
    if not os.path.exists(image_path):
        print(f"[❌] File '{image_path}' not found.")
        return

    decoded_objects = decode(img)

    if not decoded_objects:
        print("[❌] No QR code found.")
        return

    for obj in decoded_objects:
        print(f"[🔍] Decoded Data: {obj.data.decode('utf-8')}")

# --- 👇 User Interface ---
def main():
    print("==== QR Code Generator & Decoder ====")
    print("Select an option: [g] Generate QR | [d] Decode QR")

    choice = input("Enter choice (g/d): ").strip().lower()

    if choice == 'g':
        text = input("Enter text or URL to generate QR code: ")
        filename = input("Enter filename (e.g., mycode.png): ").strip() or "qrcode.png"
        generate_qr(text, filename)

    elif choice == 'd':
        filename = input("Enter path to QR code image (e.g., qrcode.png): ").strip()
        decode_qr(filename)

    else:
        print("[⚠️] Invalid choice. Use 'g' or 'd'.")

if __name__ == "__main__":
    main()
