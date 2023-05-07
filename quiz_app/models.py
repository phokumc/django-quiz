from django.db import models

class DjangoQuizQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()
    option_1 = models.TextField()
    option_2 = models.TextField()
    option_3 = models.TextField()
    option_4 = models.TextField()

    def __str__(self):
        return f'Question: {self.question} | Answer: {self.answer} | Option_1: {self.option_1} | Option_2: {self.option_2} | Option_3: {self.option_3} | Option_4: {self.option_4}'

class PythonQuizQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()
    option_1 = models.TextField()
    option_2 = models.TextField()
    option_3 = models.TextField()
    option_4 = models.TextField()

    def __str__(self):
        return f'Question: {self.question} | Answer: {self.answer} | Option_1: {self.option_1} | Option_2: {self.option_2} | Option_3: {self.option_3} | Option_4: {self.option_4}'
    

class HtmlQuizQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()
    option_1 = models.TextField()
    option_2 = models.TextField()
    option_3 = models.TextField()
    option_4 = models.TextField()

    def __str__(self):
        return f'Question: {self.question} | Answer: {self.answer} | Option_1: {self.option_1} | Option_2: {self.option_2} | Option_3: {self.option_3} | Option_4: {self.option_4}'
    
    
class CssQuizQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()
    option_1 = models.TextField()
    option_2 = models.TextField()
    option_3 = models.TextField()
    option_4 = models.TextField()

    def __str__(self):
        return f'Question: {self.question} | Answer: {self.answer} | Option_1: {self.option_1} | Option_2: {self.option_2} | Option_3: {self.option_3} | Option_4: {self.option_4}'
    

class JavascriptQuizQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()
    option_1 = models.TextField()
    option_2 = models.TextField()
    option_3 = models.TextField()
    option_4 = models.TextField()

    def __str__(self):
        return f'Question: {self.question} | Answer: {self.answer} | Option_1: {self.option_1} | Option_2: {self.option_2} | Option_3: {self.option_3} | Option_4: {self.option_4}'