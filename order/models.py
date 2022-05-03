from django.db import models


class Order(models.Model):
    user = models.ForeignKey('account.MyUser', on_delete=models.CASCADE, related_name='orders')
