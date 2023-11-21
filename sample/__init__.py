import tkinter as tk
from tkinter import filedialog
from PIL import ImageGrab

def open_paint_app():
    menu_frame.pack_forget()
    paint_app_frame.pack()

def go_back_to_menu():
    paint_app_frame.pack_forget()
    menu_frame.pack()

def on_click(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y

def on_drag(event):
    global prev_x, prev_y
    canvas.create_line(prev_x, prev_y, event.x, event.y, fill=color_picker.get(), width=brush_size.get())
    prev_x, prev_y = event.x, event.y

def change_brush_size(size):
    brush_size.set(size)

def save_canvas():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
    if file_path:
        x = root.winfo_rootx() + canvas.winfo_x()
        y = root.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)

root = tk.Tk()
root.title("Draw&Solve Labrinths")

# Main Menu
menu_frame = tk.Frame(root)

open_paint_button = tk.Button(menu_frame, text="Open Paint App", command=open_paint_app)
open_paint_button.pack()

menu_frame.pack()

# Paint app
paint_app_frame = tk.Frame(root)

brush_size = tk.Scale(paint_app_frame, from_=2, to=10, orient=tk.HORIZONTAL, label="Brush Size", command=change_brush_size)
brush_size.pack()

color_picker = tk.StringVar()
color_picker.set("black")

color_frame = tk.Frame(paint_app_frame)
colors = ["black", "red", "green"]
for color in colors:
    tk.Radiobutton(color_frame, bg=color, variable=color_picker, value=color).pack(side=tk.LEFT)
color_frame.pack()

canvas = tk.Canvas(paint_app_frame, width=600, height=400, bg="white")
canvas.pack()

canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)

save_button = tk.Button(paint_app_frame, text='Save', command=save_canvas)
save_button.pack()

go_back_button = tk.Button(paint_app_frame, text="Go Back", command=go_back_to_menu)
go_back_button.pack()

# Initially hide paint app
paint_app_frame.pack_forget()

root.mainloop()
