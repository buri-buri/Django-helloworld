from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=256)
    body=models.TextField()
    author=models.ForeignKey('Author',on_delete=models.CASCADE)
    def __str__(self):
        return self.title

# Article and Author are in OneToMany Relationship
class Author(models.Model):
    name=models.CharField(max_length=256)
    designation=models.CharField(max_length=256)
    def __str__(self):
        return self.name

# Publications and Articles are in ManyToMany Relationship
class Publications(models.Model):
    name=models.CharField(max_length=256)
    article=models.ManyToManyField('Article')
    def __str__(self):
        return self.name
