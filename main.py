from playsound import playsound
from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeats = 0
program_timer = None

# ---------------------------- SOUND ALERT ------------------------------- # 


def play_pause():
    playsound('sound/alert.mp3')


def play_work():
    playsound('sound/work.mp3')


# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global program_timer, repeats
    repeats = 0
    window.after_cancel(program_timer)
    canvas.itemconfig(timer, text='00:00')
    label_check['text'] = ''
    label_logo['text'] = 'Таймер'


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global repeats
    repeats += 1
    if repeats % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        play_pause()
        label_logo['text'] = 'Перерва'
        label_logo['fg'] = RED
        label_check['text'] = ''
    elif repeats % 2 == 0:
        label_check['text'] += '✔️'
        count_down(SHORT_BREAK_MIN * 60)
        play_pause()
        label_logo['text'] = 'Перерва'
        label_logo['fg'] = PINK
    else:
        count_down(WORK_MIN * 60)
        play_work()
        label_logo['text'] = 'Робота'
        label_logo['fg'] = GREEN


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    min = int(count // 60)
    sec = int(count % 60)
    if len(str(sec)) < 2:
        sec = '0' + str(sec)
    if len(str(min)) < 2:
        min = '0' + str(min)
    canvas.itemconfig(timer, text=f'{min}:{sec}')
    if count > 0:
        global program_timer
        program_timer = window.after(10, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50, bg=YELLOW)
window.resizable(width=False, height=False)
window.title('Pomodoro')

canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='img/tomato.png')
image = canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 28, 'bold'), fill='white')
canvas.grid(row=1, column=1)

label_logo = Label(window, font=(FONT_NAME, 28, 'bold'), text='Таймер', bg=YELLOW, fg=GREEN)
label_logo.grid(row=0, column=1)

label_check = Label(window, font=(FONT_NAME, 16), bg=YELLOW, fg=GREEN)
label_check.grid(row=5, column=1)

button_start = Button(window, font=(FONT_NAME, 12), text='Старт', width=8, fg=RED, command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(window, font=(FONT_NAME, 12), text='Скидання', width=8, fg=RED, command=reset)
button_reset.grid(row=2, column=2)

window.mainloop()