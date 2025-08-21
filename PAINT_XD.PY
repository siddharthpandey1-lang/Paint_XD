import tkinter as tk
class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Painting Software")

        self.brush_size = 5
        self.brush_color = "black"
        self.tool = "pencil"

        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<B1-Motion>", self.paint)

        self.setup_ui()

    def setup_ui(self):
        toolbar = tk.Frame(self.root)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        pencil_btn = tk.Button(toolbar, text="Pencil", command=self.use_pencil)
        pencil_btn.pack(side=tk.LEFT)

        brush_btn = tk.Button(toolbar, text="Brush", command=self.use_brush)
        brush_btn.pack(side=tk.LEFT)

        color_btn = tk.Button(toolbar, text="Color", command=self.choose_color)
        color_btn.pack(side=tk.LEFT)

        clear_btn = tk.Button(toolbar, text="Clear", command=self.clear_canvas)
        clear_btn.pack(side=tk.LEFT)

    def use_pencil(self):
        self.tool = "pencil"
        self.brush_size = 2

    def use_brush(self):
        self.tool = "brush"
        self.brush_size = 10

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.brush_color = color

    def clear_canvas(self):
        self.canvas.delete("all")

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()