import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Drawing App")

        # Default brush settings
        self.brush_size = 10
        self.brush_color = "black"

        # Create a canvas for drawing
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind mouse events to the canvas
        self.canvas.bind("<B1-Motion>", self.paint)

        # Create a toolbar for controls
        self.create_toolbar()

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bg="lightgray")
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Button to choose color
        color_button = tk.Button(toolbar, text="Choose Color", command=self.choose_color)
        color_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Brush size slider
        size_slider = tk.Scale(toolbar, from_=1, to=50, orient=tk.HORIZONTAL, label="Brush Size")
        size_slider.set(self.brush_size)
        size_slider.pack(side=tk.LEFT, padx=5, pady=5)
        size_slider.bind("<Motion>", lambda event: self.change_brush_size(size_slider.get()))

        # Clear canvas button
        clear_button = tk.Button(toolbar, text="Clear Canvas", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT, padx=5, pady=5)

    def choose_color(self):
        # Open a color chooser dialog
        color = colorchooser.askcolor()[1]
        if color:
            self.brush_color = color

    def change_brush_size(self, new_size):
        # Update the brush size
        self.brush_size = int(new_size)

    def clear_canvas(self):
        # Clear all drawings from the canvas
        self.canvas.delete("all")

    def paint(self, event):
        # Draw an oval (circle) at the mouse position
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
