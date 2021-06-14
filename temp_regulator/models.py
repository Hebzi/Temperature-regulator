from django.db import models


class Temperature(models.Model):
    temp = models.DecimalField(max_digits=4, decimal_places=1, default=20.0)

    def __str__(self):
        return str(self.temp)
