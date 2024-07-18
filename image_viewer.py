import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title('Image Viewer')

image1 = ImageTk.PhotoImage(Image.open('./cats/1.jpg'))
image2 = ImageTk.PhotoImage(Image.open('./cats/2.jpeg'))
image3 = ImageTk.PhotoImage(Image.open('./cats/3.jpg'))
image4 = ImageTk.PhotoImage(Image.open('./cats/4.jpg'))
image5 = ImageTk.PhotoImage(Image.open('./cats/5.jpeg'))

cat_images = [image1, image2, image3, image4, image5]

def update_image(num):
    global cat_label, next_btn, back_btn

    cat_label.grid_forget()
    cat_label = tk.Label(image=cat_images[num - 1])
    cat_label.grid(row=0, column=0, columnspan=3)

    back_btn = tk.Button(root, text='Back', command=lambda: backbtn_handler(num - 1))
    next_btn = tk.Button(root, text='Next', command=lambda: nextbtn_handler(num + 1))

    if num == 1:
        back_btn.config(state='disabled')
    else:
        back_btn.config(state='normal')
    
    if num == len(cat_images):
        next_btn.config(state='disabled')
    else:
        next_btn.config(state='normal')

    back_btn.grid(row=1, column=0)
    next_btn.grid(row=1, column=2)

def nextbtn_handler(num):
    update_image(num)

def backbtn_handler(num):
    update_image(num)

cat_label = tk.Label(root, image=image1)
cat_label.grid(row=0, column=0, columnspan=3)

back_btn = tk.Button(root, text='Back', command=lambda: backbtn_handler(1), state='disabled')
back_btn.grid(row=1, column=0)

quit_btn = tk.Button(root, text='Quit', command=root.quit)
quit_btn.grid(row=1, column=1)

next_btn = tk.Button(root, text='Next', command=lambda: nextbtn_handler(2))
next_btn.grid(row=1, column=2)

root.mainloop()
