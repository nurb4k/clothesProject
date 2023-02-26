from django.db import models


class role(models.Model):
    name = models.CharField(max_length=20)


class user(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    role_id = models.ForeignKey(role, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


class category(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=5)


class clothes(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=15)
    text = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    gender = models.BooleanField()
    is_published = models.BooleanField(default=False)
    category_id = models.ForeignKey(category, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
