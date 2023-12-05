import tkinter as tk
from tkinter import messagebox

# Define the quiz questions and answers
quiz_data = [
     {
        "question": "What is the primary function of an operating system?",
        "answers": ["Manage hardware resources", "Create documents", "Design websites"],
        "correct_answer": "Manage hardware resources"
    },
    {
        "question": "Which of the following is an example of a programming language?",
        "answers": ["HTML", "Excel", "Python"],
        "correct_answer": "Python"
    },
    {
        "question": "What does CPU stand for?",
        "answers": ["Central Processing Unit", "Computer Processing Unit", "Control Processing Unit"],
        "correct_answer": "Central Processing Unit"
    },
    {
        "question": "What is the purpose of a firewall?",
        "answers": ["Protect against viruses", "Control network traffic", "Store data"],
        "correct_answer": "Control network traffic"
    },
    {
        "question": "What is the function of RAM in a computer?",
        "answers": ["Store long-term data", "Execute program instructions", "Display images on the screen"],
        "correct_answer": "Execute program instructions"
    },
    {
        "question": "What is the role of an input device in a computer system?",
        "answers": ["Display output to the user", "Process data", "Enter data into the system"],
        "correct_answer": "Enter data into the system"
    },
    {
        "question": "Which of the following is an example of a secondary storage device?",
        "answers": ["USB flash drive", "RAM", "Processor"],
        "correct_answer": "USB flash drive"
    },
    {
        "question": "What is the purpose of an IP address?",
        "answers": ["Identify a website's domain name", "Establish an internet connection", "Identify a device on a network"],
        "correct_answer": "Identify a device on a network"
    },
    {
        "question": "What does HTML stand for?",
        "answers": ["Hyper Text Markup Language", "High Tech Markup Language", "Home Tool Markup Language"],
        "correct_answer": "Hyper Text Markup Language"
    },
    {
        "question": "What is the function of an output device in a computer system?",
        "answers": ["Enter data into the system", "Process data", "Display output to the user"],
        "correct_answer": "Display output to the user"
    },
    {
        "question": "Which of the following is an example of an application software?",
        "answers": ["Operating system", "Web browser", "Device driver"],
        "correct_answer": "Web browser"
    },
    {
        "question": "What is the purpose of a database management system?",
        "answers": ["Create spreadsheets", "Store and manage data", "Protect against malware"],
        "correct_answer": "Store and manage data"
    },
    {
        "question": "What is the role of a network router?",
        "answers": ["Connect to the internet", "Process data", "Control network traffic"],
        "correct_answer": "Control network traffic"
    },
    {
        "question": "What is the purpose of an antivirus software?",
        "answers": ["Create documents", "Protect against viruses", "Display images on the screen"],
        "correct_answer": "Protect against viruses"
    },
    {
        "question": "What is the function of a web server?",
        "answers": ["Store and manage data", "Connect to the internet", "Host websites"],
        "correct_answer": "Host websites"
    },
    {
        "question": "Which of the following is an example of a high-level programming language?",
        "answers": ["Assembly language", "Java", "Binary code"],
        "correct_answer": "Java"
    },
    {
        "question": "What does URL stand for?",
        "answers": ["Universal Resource Locator", "Uniform Resource Locator", "Unique Resource Locator"],
        "correct_answer": "Uniform Resource Locator"
    },
    {
        "question": "What is the purpose of a spreadsheet software?",
        "answers": ["Store and manage data", "Create presentations", "Perform calculations"],
        "correct_answer": "Perform calculations"
    },

]

def open_quiz_game():
    quiz_window = tk.Toplevel()
    quiz_window.title("ITEC ESSENTIAL")
    quiz_window.geometry("400x350")
    quiz_window.configure(bg='#BDEDFF')

    current_question_index = 0
    score = 0

    def load_question():
        nonlocal current_question_index
        if current_question_index < len(quiz_data):
            question = quiz_data[current_question_index]
            question_label.config(text=question["question"])
            for i, answer_button in enumerate(answer_buttons):
                answer_button.config(text=question["answers"][i])
        else:
            question_label.config(text="Quiz completed!")
            for answer_button in answer_buttons:
                answer_button.config(state="disabled")

    def answer_selected(answer_index):
        nonlocal current_question_index, score
        question = quiz_data[current_question_index]
        selected_answer = question["answers"][answer_index]
        if selected_answer == question["correct_answer"]:
            score += 1
            score_label.config(text="Score: {}".format(score))
        else:
            messagebox.showinfo(title="Incorrect", message="The correct answer is: {}".format(question["correct_answer"]))

        current_question_index += 1
        load_question()

    def return_to_login():
        quiz_window.destroy()
        window.deiconify()

    def next_question():
        nonlocal current_question_index
        current_question_index += 1
        load_question()

    # Create the quiz game UI elements
    question_label = tk.Label(quiz_window, text="Question goes here", bg='#BDEDFF', fg="#A9A9A9", font=("Arial", 16))
    question_label.pack(pady=20)

    answer_buttons = []
    for i in range(3):
        answer_button = tk.Button(quiz_window, text="Answer {}".format(i+1), bg="#BDEDFF", fg="#A9A9A9", font=("Arial", 12), command=lambda i=i: answer_selected(i))
        answer_button.pack()
        answer_buttons.append(answer_button)

    score_label = tk.Label(quiz_window, text="Score: 0", bg='#BDEDFF', fg="#A9A9A9", font=("Arial", 16))
    score_label.pack(pady=20)

    return_button = tk.Button(quiz_window, text="Return", bg="#BDEDFF", fg="#A9A9A9", font=("Arial", 12), command=return_to_login)
    return_button.pack(side="left", padx=20)
    
    next_button = tk.Button(quiz_window, text="Next", bg="#BDEDFF", fg="#A9A9A9", font=("Arial", 12), command=next_question)
    next_button.pack(side="right", padx=20)

    load_question()

def exit_program():
        result = messagebox.askquestion("Exit", "Are you sure you want to exit?")
        if result == "yes":
           window.destroy()

def login():
    username = "COSC23"
    password = "1111"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        window.withdraw()
        open_quiz_game()
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

window = tk.Tk()
window.title("Login form")
window.geometry('400x350')
window.configure(bg='#BDEDFF')

frame = tk.Frame(bg='#BDEDFF')

login_label = tk.Label(frame, text="Login", bg='#BDEDFF', fg="#A9A9A9", font=("Arial", 30))
username_label = tk.Label(frame, text="Username", bg='#BDEDFF', fg="#A9A9A9", font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 16))
password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
password_label = tk.Label(frame,text="Password", bg='#BDEDFF', fg="#A9A9A9", font=("Arial", 16))
login_button = tk.Button(frame, text="Login", bg="#BDEDFF", fg="#A9A9A9", font=("Arial", 16), command=login)
exit_button = tk.Button(frame, text="Exit", bg="#BDEDFF", fg="#A9A9A9", font=("Arial", 16), command=exit_program)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=50)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, pady=20)
exit_button.grid(row=3, column=1, pady=20)

frame.pack()

window.mainloop()