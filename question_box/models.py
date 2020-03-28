from django.db import models


class QuestionAnswerPair(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
