from tkinter import *
from rembg import remove
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("Remove Image Background")
root.geometry('500x700')

def open_thing():
    global input_path, my_img
    # open image path
    input_path = filedialog.askopenfilename(title="Open Image",filetypes=(("PNG Files", ".png"), ("All Files", "*.*")))
    
    if input_path:
        my_img = ImageTk.PhotoImage(Image.open(input_path))
        pic_label.config(image=my_img, bg="black")



def remove_thing():
    # get filepath to remove background
    output_path = filedialog.asksaveasfilename(title="Save as", filetypes=(("PNG Files", ".png"), ("All Files", "*.*")))

    # get file name
    input = Image.open(input_path)

    # remove bg
    output = remove(input)

    # save the file
    output.save(output_path, 'png')
# put new image on the screen
    global my_img
    my_img = ImageTk.PhotoImage(Image.open(output_path))

    # update Label
    pic_label.config(image=my_img)


# GUI
pic_label = Label(root, text='')
pic_label.pack(pady=20)

open_button = Button(root, text="Open Image", command=open_thing)
open_button.pack(pady=20)

remove_button = Button(root, text="Remove Background", command=remove_thing)
remove_button.pack(pady=10)




root.mainloop()