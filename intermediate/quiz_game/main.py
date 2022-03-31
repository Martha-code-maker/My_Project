from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for quest in question_data:
    q_text = quest["question"]
    q_answer = quest["correct_answer"]
    question = Question(q_text, q_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
        quiz.next_question()
print("\n")
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")