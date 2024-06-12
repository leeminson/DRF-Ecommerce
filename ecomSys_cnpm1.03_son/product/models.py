from django.db import models
from django.utils.text import slugify
from polymorphic.models import PolymorphicModel
# Create your models here. 
class Product(PolymorphicModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True,editable=False,
    help_text='Unique value for product page URL, created from name.')
    image = models.ImageField(upload_to='img/')
    description = models.TextField()
    price = models.IntegerField()
    quantity=models.IntegerField()
    is_available = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords",max_length=255,help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length=255,
    help_text='Content for description meta tag') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super(Product ,self).save(*args , **kwargs)
        print('slug:'+self.slug)
    def __str__(self):
        return self.name    

    