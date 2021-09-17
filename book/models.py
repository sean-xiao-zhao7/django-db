from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Book (models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    author = models.CharField(max_length=100, null=True)
    is_best_selling = models.BooleanField(default=False)
    content = models.CharField(max_length=500, null=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)

    def get_absolute_url(self):
        return reverse("book-details", args=[self.slug])

    def __str__(self):
        return f"{self.title}. ({self.rating})"
