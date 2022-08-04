from django.db import models

NUMBER_BOXES = 5
BOXES = range(1, NUMBER_BOXES + 1)

class Card(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )

    date_create = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.question
