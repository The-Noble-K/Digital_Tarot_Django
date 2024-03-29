from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=100)
    meaning = models.TextField()
    reversal = models.TextField()
    card_id = models.IntegerField()
    image = models.ImageField(upload_to="img/")

    def __str__(self):
        return "%s, %s, %s, %s, %s" %(self.name, self.meaning, self.reversal, self.card_id, self.image)

