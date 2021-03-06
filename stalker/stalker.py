import os
import sys
import math
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class App(tk.Frame):
    def __init__(self, path, master=None, width=400, height=300, padx=0, pady=0):
        super().__init__(master)
        self._geom = '{0}x{1}+{2}+{3}'.format(width, height, padx, pady)
        self.pack()

        self.master = master
        self.master.title(path)
        master_pad_x_y = 0
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth()-master_pad_x_y,\
            master.winfo_screenheight()-master_pad_x_y))
        self.exit = False
        self.path_generator = os.walk(path)
        self.tk_img = None
        self.cur_path_has_img = None
        self.cur_img_list = []

        self.canvas = tk.Canvas(self, width=self.master.winfo_screenwidth(), height=self.master.winfo_screenheight())
        self.canvas.grid()
        self.canvas.create_image((0,0), anchor=tk.NW, tags="photo")
        master.bind('<Button-1>', self.handle_click)
        master.bind('<Double-Button-1>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

    def handle_click(self, event):
        if self.exit:
            print("no more photos!")
            quit()
        if len(self.cur_img_list) == 0:
            while True:
                try:
                    cur_path, dirs, files = next(self.path_generator)
                    if len(files) > 0:
                        img_files = [i for i in files if i.split('.')[-1].lower() == 'jpg']
                        if len(img_files) > 0:
                            print (img_files)
                            break
                except StopIteration:
                    self.exit = True
                    self.master.title("没有更多照片了")
                    return
            self.cur_path_has_img = cur_path
            self.cur_img_list = img_files
        img_name = self.cur_img_list.pop(0)
        img_path = os.path.join(self.cur_path_has_img, img_name)
        self.show_img(img_path)
        
    def show_img(self, img_path):
        print(img_path)
        self.pil_img = Image.open(img_path)
        width, height = self.pil_img.size
        show_width, show_height = self.master.winfo_width(), self.master.winfo_height()
        ratio_width = show_width / width
        ratio_height = show_height / height
        ratio = min(ratio_width, ratio_height)
        height = math.floor(height * ratio)
        width = math.floor(width * ratio)
        temp_img = self.pil_img.resize((width, height))
        self.tk_img = ImageTk.PhotoImage(image=temp_img)
        self.canvas.itemconfigure('photo', image=self.tk_img)
        self.master.title(img_path)

if __name__ == '__main__':
    path = sys.argv[1]
    root = tk.Tk()
    app = App(path, root)
    root.mainloop()

