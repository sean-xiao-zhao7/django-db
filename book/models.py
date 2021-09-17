from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.aggregates import Count
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'countries'

class Address(models.Model):
    address = models.CharField(max_length=80)
    zip = models.CharField(max_length=20)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.address}, {self.city}"

    class Meta:
        verbose_name_plural = 'addresses'

class Author (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def fullname(self):
        return f"{self.last_name}, {self.first_name}"   
    
    def __str__(self):
        return self.fullname()

class Book (models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='book_author')
    is_best_selling = models.BooleanField(default=False)
    content = models.CharField(max_length=500, null=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)
    country = models.ManyToManyField(Country, related_name='book_countries')

    def get_absolute_url(self):
        return reverse("book-details", args=[self.slug])

    def __str__(self):
        return f"{self.title}. ({self.rating})"