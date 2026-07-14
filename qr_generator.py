import qrcode
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# -----------------------------
# Generate QR Code
# -----------------------------
def generate_qr():
    data = entry.get().strip()

    if not data:
        messagebox.showerror("Error", "Please enter some text or a URL.")
        return 

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")],
        title="Save QR Code"
    )

    if not file_path:
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(file_path)

    preview = img.resize((220, 220))
    preview = ImageTk.PhotoImage(preview)

    image_label.config(image=preview)
    image_label.image = preview

    status.config(text="QR Code saved successfully!", fg="green")


# -----------------------------
# GUI
# -----------------------------
window = Tk()
window.title("QR Code Generator")
window.geometry("450x500")
window.resizable(False, False)

title = Label(
    window,
    text="QR Code Generator",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

Label(
    window,
    text="Enter Text or URL",
    font=("Arial", 12)
).pack()

entry = Entry(window, width=45, font=("Arial", 12))
entry.pack(pady=10)

Button(
    window,
    text="Generate QR Code",
    command=generate_qr,
    bg="black",
    fg="white",
    font=("Arial", 11, "bold"),
    width=20
).pack(pady=10)

image_label = Label(window)
image_label.pack(pady=15)

status = Label(window, text="", font=("Arial", 11))
status.pack()

window.mainloop()