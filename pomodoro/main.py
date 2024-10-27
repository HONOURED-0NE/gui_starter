import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timerr = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timerr
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= '00:00')
    timer.config(text='Timer')
    
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec =WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps%8 ==0:
        count_down(long_break_sec)
        timer.config(text='Long break', fg=RED)
    elif reps%2 == 0:
        count_down(short_break_sec)
        timer.config(text='Short break', fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text='Work session', fg=RED)
        


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count>0:
        global timerr
        timerr = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark= ''
        work_sessions = math.floor(reps/2)
        for c in range(work_sessions):
            mark += '✔'
        check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)



canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = tk.PhotoImage(file="./pomodoro/tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)



timer = tk.Label(text='Timer', fg='green', bg=YELLOW, font=(FONT_NAME, 30))
timer.grid(column=1, row=0)

start_button = tk.Button(text='Start',highlightthickness=0, command=start_timer )
start_button.grid(column=0, row=2)
reset_button = tk.Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = tk.Label(text="", fg='green', bg=YELLOW)
check_mark.grid(column=1, row=3)


print(250%60)
window.mainloop()