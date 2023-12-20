BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
from pandas import *
import random


data= read_csv("data/french_words.csv")
dis= data.to_dict(orient="records")
print(dis)


french_word= None
english_word = None
ran_dis=None
def chose_randome_word ():
    global ran_dis
    ran_dis = random.choice(dis)
    print(ran_dis)
    global  french_word, english_word
    french_word = ran_dis["French"]
    english_word = ran_dis["English"]

def next_card_wrong():
    chose_randome_word()
    global flip_timer
    window.after_cancel(flip_timer)
    print(french_word)
    print(english_word)
    canvas.itemconfig(lang, text="French",fill="black")
    canvas.itemconfig(text, text= french_word,fill="black")
    canvas.itemconfig(canvas_bg, image=front_card)
    flip_timer=window.after(3000, func=flip_card)

def next_card_right():
    chose_randome_word()
    global flip_timer
    window.after_cancel(flip_timer)
    print(french_word)
    print(english_word)
    canvas.itemconfig(lang, text="French",fill="black")
    canvas.itemconfig(text, text= french_word,fill="black")
    canvas.itemconfig(canvas_bg, image=front_card)
    flip_timer=window.after(3000, func=flip_card)
    dis.remove(ran_dis)
def flip_card():
    global english_word , back_card
    canvas.itemconfig(lang,fill="white", text="English")
    canvas.itemconfig(text,fill="white", text=english_word)
    canvas.itemconfig(canvas_bg, image= back_card)


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000, func=flip_card)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
canvas_bg =canvas.create_image(400,263,image=front_card)

lang = canvas.create_text(400,150,text="French",fill="black", font=("Ariel",40,"italic"))
text = canvas.create_text(400,263,text="word",fill="black", font=("Ariel",60,"bold"))
canvas.grid(row = 0,column=0 , columnspan=2)

tic = PhotoImage(file="images/right.png")
cross = PhotoImage(file="images/wrong.png")

right_butten = Button(image=tic,highlightthickness=0,command=next_card_right )
right_butten.grid(row= 1 , column = 1)

wrong_butten = Button(image=cross,highlightthickness=0,command=next_card_wrong)
wrong_butten.grid(row= 1 , column=0)


next_card_wrong()


window.mainloop()