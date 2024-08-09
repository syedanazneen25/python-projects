from question_class import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_text = question["question"]
    answer_text = question["correct_answer"]
    new_q = Question(question_text, answer_text)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.questions_left():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")