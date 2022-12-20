from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from PIL import Image, ImageDraw, ImageFont
from tkinter import *
from tkinter import filedialog

blue = "#4D77FF"
light_black = "#303841"

filepath1 = ""
def file_open():
    global filepath1
    filepath1 = filedialog.askopenfilename()
    
    entry_file_box.insert(0,filepath1)

def get_file():
    global watermarking_name
    global file_full_path
    watermarking_name = water_mark_box.get()
    file_full_path = entry_file_box.get()
    print(watermarking_name)
    print(file_full_path)

window = Tk()
window.title("Image Water marking")
window.config(padx=430, pady=250,bg=blue)

canvas = Canvas(width=650, height=400)
canvas.grid()



Enter_File = canvas.create_text(55,100,text="FileName :",fill=light_black,font=("Comic Sans MS",15,"italic"))
canvas.grid()

enter_water_mark = canvas.create_text(65,200,text="watermark : ",fill=light_black,font=("Comic Sans MS",15,"italic"))


entry_file_box = Entry(width=75)
entry_file_box.insert(0,filepath1)
canvas.create_window((128,92),height=25,window=entry_file_box,anchor=NW)

water_mark_box = Entry(width=75)
water_mark_box.insert(0,"Enter your Watermark")
canvas.create_window((130,192),height=25,window=water_mark_box,anchor=NW)

 
button_image = PhotoImage(file="file.png") ## here file enter your sumbit image size around 200 * 200 ##
button = Button(image=button_image,highlightthickness=0,borderwidth=0,command=file_open)
canvas.create_window(595,90,window=button,anchor=NW)

button_img = PhotoImage(file="ok.png") ## here file enter your ok image size around 200 * 200 ##
button_ok = Button(image=button_img,highlightthickness=0,borderwidth=1,command=get_file)
canvas.create_window(300,300,window=button_ok,anchor=NW)

window.mainloop()

image = Image.open(file_full_path)
image.show()
plt.imshow(image,aspect='auto')

color_choise = input("Select which color you like for water_mark_text : ")
water_mark_image = image.copy()
font_s = ImageFont.load_default()
draw = ImageDraw.Draw(water_mark_image)
font_size = int(input("Enter water_mark_text_size : "))
place_x = int(input("where you place water marking x : "))
plce_y = int(input("Enter where you place water marking y : "))
font_type_1 = ImageFont.truetype(fm.findfont(fm.FontProperties()),font_size)
draw.text((place_x,plce_y),text=watermarking_name,fill=color_choise,font=font_type_1)  
plt.subplot(1,1,1)
plt.title("black text")
plt.imshow(water_mark_image,aspect='auto')