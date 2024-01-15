from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    status = models.IntegerField(default=0)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book'
        verbose_name = '书'
        verbose_name_plural = verbose_name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.status == '10' or self.status == 10:
            self.price = 20
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def update_price(self):
        self.price = 10