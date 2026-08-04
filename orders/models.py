from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    cp_amount = models.CharField(max_length=50)
    status = models.CharField(
        max_length=50,
        default="در انتظار"
    )

    def __str__(self):
        return self.name