import tkinter
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FRONT_LANGUAGE_FONT = ('Arial', 40, 'italic')
FRONT_WORD_FONT = ('Arial', 60, 'bold')
FRENCH_WORD = ''
ENGLISH_WORD = ''
DATA_DICTIONARY_ITEM = None

# ------------- Window ------------------------------------
window = tkinter.Tk()
window.title('Flashy')
window.minsize(width=900, height=626)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ------------- Data retrieval functionality --------------
try:
    df = pd.read_csv('./words_to_learn.csv')
except FileNotFoundError:
    df = pd.read_csv('./data/french_words.csv')
    data_dictionary_list = df.to_dict(orient='records')
else:
    data_dictionary_list = df.to_dict(orient='records')

# ------------- Right button, update the data functionality --------------------


def remove_correct_words():
    try:
        del data_dictionary_list[data_dictionary_list.index(DATA_DICTIONARY_ITEM)]
        new_df = pd.DataFrame(data_dictionary_list)
        new_df.to_csv('./words_to_learn.csv', index=False)
        show_new_french_word_and_flip_card()
    except ValueError:
        show_new_french_word_and_flip_card()

# ------------- New word functionality --------------------


def show_new_french_word_and_flip_card():

    global DATA_DICTIONARY_ITEM
    global FRENCH_WORD
    global ENGLISH_WORD
    DATA_DICTIONARY_ITEM = random.choice(data_dictionary_list)
    canvas.config(bg=BACKGROUND_COLOR)
    FRENCH_WORD = DATA_DICTIONARY_ITEM['French']
    ENGLISH_WORD = DATA_DICTIONARY_ITEM['English']
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(actual_word, text=FRENCH_WORD, fill='black')
    canvas.itemconfig(actual_language, text='French', fill='black')
    window.after(ms=3000, func=flip_card)

# ------------ Flip card functionality --------------------


def flip_card():

    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(actual_language, text='English', fill='white')
    canvas.itemconfig(actual_word, text=ENGLISH_WORD, fill='white')

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
right_button = tkinter.Button(image=right_button_image, highlightthickness=0,
                              bg=BACKGROUND_COLOR, command=remove_correct_words)
right_button.grid(row=2, column=2)
wrong_button_image = tkinter.PhotoImage(file='./images/wrong.png')
wrong_button = tkinter.Button(image=wrong_button_image, highlightthickness=0, command=show_new_french_word_and_flip_card)
wrong_button.grid(row=2, column=1)
window.mainloop()