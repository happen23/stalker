import os
import sys
import tkinter as tk
from PIL import Image, ImageTk

class App(tk.Frame):
    def __init__(self, path, master=None, width=400, height=300, padx=0, pady=0):
        super().__init__(master)
        self._geom = '{0}x{1}+{2}+{3}'.format(width, height, padx, pady)
        self.pack()

        self.master = master
        master_pad_x_y = 3
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth()-master_pad_x_y,\
            master.winfo_screenheight()-master_pad_x_y))
        self.exit = False
        self.path_generator = os.walk(path)
        self.tk_img = None
        self.cur_path_has_img = None
        self.cur_img_list = []

        self.label = tk.Label(self, text=path, compound=tk.BOTTOM)
        self.label.grid()
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
            self.label.configure(text="没有更多照片了", image=None)
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
        while width > 1000 or height > 1000:
            width = width // 2
            height = height // 2
        temp_img = self.pil_img.resize((width, height))
        self.tk_img = ImageTk.PhotoImage(image=temp_img)
        self.label.configure(text=img_path, image=self.tk_img)

if __name__ == '__main__':
    path = sys.argv[1]
    root = tk.Tk()
    app = App(path, root)
    root.mainloop()

