# SmashPad v0.2
# by Birdwards and NyxTheShield

import sys
import zstandard as zstd
import os
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from tkinter import filedialog
from tkinter import messagebox
import base64

photo = "R0lGODlhkAFkAPcAAMnJyVRUVIiIiI+Pj4p+fY6BgVZWVq6lpdra2vr6+tHR0aCWlXR0dFZDQrKqqiEhISUNDc3NzZSKiTExMSEJCJGRkfz8/EYyMUk1NBIAAOLf3+7u7sLCwjgiIcbGxsG6uj4pKBEREYWFhZ+fn97e3mlpaeTk5Hl5eeDg4Ly1tU1NTcDAwIGBgWVlZeTh4T4+Pp2SkV1dXRoaGlFRUUhISPPz8+rq6tHMzHpra5qamqysrH19faWlpdXV1bi4uHp6em5ubjolJOLi4hwCAUItLE06OTQeHTk5OWZVVcTExKOZmd3Z2RwDAjchILS0tOjo6JeXlx0dHVE+PW1eXaGhoXFxcYqKil9NTGNSUcrExLKysjMdHAsLCxgAAJycnPHu7nNkY/Ly8piYmP7+/i0tLampqQICAujl5VhYWEFBQaSamioTEpCEhKOjo2NjY6qqqltbW7CwsO3r6oZ6eWpaWTIcGy8YGCwVFB8GBaednCgRECkpKTEaGe7s7Ozs7H5wcCYmJt3c276+vs/JyTwmJZ+UlDIbGjkkIyAIBycQD1hFRC4XFpeMizYgHz0oJzAZGEdHRywWFdnV1Z6Ukzw8PEQwL/X19fTy8h4JCfPx8TAaGGBOTSkUFI2AgIt/fkEsK2VUUy8YF4h7eyUREUArKiwXFw0AAJSIhyQMC11LSxQUFKqgoB4FBB8HBl1MSykSEVtJSCINDW9gXxwFBL29vdnZ2RoEBBwGBSILChwHBpOTk2BgYBgDA+fn59fX1/f397a2tpWVlfDw8CAHBisUE+bm5uHe3uPg4Ly8vLe3t/n5+ZSUlPj4+GFQTywUE2FhYZKSktjY2EMvLvb29tbW1ioSEbq6uvv7+/f29mhYV6KYl/Hx8SMLCi0WFfn4+FpIR+Pf3/r5+WdXVh8ICIl8fPj393VnZ19QUCcPDkY4N9XQ0Eo4N+bj42tcXFNAQIN3d5uQj8a/wH9xcHdoZ+fk5Oro6KWcm/39/ZuQkGNSUmZYV7iwsOXi4hsCAQAAAP///yH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS4zLWMwMTEgNjYuMTQ1NjYxLCAyMDEyLzAyLzA2LTE0OjU2OjI3ICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ4bXAuZGlkOjcwM0VGRTE0RjMzRkU5MTE4MTE0RjFCMjdFNzU1RkZEIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkVDRjlBM0YwM0ZGMzExRTk5OENBQjZEQTA0OUJDRkE4IiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkVDRjlBM0VGM0ZGMzExRTk5OENBQjZEQTA0OUJDRkE4IiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDUzYgKFdpbmRvd3MpIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6NzkzRUZFMTRGMzNGRTkxMTgxMTRGMUIyN0U3NTVGRkQiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6NzAzRUZFMTRGMzNGRTkxMTgxMTRGMUIyN0U3NTVGRkQiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz4B//79/Pv6+fj39vX08/Lx8O/u7ezr6uno5+bl5OPi4eDf3t3c29rZ2NfW1dTT0tHQz87NzMvKycjHxsXEw8LBwL++vby7urm4t7a1tLOysbCvrq2sq6qpqKempaSjoqGgn56dnJuamZiXlpWUk5KRkI+OjYyLiomIh4aFhIOCgYB/fn18e3p5eHd2dXRzcnFwb25tbGtqaWhnZmVk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"
icon = "R0lGODlhQABAAPf/AK2lpLmxsZmOjuzq6lFCQWRTUsvFxTMhISoUFEEuLUw+PbaurjYkJC4YGKqgnywXFo6CgYJ2dqCWlTAcHOTi4SgSEjQgIOro6DMfHqienjAbGqSbmjopKCYQDzwrK5+VlScPD723t9XQ0CYPDvLx8TMgIHpsbEk2NTIdHKednS0YFy0aGkw8PEY3Nj4tLHFhYB4FBDUiIiAICM3Hx05BQR4GBUg4NjkmJl9NTSwYGEI1NSMLCjIcG9zZ2TQiItbR0FJGRkIzM0o9PNHNyygQEBAAAB8GBTgmJjwtLRwCAbSsq0xAP1VGRkUwLyoTEzEeHiUNDDgoKEQ0NCoWFjYkIzosKxwEA0Q2NjcjIi0XFykTEz4rKzQeHTYgICcREUEzMzYiIR0FBDwnJjwqKUU0MzooJ2FPTj8wLzgkIywWFTQiISQODkk6OTIdHR8HBks5ODclJTolJRoEBD8wMBgCAUEwLyILCy8bGzwpKSUODSsVFTEbGiEJCBkDAyAIB9TPz9POzufl5dLNzeTh4efl5CIKCePg4Obk46OZmeLf3zAaGSQMC/v7+/v6+iYODeLe3uTh4PX09Pn4+OXi4uPf3/r5+aKYmOjm5unn5+fk5P39/T0sLObj4+bk5PTz8y0ZGaOamaKXlyEKCUAvLzgkJNTQz+Hd3ff29kAuLero50MyMZyRkfPy8o2FheXj4rewr9rV1aSamUk7OmhXVmlaV5+VksG7tzEdHKacm4Z5eIl/flZDQi4cHKegoKGWlhwGBRwHBrKpqenn5mpdXS8aGiQNDKOamnBkYnJmZs7LyyYYGOLf3ujl5VhFRPHw8PPy8ZaKif7+/rOsqCkSEaKYl9fS0uTg4OPg30M0M3VlZUQyMfv7+qKZmaOZmOnm5u7s7NHOzpuQj56Tk8jCwUc1NEU2Nby0s9vZ2SgVFe3r6x8IB0AyMUExMMG6ucK8usS9vNPPz9jV1dvX1qSZmZySkOTi4kk8O+Xj497b2C8ZGUw7OllLSh0EAxwDAhsCAf///yH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS4zLWMwMTEgNjYuMTQ1NjYxLCAyMDEyLzAyLzA2LTE0OjU2OjI3ICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ1M2IChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo4OUIwQTRFNDNGRjcxMUU5OENFMTk0MTYxOUFGQjVCQyIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo4OUIwQTRFNTNGRjcxMUU5OENFMTk0MTYxOUFGQjVCQyI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjg5QjBBNEUyM0ZGNzExRTk4Q0UxOTQxNjE5QUZCNUJDIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjg5QjBBNEUzM0ZGNzExRTk4Q0UxOTQxNjE5QUZCNUJDIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+Af/+/fz7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4uHg397d3Nva2djX1tXU09LR0M/OzczLysnIx8bFxMPCwcC/vr28u7q5uLe2tbSzsrGwr66trKuqqainpqWko6KhoJ+enZybmpmYl5aVlJOSkZCPjo2Mi4qJiIeGhYSDgoGAf359fHt6eXh3dnV0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUlFQT05NTEtKSUhHRkVEQ0JBQD8+PTw7Ojk4NzY1NDMyMTAvLi0sKyopKCcmJSQjIiEg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"


