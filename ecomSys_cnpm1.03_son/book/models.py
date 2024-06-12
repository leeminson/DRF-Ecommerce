from django.db import models
from django.utils.text import slugify

from product.models import Product


# Create your models here.
class BookCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True),
    description = models.TextField(),
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
class Author(models.Model):
    class gender(models.TextChoices):
        Male='Male'
        Female='Female'
    name=models.CharField(max_length=255,unique="true")
    slug=models.SlugField(max_length=50,unique="true",editable=False)
    gender=models.CharField(max_length=25,
                            choices=gender.choices,
                            default=gender.Male)
    def __str__(self) -> str:
        return self.name 
    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super(Author ,self).save(*args , **kwargs)
        print('slug:'+self.slug) 
class Publisher(models.Model):
    name=models.CharField(max_length=255,unique="true")
    slug=models.SlugField(max_length=50,unique="true",editable=False)
    address=models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name
class Book(Product):
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    numberofpage=models.IntegerField()
    Book_Category=models.ManyToManyField(BookCategory)
    authors=models.ManyToManyField(Author)
    
    def __str__(self) -> str:
        return self.name  
