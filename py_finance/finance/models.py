from django.utils import timezone
from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_text = models.CharField(max_length=200)

    def __str__(self):
        return self.tag_text

class People(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Method_Payment(models.Model):
    method_id = models.CharField(max_length=200)

    def __str__(self):
        return self.method_id

class Spent(models.Model):
    spant_name = models.CharField('Spent identication', max_length=200)
    price = models.FloatField('Price payed')
    dateSpent = models.DateField('Date of expense')
    tag_FK = models.ForeignKey(Tag, on_delete=models.CASCADE)
    method_FK = models.ForeignKey(Method_Payment, on_delete=models.CASCADE)

    def __str__(self):
        return self.spant_name

class Incoming(models.Model):
    amount = models.FloatField()
    people_FK = models.ForeignKey(People, on_delete=models.CASCADE)
    dateEarn = models.DateField('Date of earn')

    def __str__(self):
        resp = str(self.dateEarn) + " | R$" + str(self.amount) + " | " + str(self.people_FK.name)
        return resp
