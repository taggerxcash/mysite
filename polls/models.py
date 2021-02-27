from django.db import models

# Модель для обработки вопроса
class Question(models.Model):
    text = models.CharField(max_length=500)
    pub_Date = models.DateTimeField('Date published')

    def __str__(self):
        return self.text

# Модель для обработки варианта ответа на вопрос
class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Связываем qustion & choises
    text = models.CharField(max_length=500)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.text