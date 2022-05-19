from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn_card = {}

window = Tk()

try:
    word_data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = word_data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    card.itemconfig(title, text="French", fill = "black")
    card.itemconfig(word, text=current_card["French"], fill= "black")
    card.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    card.itemconfig(card_image, image=card_back)
    card.itemconfig(title, text = "English", fill="white")
    card.itemconfig(word, text=current_card["English"], fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()



window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_image = card.create_image(400,263, image=card_front)
card_back = PhotoImage(file="./images/card_back.png")
title = card.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = card.create_text(400,263, text="word", font=("Ariel", 60, "bold"), tags='labels')
card.grid(column=0, row=0, columnspan=2)


my_image1 = PhotoImage(file="./images/wrong.png")
x_button = Button(image=my_image1, highlightthickness=0, command=next_card)
x_button.grid(column=0, row=1)

my_image2 = PhotoImage(file="./images/right.png")
o_button = Button(image=my_image2, highlightthickness=0, command=is_known)
o_button.grid(column=1, row=1)


next_card()


window.mainloop()
