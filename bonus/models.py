from django.db import models

class Bonus(models.Model):
    tipo_de_bonus = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tipo_de_bonus