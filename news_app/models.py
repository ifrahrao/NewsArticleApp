from django.db import models


# Create your models here.
class NewsCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=30)
    job_description = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class NewsArticle(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    content = models.TextField()
    published = models.BooleanField()
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(NewsCategory,on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