def comp(input_name, output_name, target_size):
    
    input = open(input_name, 'rb').read()
    
    # Compress uncomp_file to smaller than target_size
    print("Finding small enough compression level...")
    lvl = 1
    while True:
        cctx = zstd.ZstdCompressor(level=lvl)
        byte_data = cctx.compress(input)
        comp_size = len(byte_data)
        pad_size =  target_size - comp_size

        print("Level " + str(lvl) + ": file compressed to " + hex(comp_size) + " bytes")
        if pad_size < 0 or pad_size == 1 or pad_size == 2 or pad_size == 5:
            lvl+=1
            if lvl > 22:
                messagebox.showerror("Error", "File cannot be compressed to the required size!")
                return
        else:
            break
    print("Padding file at compression level " + str(lvl) +  "...")

    # Get the Frame_Header_Descriptor from the compressed file's first Frame_Header
    # This is the only step that differs between Python 2 and 3
    # For more info on how Frame_Header_Descriptor works, see:
    # https://tools.ietf.org/html/rfc8478#section-3.1.1.1
    if sys.version_info[0] >= 3:
        fhd = byte_data[4]
    else:
        fhd = ord(byte_data[4])

    # Read Frame_Content_Size_Flag to find the length of the Frame_Header
    start_index = 6
    if fhd >= 192:
        start_index = 13
    elif fhd >= 128:
        start_index = 9
    elif fhd >= 64:
        start_index = 7
        
    # Handle edge case for large files with Single_Segment_Flag unset
    if start_index > 6 and fhd % 64 < 32:
        start_index += 1

    # Dictionary_ID_Flag also affects Frame_Header length. I think this is always 0 by default, but I'm including it just in case
    if fhd % 4 == 1:
        start_index += 1
    elif fhd % 4 == 2:
        start_index += 2
    elif fhd % 4 == 3:
        start_index += 4

    # Create output file and write entire Frame_Header to file
    output = open(output_name, 'w+b')
    output.write(byte_data[0:start_index])

    # Insert empty data blocks of 3-byte or 4-byte lengths to make up the difference between the compressed size and our target size 
    if pad_size % 3 == 0:
        for x in range(pad_size):
            output.write(b"\x00")
    elif pad_size % 3 == 1:
        for x in range(pad_size-4):
            output.write(b"\x00")
        output.write(b"\x02\x00\x00\x00")
    elif pad_size % 3 == 2:
        for x in range(pad_size-8):
            output.write(b"\x00")
        output.write(b"\x02\x00\x00\x00\x02\x00\x00\x00")

    # Write the rest of the data from the compressed file
    output.write(byte_data[start_index:])
    output.close()

    messagebox.showinfo("Success!","File successfully padded to " + hex(target_size) + " bytes!")

