from quiz_brain import QuizBrain
from data import question_data
from question_model import Question
question_bank = []
for qn in question_data:
    qn_sen= qn["text"]
    qn_ans = qn["answer"]
    new_qn = Question(qn_sen, qn_ans)
    question_bank.append(new_qn)

QuizBrain(question_bank)
quiz = QuizBrain(question_bank)
while quiz.Still_has_qn():
    quiz.next_qn()

print(f'\n You have completed the quizzz...\n The final score is {quiz.score}/{quiz.question_number}')
