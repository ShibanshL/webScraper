from django.db import models
# from django.contrib.postgres.fields import ArrayField


pseudoData = {'Symbol':'null'}

class webScrModel(models.Model):
    Symbol = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.Symbol


class sendArrayModal(models.Model):
    # Data = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    # Data = models.CharField(max_length=200)
    Data = models.ManyToManyField(webScrModel)
    # id= models.IntegerField()

    # def __str__(self):
    #     return self.Data
    
    def __repr__(self) -> str:
        return self.Data