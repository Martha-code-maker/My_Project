from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", font=("Courier", 13, "bold"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 18, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        check_img = PhotoImage(file="./images/true.png")
        self.check_button = Button(image=check_img, highlightthickness=0, command=self.get_check_answer_True)
        self.check_button.grid(column=0, row=2)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.get_check_answer_False)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.check_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def get_check_answer_True(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def get_check_answer_False(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
