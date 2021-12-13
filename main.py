import tkinter as tk

"""
Constants
"""

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

"""
Timer reset
"""


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    reps = 0


"""
Timer mechanism
"""


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


"""
Countdown mechanism
"""


def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        mark = ""
        for _ in range(reps//2):
            mark += "✓"
        check_mark.config(text=mark)
        start_timer()


"""
UI Setup
"""

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tk.Label(text="Timer", font=(FONT_NAME, 36, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
canvas.grid(row=1, column=1)

start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = tk.Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)


window.mainloop()
