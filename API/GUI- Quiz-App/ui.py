THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white", font=("Arial", 15,"normal" ))
        self.score_label.grid(row=0, column=1)
        self.score_label.config(background=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width= 280,
            text="Some Text", 
            fill=THEME_COLOR, 
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
        self.true_img = PhotoImage(file="API/GUI- Quiz-App/images/true.png")
        self.false_img = PhotoImage(file="API/GUI- Quiz-App/images/false.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text =self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= f"You have reached end of the Quiz. Final Score:{self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.score_label.config(fg=THEME_COLOR)
    def true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        
