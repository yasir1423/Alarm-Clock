import tkinter as tk
from datetime import datetime
import time
import threading
import winsound
# Function to update live clock
def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")  # 24-hour format
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)
# Function to check alarm
def check_alarm():
    while alarm_running:
        set_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        now = datetime.now().strftime("%H:%M:%S")
        if now == set_time:
            winsound.PlaySound("SystemHand",winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
            break
        time.sleep(1)
# Start alarm
def start_alarm():
    global alarm_running
    alarm_running = True
    threading.Thread(target=check_alarm, daemon=True).start()
    status_label.config(text="Alarm Activated", fg="green")
# Stop alarm
def stop_alarm():
    global alarm_running
    alarm_running = False
    winsound.PlaySound(None,winsound.SND_PURGE)
    status_label.config(text="Alarm Stopped", fg="red")
# GUI Window
root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x250")
# Live clock display
clock_label = tk.Label(root, font=("Arial", 40,"bold"), fg="black")
clock_label.pack(pady=10)
update_time()
# Alarm time inputs
tk.Label(root, text="Set Alarm Time (HH:MM:SS)", font=("Arial",17,"bold"),fg="dark blue").pack()
frame = tk.Frame(root)
frame.pack()
hour = tk.StringVar(value="00")
minute = tk.StringVar(value="00")
second = tk.StringVar(value="00")
tk.Entry(frame, textvariable=hour, width=2, font=("Arial", 14)).grid(row=0, column=0)
tk.Label(frame, text=":", font=("Arial", 14)).grid(row=0, column=1)
tk.Entry(frame, textvariable=minute, width=2, font=("Arial", 14)).grid(row=0, column=2)
tk.Label(frame, text=":", font=("Arial", 14)).grid(row=0, column=3)
tk.Entry(frame, textvariable=second, width=2, font=("Arial", 14)).grid(row=0, column=4)
# Buttons
tk.Button(root, text="Start Alarm", font=("Arial", 14),bg="black",fg="white",command=start_alarm).pack(pady=10)
tk.Button(root, text="Stop Alarm", font=("Arial", 14),bg="red",fg="white", command=stop_alarm).pack()
status_label = tk.Label(root, text="", font=("Arial", 12))
status_label.pack(pady=5)
root.mainloop()