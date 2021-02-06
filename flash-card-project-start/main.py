import tkinter
import pandas as pd
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
FRONT_LANGUAGE_FONT = ('Arial', 40, 'italic')
FRONT_WORD_FONT = ('Arial', 60, 'bold')
french_word = ''
english_word = ''
# ------------- Window ------------------------------------
window = tkinter.Tk()
window.title('Flashy')
window.minsize(width=900, height=626)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# ------------- Data retrieval functionality --------------
df = pd.read_csv('./data/french_words.csv')
data_dictionary = df.to_dict(orient='records')

# ------------- New word functionality --------------------

def show_new_french_word_and_flip_card():

    data_dictionary_item = random.choice(data_dictionary)
    global french_word
    global english_word
    canvas.config(bg=BACKGROUND_COLOR)
    french_word = data_dictionary_item['French']
    english_word = data_dictionary_item['English']
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(actual_word, text=french_word, fill='black')
    canvas.itemconfig(actual_language, text='French', fill='black')
    window.after(ms=3000, func=flip_card)

# ------------ Flip card functionality --------------------

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(actual_language, text='English', fill='white')
    canvas.itemconfig(actual_word, text=english_word, fill='white')

# ------------- Canvas ------------------------------------

canvas = tkinter.Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=1, column=1, columnspan=2)
card_front_image = tkinter.PhotoImage(file='./images/card_front.png')
card_back_image = tkinter.PhotoImage(file='./images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_front_image)
actual_language = canvas.create_text(400, 150, text='Ready?', font=FRONT_LANGUAGE_FONT)
actual_word = canvas.create_text(400, 263, text='Goodluck!', font=FRONT_WORD_FONT)

# ------------- Buttons -----------------------------------
right_button_image = tkinter.PhotoImage(file='./images/right.png')
right_button = tkinter.Button(image=right_button_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=show_new_french_word_and_flip_card)
right_button.grid(row=2, column=2)
wrong_button_image = tkinter.PhotoImage(file='./images/wrong.png')
wrong_button = tkinter.Button(image=wrong_button_image, highlightthickness=0, command=show_new_french_word_and_flip_card)
wrong_button.grid(row=2, column=1)
window.mainloop()