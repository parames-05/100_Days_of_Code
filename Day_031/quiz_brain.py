class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.qn_list = question_list
        self.score = 0
    def Still_has_qn(self):
        if self.question_number < len(self.qn_list):
            return True
        else:
            return False



    def next_qn(self):
        current_qn=self.qn_list[self.question_number]
        self.question_number+=1
        ip= input(f"Q.{self.question_number}: {current_qn.txt} (True/False)").lower()
        self.check_answer(ip,current_qn.ans)

    def check_answer(self, useranswer,crt_answer):
        if useranswer.lower() == crt_answer.lower():
            print("You got it right!!! LESSS GOOOO")
            self.score += 1
        else:
            print(f"Better luck next time, the correct answer is {crt_answer}")
        print(f"The current score is {self.score}/{self.question_number}")
        print('\n'*2)






