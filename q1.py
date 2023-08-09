from tkinter import *
from tkinter import messagebox

Questions = ["1) which of the following is the correct extension of the python file?",
             "2) Who developed python programming language?",
             "3) Which keyword is used for function in python language?"]
Options = [[".python", ".pl", ".py"],
           ["wick van Rossum", "rasmus lerdorf", "Guido van Rossum",],
           ["function", "def", "fun"]]

Answers = [3, 3, 2]

Score = 0
Total_No_Questions = 3
Question_no = 1

def start_again():
    global Score,Question_no
    
    Score = 0
    Question_no = 1
    val1.set(0)
    val2.set(0)
    val3.set(0)
    question.config(text=Questions[Question_no-1])
    option1.config(text=Options[Question_no-1][0])
    option2.config(text=Options[Question_no-1][1])
    option3.config(text=Options[Question_no-1][2])
    next_b.config(text="next")
    play_again.place_forget()
    score.place_forget()
    root.pack()

    

def next():
    global Score, Question_no
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    elif val3.get() == 1:
        selected_option = 3
    else:
        selected_option = -1

    if Answers[Question_no-1] == selected_option :
        Score += 1
        print("Correct!")
        messagebox.showinfo("","correct!") 
    else:
        print("Incorrect!")
        messagebox.showinfo("","Incorrect!")
        
    Question_no += 1
       



    if Question_no > Total_No_Questions:
        root.pack_forget()
        score.place(relx=.5, rely=.5,anchor=CENTER)
        play_again.place(relx=.45, rely=.1)
        
        score.config(text="Score:"+str(Score), font=("Arial", 15))
       
         


    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        question.config(text=Questions[Question_no-1])
        option1.config(text=Options[Question_no-1][0])
        option2.config(text=Options[Question_no-1][1])
        option3.config(text=Options[Question_no-1][2])
        

 


def check(option):
    if option == 1:
        val2.set(0)
        val3.set(0)
    elif option == 2:
        val1.set(0)
        val3.set(0)
    else:
        val2.set(0)
        val1.set(0)


def start_game():
    user_screen.place_forget()
    root.pack()


Win = Tk()
Win.geometry("800x450")
Win.title("Quiz Game")

user_screen = Frame()
user_screen.place(relx=0.5, rely=0.5, anchor=CENTER)
intro_message = Label(user_screen, width=60, font=("Arial", 15), text="Welcome to Quiz Game")
intro_message.pack()
play_b = Button(user_screen, text="Play  Quiz",width=10,bg="black",fg="white",font=("ariel",10), command=start_game)
play_b.pack()

root = Frame(Win)
root.pack_forget()

question = Label(root, width=60, font=("Arial", 15,"bold"), text=Questions[0])
question.pack(pady=10)

val1 = IntVar()
val2 = IntVar()
val3 = IntVar()

option1 = Checkbutton(root, variable=val1,font=("ariel",15), text=Options[0][0], command=lambda: check(1))
option1.pack(pady=5)

option2 = Checkbutton(root, variable=val2,font=("ariel",15), text=Options[0][1], command=lambda: check(2))
option2.pack(pady=5)

option3 = Checkbutton(root, variable=val3,font=("ariel",15), text=Options[0][2], command=lambda: check(3))
option3.pack(pady=5)

next_b = Button(root, text="next",width=15,bg="black",fg="white",font=("ariel",15), command=next)
next_b.pack(pady=5)

score = Label(Win)
score.place_forget()

play_again = Button(Win,text= "Play Again",command=start_again,width=10,bg="black",fg="white",font=("ariel",10))
play_again.place_forget()



Win.mainloop()
