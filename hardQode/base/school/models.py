from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
    created_at = timezone.now()
    start_at = models.DateField()
    price = models.FloatField()
    min_students_in_group = models.IntegerField(default=1)
    max_students_in_group = models.IntegerField(default=3)
    def lessons_qty(self):
        return Lesson.objects.filter(category=Product).count()
    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    category = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    link_to_video = models.CharField(max_length=255)


class Group(models.Model):
    title = models.CharField(max_length=64)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def students(self):
        return Student.objects.filter(group=Group).count()
    


class Student(models.Model):
    name = models.CharField(max_length = 64)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
