import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("fitness_tracker.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS fitness_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    activity TEXT NOT NULL,
    duration INTEGER,
    calories INTEGER
)
""")
conn.commit()


def add_entry():
    activity = activity_entry.get()
    duration = duration_entry.get()
    calories = calories_entry.get()

    if not activity or not duration or not calories:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    try:
        duration = int(duration)
        calories = int(calories)
    except ValueError:
        messagebox.showwarning("Input Error", "Duration and Calories must be numbers.")
        return

    cursor.execute("INSERT INTO fitness_log (activity, duration, calories) VALUES (?, ?, ?)",
    (activity, duration, calories))
    conn.commit()
    show_summary()
    activity_entry.delete(0, tk.END)
    duration_entry.delete(0, tk.END)
    calories_entry.delete(0, tk.END)

def show_summary():
    display_box.delete(0, tk.END)
    cursor.execute("SELECT * FROM fitness_log")
    records = cursor.fetchall()

    total_duration = 0
    total_calories = 0

    for rec in records:
        display_box.insert(tk.END, f"{rec[1]} | {rec[2]} min | {rec[3]} kcal")
        total_duration += rec[2]
        total_calories += rec[3]

    summary_label.config(text=f"Total: {total_duration} mins | {total_calories} kcal")

root = tk.Tk()
root.title("Fitness Tracker")
root.geometry("600x500")
root.config(bg="#f4f4f4")

tk.Label(root, text="🏃 Fitness Tracker App", font=("Arial", 16, "bold"), bg="#f4f4f4").pack(pady=10)

frame = tk.Frame(root, bg="#f4f4f4")
frame.pack(pady=10)

tk.Label(frame, text="Activity:", font=("Arial", 12), bg="#f4f4f4").grid(row=0, column=0, padx=5, pady=5, sticky="e")
activity_entry = tk.Entry(frame, width=30)
activity_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Duration (mins):", font=("Arial", 12), bg="#f4f4f4").grid(row=1, column=0, padx=5, pady=5, sticky="e")
duration_entry = tk.Entry(frame, width=30)
duration_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Calories Burned:", font=("Arial", 12), bg="#f4f4f4").grid(row=2, column=0, padx=5, pady=5, sticky="e")
calories_entry = tk.Entry(frame, width=30)
calories_entry.grid(row=2, column=1, padx=5, pady=5)

add_btn = tk.Button(root, text="Add Entry", command=add_entry, font=("Arial", 12), bg="#28a745", fg="white")
add_btn.pack(pady=10)

tk.Label(root, text="📋 Daily Summary", font=("Arial", 12, "bold"), bg="#f4f4f4").pack()

display_box = tk.Listbox(root, width=70, height=10, font=("Courier", 10))
display_box.pack(pady=10)
summary_label = tk.Label(root, text="Total: 0 mins | 0 kcal", font=("Arial", 12), bg="#f4f4f4")
summary_label.pack(pady=5)
show_summary()
root.mainloop()
conn.close()
