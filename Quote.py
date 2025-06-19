import tkinter as tk
import random

quotes = [
    ("The best way to get started is to quit talking and begin doing.", "Walt Disney"),
    ("Don't let yesterday take up too much of today.", "Will Rogers"),
    ("It's not whether you get knocked down, it's whether you get up.", "Vince Lombardi"),
    ("If you are working on something exciting, it will keep you motivated.", "Steve Jobs"),
    ("Success is not in what you have, but who you are.", "Bo Bennett"),
    ("Your time is limited, so don’t waste it living someone else’s life.", "Steve Jobs"),
    ("Dream, dream, dream. Dreams transform into thoughts and thoughts result in action.", "A.P.J. Abdul Kalam"),
    ("Failure will never overtake me if my determination to succeed is strong enough.", "A.P.J. Abdul Kalam"),
    ("Do not wait for leaders. Do it alone, person to person.", "Mother Teresa"),
    ("Be the change that you wish to see in the world.", "Mahatma Gandhi"),
    ("Arise, awake, and stop not till the goal is reached.", "Swami Vivekananda"),
    ("Take risks in your life. If you win, you can lead! If you lose, you can guide!", "Swami Vivekananda"),
    ("When something is important enough, you do it even if the odds are not in your favor.", "Elon Musk"),
    ("Persistence is very important. You should not give up unless you are forced to give up.", "Elon Musk"),
    ("Try not to become a man of success, but rather try to become a man of value.", "Albert Einstein"),
    ("Imagination is more important than knowledge.", "Albert Einstein"),
    ("In the middle of every difficulty lies opportunity.", "Albert Einstein"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("Act as if what you do makes a difference. It does.", "William James"),
    ("What lies behind us and what lies before us are tiny matters compared to what lies within us.", "Ralph Waldo Emerson"),
    ("Keep your face always toward the sunshine—and shadows will fall behind you.", "Walt Whitman"),
    ("Opportunities don't happen. You create them.", "Chris Grosser"),
    ("Everything you’ve ever wanted is on the other side of fear.", "George Addair"),
    ("Start where you are. Use what you have. Do what you can.", "Arthur Ashe"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("Hustle in silence and let your success make the noise.", "Unknown"),
    ("Success usually comes to those who are too busy to be looking for it.", "Henry David Thoreau"),
    ("The harder you work for something, the greater you’ll feel when you achieve it.", "Unknown"),
    ("Don’t watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ("Success is not final, failure is not fatal: It is the courage to continue that counts.", "Winston Churchill"),
    ("Do not be embarrassed by your failures, learn from them and start again.", "Richard Branson"),
    ("The future depends on what you do today.", "Mahatma Gandhi"),
    ("Success is not how high you have climbed, but how you make a positive difference to the world.", "Roy T. Bennett"),
    ("Push yourself, because no one else is going to do it for you.", "Unknown"),
    ("Great things never come from comfort zones.", "Unknown"),
]

def show_new_quote():
    quote, author = random.choice(quotes)
    quote_text.config(text=f'"{quote}"')
    author_text.config(text=f"- {author}")

root = tk.Tk()
root.title("Famous Quote Generator")
root.geometry("700x350")
root.config(bg="#121212")

quote_text = tk.Label(root, text="", wraplength=650, font=("Arial", 14),
fg="white", bg="#121212", justify="center")
quote_text.pack(pady=40)
author_text = tk.Label(root, text="", font=("Arial", 12, "italic"),
fg="#cccccc", bg="#121212")
author_text.pack()

new_quote_btn = tk.Button(root, text="New Quote", command=show_new_quote,
font=("Arial", 12), bg="#1f6feb", fg="white", padx=10, pady=5)
new_quote_btn.pack(pady=20)
show_new_quote()
root.mainloop()
