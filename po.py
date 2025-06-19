import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

FLASHCARD_FILE = "flashcards.json"

def load_flashcards():
    if os.path.exists(FLASHCARD_FILE):
        with open(FLASHCARD_FILE, 'r') as file:
            return json.load(file)
    return []

def save_flashcards(data):
    with open(FLASHCARD_FILE, 'w') as file:
        json.dump(data, file, indent=4)

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz App")
        self.root.geometry("400x300")
        self.root.configure(bg="lightblue")

        self.flashcards = load_flashcards()
        self.current_index = 0
        self.showing_answer = False

        self.card_label = tk.Label(root, text="", font=("Arial", 18), bg="white", width=30, height=5, wraplength=300)
        self.card_label.pack(pady=20)

        btn_frame = tk.Frame(root, bg="lightblue")
        btn_frame.pack()

        btn_style = {
    "bd": 0,
    "relief": "flat",
    "padx": 10,           
    "pady": 7,
    "width": 10,
    "cursor": "hand2"
}

        tk.Button(btn_frame, text="Previous", command=self.prev_card, **btn_style).grid(row=0, column=0, padx=8)
        tk.Button(btn_frame, text="Flip", command=self.flip_card, **btn_style).grid(row=0, column=1, padx=8)
        tk.Button(btn_frame, text="Next", command=self.next_card, **btn_style).grid(row=0, column=2, padx=8)


        action_frame = tk.Frame(root, bg="lightblue")
        action_frame.pack(pady=10)

        tk.Button(action_frame, text="Add", command=self.add_card, **btn_style).grid(row=0, column=0, padx=5)
        tk.Button(action_frame, text="Edit", command=self.edit_card, **btn_style).grid(row=0, column=1, padx=5)
        tk.Button(action_frame, text="Delete", command=self.delete_card, **btn_style).grid(row=0, column=2, padx=5)

        self.show_card()

    def show_card(self):
        if not self.flashcards:
            self.card_label.config(text="No flashcards found.\nClick 'Add' to create one.")
            return
        card = self.flashcards[self.current_index]
        text = card['answer'] if self.showing_answer else card['question']
        self.card_label.config(text=text)

    def flip_card(self):
        self.showing_answer = not self.showing_answer
        self.show_card()

    def next_card(self):
        if self.flashcards:
            self.current_index = (self.current_index + 1) % len(self.flashcards)
            self.showing_answer = False
            self.show_card()

    def prev_card(self):
        if self.flashcards:
            self.current_index = (self.current_index - 1) % len(self.flashcards)
            self.showing_answer = False
            self.show_card()

    def add_card(self):
        question = simpledialog.askstring("New Flashcard", "Enter Question:")
        answer = simpledialog.askstring("New Flashcard", "Enter Answer:")
        if question and answer:
            self.flashcards.append({"question": question, "answer": answer})
            save_flashcards(self.flashcards)
            self.current_index = len(self.flashcards) - 1
            self.showing_answer = False
            self.show_card()

    def edit_card(self):
        if not self.flashcards:
            return
        card = self.flashcards[self.current_index]
        new_question = simpledialog.askstring("Edit Question", "Update question:", initialvalue=card['question'])
        new_answer = simpledialog.askstring("Edit Answer", "Update answer:", initialvalue=card['answer'])
        if new_question and new_answer:
            self.flashcards[self.current_index] = {"question": new_question, "answer": new_answer}
            save_flashcards(self.flashcards)
            self.showing_answer = False
            self.show_card()

    def delete_card(self):
        if not self.flashcards:
            return
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this flashcard?")
        if confirm:
            del self.flashcards[self.current_index]
            if self.current_index >= len(self.flashcards):
                self.current_index = 0
            save_flashcards(self.flashcards)
            self.showing_answer = False
            self.show_card()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
