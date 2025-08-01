
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageFilter
import threading
from io import BytesIO
from rembg import remove
from rembg.session_factory import new_session
import webbrowser

from sympy.testing.pytest import tooslow

# Global variables
drag_area = None
drop_label = None


def open_url(url):
    webbrowser.open_new_tab(url)

# 👉 Use a better model for higher accuracy
session = new_session("isnet-general-use")

def refine_alpha(img: Image.Image) -> Image.Image:
    """Optional: Smooth edges slightly"""
    if img.mode != 'RGBA':
        return img
    rgb = img.convert('RGB')
    alpha = img.split()[-1]
    alpha = alpha.filter(ImageFilter.GaussianBlur(radius=0.7))  # Soften edges
    return Image.merge('RGBA', (*rgb.split(), alpha))

def process_image(image_path):
    try:
        with open(image_path, 'rb') as f:
            input_data = f.read()

        output_data = remove(input_data, session=session)

        img = Image.open(BytesIO(output_data))
        img = refine_alpha(img)  # Improve edge quality

        # Save as PNG with _bgninja suffix
        dir_name = os.path.dirname(image_path)
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        output_path = os.path.join(dir_name, f"{base_name}_bgninja.png")

        img.save(output_path, format="PNG")
        return output_path

    except Exception as e:
        raise RuntimeError(f"Processing failed: {str(e)}")

def drop(event):
    file_path = event.data.strip('{}')
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in ['.png', '.jpg', '.jpeg', '.bmp', '.webp']:
        messagebox.showerror("Invalid", "Not an image file.")
        return

    drop_label.config(text="Processing...", fg="blue")
    drag_area.config(bg="#e0f7fa")
    threading.Thread(target=handle_processing, args=(file_path,), daemon=True).start()

def handle_processing(image_path):
    try:
        output_path = process_image(image_path)
        def on_done():
            drop_label.config(text=f"Saved as:\n{os.path.basename(output_path)}", fg="green")
            drag_area.config(bg="#d4edda")
        drag_area.after(0, on_done)
    except Exception as e:
        def on_error():
            drop_label.config(text="Error!", fg="red")
            drag_area.config(bg="#f8d7da")
            messagebox.showerror("Error", str(e))
        drag_area.after(0, on_error)

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.webp")]
    )
    if file_path:
        drop_label.config(text="Processing...", fg="blue")
        drag_area.config(bg="#e0f7fa")
        threading.Thread(target=handle_processing, args=(file_path,), daemon=True).start()

def create_app():
    global drag_area, drop_label

    try:
        from tkinterdnd2 import TkinterDnD
        root = TkinterDnD.Tk()
    except ImportError:
        messagebox.showerror("Error", "tkinterdnd2 not installed!")
        return

    root.title("Ninja - Background Remover ")

    root.geometry("500x500")
    root.configure(bg="#f0f0f0")
    root.resizable(False, False)
    root.iconbitmap("icon.ico")
    Button1 = tk.Label(root, text="Buy Me a Coffee | Thanks", font=("Helvetica", 18, "bold"), fg="blue" , cursor='hand2')
    Button1.pack(pady=10)
    Button1.bind("<Button-1>", lambda e: open_url("coff.ee/dilip3524"))
    tk.Label(root, text="Ninja Bg Remover", font=("Helvetica", 18, "bold"), bg="#f0f0f0").pack(pady=10)
    tk.Label(root, text="Contact-dilipdev3524@gmail.com | Github-github.com/DILIP3524", bg="#f0f0f0").pack(pady=5)


    drag_area = tk.Frame(root, bg="#ddd", width=400, height=200, relief="ridge", bd=2)
    drag_area.pack(pady=20)
    drag_area.pack_propagate(False)

    drop_label = tk.Label(
        drag_area,
        text="Drop image here\nor click 'Browse'",
        font=("Arial", 14),
        bg="#ddd",
        fg="#555"
    )
    drop_label.pack(expand=True)

    # Enable drop
    drop_label.drop_target_register("DND_Files")
    drop_label.dnd_bind('<<Drop>>', drop)

    tk.Button(
        root, text="Browse Image", font=("Arial", 12),
        bg="#3498db", fg="white", command=browse_file,
        padx=10, pady=5
    ).pack(pady=10)

    tk.Label(root, text="Ninja Bg Remove © DILIP KUMAR - 2025 - Works offline", bg="#f0f0f0", fg="#777").pack(side="bottom", pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_app()