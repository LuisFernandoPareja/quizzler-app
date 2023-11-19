from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface(Tk):
    def __init__(self, quiz_brain: QuizBrain):
        super().__init__()
        self.title('Quizzler')
        self.quiz = quiz_brain
        self.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300)
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text='',
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.score_label = Label(text=f'Score: 0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)
        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')

        self.true_button = Button(image=true_img, command=self.true_answer, highlightthickness=0)
        self.false_button = Button(image=false_img, command=self.false_answer, highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()


        self.mainloop()

    def get_next_question(self):
        self.score_label.config(text=f'Score: {self.quiz.score}')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.config(bg='white')
            self.canvas.itemconfig(self.question, text=q_text)

        else:
            self.canvas.config(bg='white')
            self.canvas.itemconfig(self.question, text=f"GAME OVER\nYou're score: {self.quiz.score}/"
                                                       f"{len(self.quiz.question_list)}")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def false_answer(self):
        is_right = self.quiz.check_answer(user_answer='False')
        self.give_feedback(is_right)

    def true_answer(self):
        is_right = self.quiz.check_answer(user_answer='True')
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.after(1000, self.get_next_question)