def decomp(input_name, output_name):
    try:
        input = open(input_name, 'rb').read()
        dctx = zstd.ZstdDecompressor()
        original = dctx.decompress(input)
        
        output = open(output_name, 'w+b')
        output.write(original)
        output.close()
        
        messagebox.showinfo("Success!","File successfully decompressed to " + hex(len(original)) + " bytes!")
    except zstd.ZstdError:
        messagebox.showerror("Error", "The selected file is not a Zstd compressed file!")

#=============================================
# GUI Code
#=============================================

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


class popupWindow(object):
    def __init__(self,master):
        self.main_window = master
        top=self.top=Toplevel(master.raiz)
        top.resizable(width=False,height=False)
        top.geometry("230x100")
        top.title("Enter Size")
        top.wm_iconphoto(True, PhotoImage(data=icon))
        
        top.focus_force()
        top.grab_set()
        center(self.top)
        
        self.l=Label(top,text="Enter the desired size (In Hex)")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Save',command=self.cleanup,width=10)
        self.b.pack(pady=10)
        
    def cleanup(self):
        value=self.e.get()
        self.main_window.compress_file(value)
        self.top.destroy()


#=============================================
# Main Loop
#=============================================
        
class Application():
    
    def __init__(self):

        self.raiz = Tk()
        self.raiz.geometry('400x200')
        self.raiz.resizable(width=False,height=False)
        self.raiz.title('Smashpad GUI')
        center(self.raiz)

        image = PhotoImage(data=photo)
        self.label = Label(image=image)
        self.label.image = image # keep a reference!
        self.label.grid(row=0,columnspan = 3, rowspan = 1)

        imgicon = PhotoImage(data=icon)
        self.raiz.call('wm', 'iconphoto', self.raiz._w, imgicon)

        self.input_filename = Entry(self.raiz)
        self.input_filename.grid(row=1,columnspan = 2,sticky=N+S+W+E,padx=5)
        
        self.input = ttk.Button(self.raiz, text='Select File', command = self.openfile)
        self.input.grid(row=1,column=2,sticky=N+S+W+E,padx=5)

        self.compress = ttk.Button(self.raiz, text='Compress', command=self.compress_dialog)                   
        self.compress.grid(row=2,sticky=N+S+W+E,padx=20,pady=30)

        self.decompress = ttk.Button(self.raiz, text='Decompress', command=self.decompress_dialog)                   
        self.decompress.grid(row=2,column=2,sticky=N+S+W+E,padx=20,pady=30)

        

        self.raiz.mainloop()

    def openfile(self):
        file = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file", filetypes =(("All Files","*.*"),("All Files","*.*")))
        self.input_filename.delete(0, END)
        self.input_filename.insert(0, file)
        

    def outputfile(self):
        
        self.output_filename.delete(0, END)
        self.output_filename.insert(0, file)

    def compress_dialog(self):
        filepath = self.input_filename.get()
        filename = os.path.basename(filepath)
        splitted = filename.split("-")
        if not os.path.isfile(filepath):
            messagebox.showerror("Error", "You must select a file first!")
        else:
            if len(splitted) != 3:
                popupWindow(self)
            else:
                compressed_file = self.compress_file(splitted[2])

    def compress_file(self,target):
        filepath = self.input_filename.get()
        filename = os.path.basename(filepath)
        splitted = filename.split("-")
        output_filepath = filedialog.asksaveasfilename(initialdir = filepath, title = "Save as output file",initialfile = filename+".pad")
        target = int(target,16)
        comp(filepath, output_filepath, target)

    
    def decompress_dialog(self):
        filepath = self.input_filename.get()
        filename = os.path.basename(filepath)
        splitted = filename.split("-")
        if not os.path.isfile(filepath):
            messagebox.showerror("Error", "You must select a file first!")
        else:
            output_filepath = filedialog.asksaveasfilename(initialdir = filepath, title = "Save as output file",initialfile = filename+".orig")
            decomp(filepath, output_filepath)

 
def main():
    my_app = Application()
    return 0

if __name__ == '__main__':
    main()
