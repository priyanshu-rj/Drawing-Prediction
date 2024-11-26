import tkinter as tk
from PIL import Image, ImageDraw
import os


class DrawingApp:
    def __init__(self, root, save_path):
        self.root = root
        self.root.title("Draw and Save Image")

        self.canvas_width = 400
        self.canvas_height = 400

        
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack()

        
        self.image = Image.new('RGB', (self.canvas_width, self.canvas_height), color='white')
        self.draw = ImageDraw.Draw(self.image)

        
        self.pen_size = 5  

        
        self.canvas.bind("<B1-Motion>", self.paint)

        
        self.save_path = save_path

        
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        
        self.save_button = tk.Button(self.root, text="Save Drawing", command=self.save_image)
        self.save_button.pack()

    def paint(self, event):
       
        x1, y1 = (event.x - self.pen_size), (event.y - self.pen_size)
        x2, y2 = (event.x + self.pen_size), (event.y + self.pen_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill='black', width=self.pen_size)
        
        
        self.draw.line([x1, y1, x2, y2], fill="black", width=self.pen_size)

    def save_image(self):
        
        existing_files = os.listdir(self.save_path)
        existing_numbers = [int(f.split('.')[0]) for f in existing_files if f.endswith('.png')]
        next_number = max(existing_numbers, default=0) + 1
        filename = f"{next_number}.png"

        
        self.image.save(os.path.join(self.save_path, filename))
        print(f"Image saved as {filename}!")


root = tk.Tk()


save_folder = "C:/Users/priya/OneDrive/Desktop/Drawn"  
app = DrawingApp(root, save_folder)
root.mainloop()
