import calendar
import datetime
import tkinter as tk


def update_calendar():
    now = datetime.datetime.now()
    yy = now.year
    mm = now.month
    cal_text = calendar.month(yy, mm)
    calendar_label.config(text=cal_text)

def previous_month():
    global mm, yy
    mm -= 1
    if mm == 0:
        mm = 12
        yy -= 1
    update_calendar()

def next_month():
    global mm, yy
    mm += 1
    if mm == 13:
        mm = 1
        yy += 1
    update_calendar()

# Create a Tkinter window
window = tk.Tk()
window.title("Calendar Widget")
window_width = 500
window_height = 500

# Calculate the screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the window position to center it
x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)

# Set the window position and size
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a label to display the current date and time
current_datetime = datetime.datetime.now()
current_date = current_datetime.strftime("%B %d, %Y")
current_time = current_datetime.strftime("%H:%M:%S")
date_label = tk.Label(window, text=current_date, font=("Courier", 16))
date_label.pack(pady=10)
time_label = tk.Label(window, text=current_time, font=("Courier", 16))
time_label.pack(pady=5)

# Define a greeting based on the time of day
hour = current_datetime.hour
if 5 <= hour < 12:
    greeting = "Good morning!"
    window.configure(background="lightblue")
elif 12 <= hour < 18:
    greeting = "Good afternoon!"
    window.configure(background="lightyellow")
else:
    greeting = "Good evening!"
    window.configure(background="lightgray")

# Create a label to display the greeting
greeting_label = tk.Label(window, text=greeting, font=("Courier", 26))
greeting_label.pack(pady=5)

# Create a label to display the calendar
calendar_label = tk.Label(window, font=("Courier", 34), bg="white", fg="black")
calendar_label.pack(pady=15)

# Create buttons for navigating to previous and next month
previous_button = tk.Button(window, text="Previous", command=previous_month, font=("Courier", 12))
previous_button.pack(side="left", padx=5)
next_button = tk.Button(window, text="Next", command=next_month, font=("Courier", 12))
next_button.pack(side="right", padx=5)

# Update the calendar initially
update_calendar()

# Start the Tkinter event loop
window.mainloop()
