from django.db import models



class category(models.model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Book(models.model):

    status_book = [

        ('availble','availble')
        ('rental','rental')
        ('sold','sold')



    ]





    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    photo_book = models.ImageField(upload_to ='photos',null=True, blank=True)
    photo_author = photo_book = models.ImageField(upload_to ='photos',null=True, blank=True)
    pages = models.IntegerField(null=True, blank = True)
    price = models.DecimalField(max_digits=5, null=True, blank=True)
    retal_price_day= models.DecimalField(max_digits=5, null=True, blank=True)
    retal_period = models.IntegerField(null=True, blank = True) 
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=250, choices = status_book, null=True, blank=True)
    category = models.ForeignKey(category, on_delete = models.PROJECT,null=True, blank = True)


    def __str__(self):
        return self.name