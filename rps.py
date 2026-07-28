import tkinter as tk
import random

# ---------------- Window ----------------

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x600")
root.resizable(False, False)
root.configure(bg="#1E1E1E")


# ---------------- Variables ----------------

player_score = 0
computer_score = 0


# ---------------- Functions ----------------

def play(player_choice):
    global player_score, computer_score

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a Draw!"

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        player_score += 1

    else:
        result = "Computer Wins!"
        computer_score += 1


    player_choice_label.config(
        text=f"You chose: {player_choice}"
    )

    computer_choice_label.config(
        text=f"Computer chose: {computer_choice}"
    )

    result_label.config(
        text=result
    )

    score_label.config(
        text=f"You: {player_score}     Computer: {computer_score}"
    )


def reset_game():
    global player_score, computer_score

    player_score = 0
    computer_score = 0

    player_choice_label.config(
        text="You chose:"
    )

    computer_choice_label.config(
        text="Computer chose:"
    )

    result_label.config(
        text="Choose Rock, Paper or Scissors"
    )

    score_label.config(
        text="You: 0     Computer: 0"
    )


# ---------------- Title ----------------

title = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 26, "bold"),
    bg="#1E1E1E",
    fg="white"
)

title.pack(pady=25)


# ---------------- Result Area ----------------

player_choice_label = tk.Label(
    root,
    text="You chose:",
    font=("Arial", 15),
    bg="#1E1E1E",
    fg="white"
)

player_choice_label.pack(pady=5)


computer_choice_label = tk.Label(
    root,
    text="Computer chose:",
    font=("Arial", 15),
    bg="#1E1E1E",
    fg="white"
)

computer_choice_label.pack(pady=5)


result_label = tk.Label(
    root,
    text="Choose Rock, Paper or Scissors",
    font=("Arial", 18, "bold"),
    bg="#1E1E1E",
    fg="#4CAF50"
)

result_label.pack(pady=25)


score_label = tk.Label(
    root,
    text="You: 0     Computer: 0",
    font=("Arial", 16, "bold"),
    bg="#1E1E1E",
    fg="white"
)

score_label.pack(pady=10)


# ---------------- Buttons ----------------

button_frame = tk.Frame(
    root,
    bg="#1E1E1E"
)

button_frame.pack(pady=20)


rock_button = tk.Button(
    button_frame,
    text="🪨 Rock",
    font=("Arial", 16, "bold"),
    width=12,
    height=2,
    command=lambda: play("Rock")
)

rock_button.grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)


paper_button = tk.Button(
    button_frame,
    text="📄 Paper",
    font=("Arial", 16, "bold"),
    width=12,
    height=2,
    command=lambda: play("Paper")
)

paper_button.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)


scissors_button = tk.Button(
    button_frame,
    text="✂ Scissors",
    font=("Arial", 16, "bold"),
    width=12,
    height=2,
    command=lambda: play("Scissors")
)

scissors_button.grid(
    row=1,
    column=0,
    columnspan=2,
    pady=10
)


# ---------------- Reset Button ----------------

reset_button = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 15, "bold"),
    width=15,
    height=2,
    bg="#F44336",
    fg="white",
    command=reset_game
)

reset_button.pack(pady=25)


# ---------------- Run ----------------

root.mainloop()