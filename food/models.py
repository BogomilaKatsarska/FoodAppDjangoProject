from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):
    item_name = models.CharField(
        max_length=200,
    )
    item_desc = models.CharField(
        max_length=200,
    )
    item_price = models.IntegerField()
    item_image = models.URLField(
        default='https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg',
        null=True,
        blank=True,
    )
    user_name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1,
    )

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('food:detail', kwargs={'pk': self.pk})