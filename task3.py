import tkinter as tk
from tkinter import messagebox as msgbox
import random

# Initialise the user_score and comp_score
user_score = 0
comp_score = 0 

# Comment for the result display
tie_comms = ["Honors even, and the drama lives on!", "No winner, no loser—just pure competition!", "All tied up—what a nail-biter!", "Neither side blinked—it’s a perfect standoff!", "A stalemate, but far from a dull affair!"]
win_comms = ["Victory sealed—what a performance!", "Clinched it in style—what a finish!", "Triumph written all over", "A commanding win and a statement made!"]
lose_comms = ["Defeat today, lessons for tomorrow.", "A tough loss, but the spirit was there.", "The battle’s lost, but the war goes on.", "Beaten, but not broken."]

# Decide the winner
def winner(user, comp):
    if user == comp:
        return "TIE"
    elif (user == "Rock" and comp == "Scissors") or (user == "Paper" and comp == "Rock") or (user == "Scissors" and comp == "Paper"):
        return "WIN"
    else:
        return "LOSE"

# Start the game
def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = winner(user_choice, comp_choice)

    if result == "WIN":
        user_score += 1
        comment = random.choice(win_comms)
        outcome = "You Win!"
    elif result == "LOSE":
        comp_score += 1
        comment = random.choice(lose_comms)
        outcome = "Computer Wins!"
    else:
        comment = random.choice(tie_comms)
        outcome = "It's a Tie!"

    result_label.config(text=f"You: {user_choice}\nComputer: {comp_choice}\nResult: {outcome}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {comp_score}")
    comment_label.config(text=comment)

# Exit game
def quit():
    msg = msgbox.askyesno("Quit", "Do you want to quit the game?")
    if msg:
        root.destroy()

# Setup the GUI
root = tk.Tk()
root.title("ROCK PAPER SCISSORS GAME")
root.geometry("600x600")
root.config(bg="#FDEBD0")  # Pastel peach background

title = tk.Label(root, text="ROCK PAPER SCISSORS GAME", font=("Helvetica", 20, "bold"),
                 bg="#FDEBD0", fg="#5D6D7E", justify="center")
title.pack(pady=40, anchor="center")

comment_label = tk.Label(root, text="", font=("Helvetica", 15), bg="#FDEBD0", fg="#4A235A")
comment_label.pack(pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 15), bg="#FDEBD0", fg="#154360")
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Helvetica", 15), bg="#FDEBD0", fg="#6E2C00")
score_label.pack(pady=20)

# Buttons
btn_frame = tk.Frame(root, bg="#FDEBD0")
btn_frame.pack(pady=20)

rock_btn = tk.Button(btn_frame, text="Rock", font=("Helvetica", 15), width=12, command=lambda: play("Rock"), bg="#FFC1CC")  # pastel pink
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(btn_frame, text="Paper", font=("Helvetica", 15), width=12, command=lambda: play("Paper"), bg="#B0E57C")  # pastel green
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(btn_frame, text="Scissors", font=("Helvetica", 15), width=12, command=lambda: play("Scissors"), bg="#B5D3FF")  # pastel blue
scissors_btn.grid(row=0, column=2, padx=10)

quit_btn = tk.Button(root, text="Quit", font=("Helvetica", 15), command=quit, width=15, bg="#F5B7B1")
quit_btn.pack(pady=20)

root.mainloop()
