import tkinter
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
FRONT_LANGUAGE_FONT = ('Arial', 40, 'italic')
FRONT_WORD_FONT = ('Arial', 60, 'bold')

# ------------- Window ------------------------------------
window = tkinter.Tk()
window.title('Flashy')
window.minsize(width=900, height=626)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# ------------- Dataframe ---------------------------------
df = pd.read_csv('./data/french_words.csv')

# ------------- Canvas ------------------------------------

canvas = tkinter.Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=1, column=1, columnspan=2)
card_front_image = tkinter.PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(400, 150, text='Hello_Placeholder', font=FRONT_LANGUAGE_FONT)
canvas.create_text(400, 263, text='PALCEHOLDER', font=FRONT_WORD_FONT)

# ------------- Buttons -----------------------------------
right_button_image = tkinter.PhotoImage(file='./images/right.png')
right_button = tkinter.Button(image=right_button_image, highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(row=2, column=2)
wrong_button_image = tkinter.PhotoImage(file='./images/wrong.png')
wrong_button = tkinter.Button(image=wrong_button_image, highlightthickness=0)
wrong_button.grid(row=2, column=1
                  )
window.mainloop()