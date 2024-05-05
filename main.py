from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from PIL import Image, ImageTk
import os

class Resizer:
    def __init__(self):
        self.root = Tk()
        self.root.title("Image Resizer")

        self.label = Label(self.root)
        self.label.pack()

        self.width_entry = Entry(self.root)
        self.width_entry.pack()

        self.height_entry = Entry(self.root)
        self.height_entry.pack()

        self.open_button = Button(self.root, text="Open Image", command=self.open_image)
        self.open_button.pack()

        self.resize_button = Button(self.root, text="Resize Image", command=self.resize_image)
        self.resize_button.pack()

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff")])
        if not file_path:
            return
        image = Image.open(file_path)
        image.thumbnail((300, 300))  # Resize the image to fit in a 300x300 box
        photo = ImageTk.PhotoImage(image)
        self.label.config(image=photo)
        self.label.image = photo  # Keep a reference to the image to prevent it from being garbage collected

    def resize_image(self):
        width = int(self.width_entry.get())
        height = int(self.height_entry.get())
        if width == 0 or height == 0:
            messagebox.showerror("Error", "Width and height must be greater than 0.")
            return
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff")])
            if not file_path:
                return
            image = Image.open(file_path)
            image = image.resize((width, height), Image.ANTIALIAS)
            image.save("resized_image.jpg")
            messagebox.showinfo("Success", "Image resized successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        self.root.mainloop()

# Create an instance of the Resizer class and run it
resizer = Resizer()
resizer.run()
