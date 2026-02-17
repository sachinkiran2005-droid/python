import tkinter as tk
from tkinter import messagebox

# --------- GAME VARIABLES ----------
p1_choice = ""
p2_choice = ""
p1_score = 0
p2_score = 0


# --------- LOGIN FUNCTION ----------
def login():
    username = user_entry.get()

    if username == "python":
        welcome_label.config(text=f"Welcome {username} 👋")
        login_frame.pack_forget()
        game_frame.pack(fill="both", expand=True)
    else:
        messagebox.showerror("Login Failed", "Username must be: python")


# --------- GAME FUNCTIONS ----------
def player1(choice):
    global p1_choice
    p1_choice = choice
    p1_label.config(text="Player 1: " + choice)

def player2(choice):
    global p2_choice
    p2_choice = choice
    p2_label.config(text="Player 2: " + choice)

def check_result():
    global p1_score, p2_score

    if p1_choice == "" or p2_choice == "":
        result_label.config(text="Both players choose first!", fg="yellow")
        return

    if p1_choice == p2_choice:
        result = "Draw"
        color = "yellow"
    elif (p1_choice == "Rock" and p2_choice == "Scissors") or \
         (p1_choice == "Paper" and p2_choice == "Rock") or \
         (p1_choice == "Scissors" and p2_choice == "Paper"):
        result = "Player 1 Wins!"
        p1_score += 1
        color = "lightgreen"
    else:
        result = "Player 2 Wins!"
        p2_score += 1
        color = "red"

    result_label.config(text=result, fg=color)
    score_label.config(text=f"P1: {p1_score}   P2: {p2_score}")

def reset_game():
    global p1_choice, p2_choice, p1_score, p2_score
    p1_choice = ""
    p2_choice = ""
    p1_score = 0
    p2_score = 0

    p1_label.config(text="Player 1:")
    p2_label.config(text="Player 2:")
    result_label.config(text="")
    score_label.config(text="P1: 0   P2: 0")


# --------- WINDOW ----------
root = tk.Tk()
root.title("RPS App")
root.geometry("350x600")


# ================= LOGIN PAGE =================
login_frame = tk.Frame(root, bg="#6c5ce7")  # purple background

tk.Label(login_frame, text="🎮 Welcome",
         font=("Arial", 24, "bold"),
         bg="#6c5ce7", fg="white").pack(pady=40)

tk.Label(login_frame, text="Enter Username",
         font=("Arial", 12),
         bg="#6c5ce7", fg="white").pack()

user_entry = tk.Entry(login_frame,
                      font=("Arial", 12),
                      width=20,
                      bd=3)
user_entry.pack(pady=15)

tk.Button(login_frame, text="Login",
          font=("Arial", 12, "bold"),
          bg="#00cec9",
          fg="white",
          width=12,
          command=login).pack(pady=20)

tk.Label(login_frame, text="(Username: python)",
         bg="#6c5ce7", fg="white").pack()

login_frame.pack(fill="both", expand=True)


# ================= GAME PAGE =================
game_frame = tk.Frame(root, bg="#1e272e")

welcome_label = tk.Label(game_frame, text="",
                         font=("Arial", 14),
                         bg="#1e272e", fg="#00cec9")
welcome_label.pack(pady=10)

tk.Label(game_frame, text="🎮 Rock Paper Scissors",
         font=("Arial", 18, "bold"),
         bg="#1e272e", fg="white").pack(pady=10)

score_label = tk.Label(game_frame, text="P1: 0   P2: 0",
                       font=("Arial", 16, "bold"),
                       bg="#1e272e", fg="#00cec9")
score_label.pack(pady=10)

# Player 1
frame1 = tk.Frame(game_frame, bg="#2f3640")
frame1.pack(pady=10, padx=20, fill="x")

tk.Label(frame1, text="Player 1 Choose",
         bg="#2f3640", fg="white").pack()

tk.Button(frame1, text="Rock", command=lambda: player1("Rock")).pack(pady=3)
tk.Button(frame1, text="Paper", command=lambda: player1("Paper")).pack(pady=3)
tk.Button(frame1, text="Scissors", command=lambda: player1("Scissors")).pack(pady=3)

p1_label = tk.Label(frame1, text="Player 1:", bg="#2f3640", fg="white")
p1_label.pack(pady=5)

# Player 2
frame2 = tk.Frame(game_frame, bg="#2f3640")
frame2.pack(pady=10, padx=20, fill="x")

tk.Label(frame2, text="Player 2 Choose",
         bg="#2f3640", fg="white").pack()

tk.Button(frame2, text="Rock", command=lambda: player2("Rock")).pack(pady=3)
tk.Button(frame2, text="Paper", command=lambda: player2("Paper")).pack(pady=3)
tk.Button(frame2, text="Scissors", command=lambda: player2("Scissors")).pack(pady=3)

p2_label = tk.Label(frame2, text="Player 2:", bg="#2f3640", fg="white")
p2_label.pack(pady=5)

result_label = tk.Label(game_frame, text="",
                        font=("Arial", 16, "bold"),
                        bg="#1e272e", fg="white")
result_label.pack(pady=20)

tk.Button(game_frame, text="Show Result",
          width=20, command=check_result).pack(pady=5)

tk.Button(game_frame, text="Reset Game",
          command=reset_game).pack(pady=10)

root.mainloop()