# 🐱‍👤 Ninja Background Remover

![License](https://img.shields.io/badge/license-MIT-blue.svg)  
*A free, offline, drag-and-drop background remover tool built with Python and AI.*

> 🔥 Remove image backgrounds instantly — no internet, no cost, just click & go!

![Demo](https://i.imgur.com/ZKQrF1p.gif) <!-- Optional: Replace with your own demo GIF -->

---

🤖 How It Works
---

Uses rembg with the isnet-general-use AI model for high-accuracy matting.
Post-processes alpha channel with Gaussian blur for smooth edges.
Built with tkinter + tkinterdnd2 for drag-and-drop support.
Fully offline — no data leaves your computer.

---

## 🚀 Features

- ✅ **Drag & drop** images (anywhere on the window)
- ✅ **Offline mode** — no data sent online
- ✅ Removes background using **AI (isnet-general-use model)**
- ✅ Saves output as `filename_bgninja.png` (transparent PNG)
- ✅ Works on JPG, PNG, BMP, WebP
- ✅ Lightweight GUI with **Tkinter**
- ✅ Smooth edges with post-processing blur
- ✅ Built-in support link & feedback

---

## 🖱️ How to Use

### 📦 Using the `.exe` (No Installation Needed)

1. Download `Ninja_Bg_Rm.exe` from the [Releases](https://github.com/DILIP3524/bgremoveAI/releases) section.
2. Double-click to run (Windows only).
3. Drag an image into the window or click **"Browse Image"**.
4. Wait a few seconds — output saved as `yourimage_bgninja.png` in the same folder!
5. Done! ✅

> 💡 No Python, no dependencies — works on any Windows PC.


🧰 Create Your Own .exe
```bash
pyinstaller --onefile --windowed ^
    --add-data ".venv/lib/site-packages/rembg/bg/models;rembg/bg/models" ^
    --icon=icon.ico ^
    Ninja_Bg_Rm.py
````    
✅ Output: dist/Ninja_Bg_Rm.exe 

---



### ⚙️ Developer: Build from Source

If you want to run or modify the code:

```bash
# Clone the repo
git clone https://github.com/DILIP3524/bgremoveAI.git
cd Ninja-Bg-Remover

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/macOS

# Install dependencies
pip install pillow rembg tkinterdnd2 pyinstaller

# Run the app
python Ninja_Bg_Rm.py
```

---
🛑 Usage Rights & License
All rights reserved by DILIP KUMAR (dilipdev3524@gmail.com ) 

✅ You are free to use this tool for personal or commercial projects.

✅ You may modify the code for your own use.

✅ You can share the tool or source code, as long as credit is given.

Prohibited Actions:

❌ Selling this tool or any version of it.

❌ Selling the code on marketplaces (CodeCanyon, Gumroad, etc.).

❌ Claiming ownership of the original code.

❌ Distributing as a paid product (directly or bundled).

❌ Using in SaaS without permission if monetized.

This project is not open-source for commercial resale. Respect the work. 

💬 Contact Me
📧 Email: dilipdev3524@gmail.com
🐱‍💻 GitHub: @DILIP3524
☕ Buy Me a Coffee: coff.ee/dilip3524

I'd love to hear how you're using it! Feature requests? Bugs? Just say hi! 🙌 

---


📜 License
This project is protected under all rights reserved. Unauthorized commercial redistribution or resale is strictly prohibited.

You may use, modify, and share freely as long as:

Credit is given to DILIP KUMAR
You do not sell the tool or code
You do not claim full ownership
For commercial licensing inquiries, contact: dilipdev3524@gmail.com

Made with ❤️ by DILIP KUMAR | © 2025 
