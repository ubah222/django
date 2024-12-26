from django.db import models



    
    

class post(models.Model): # select * from post
    title = models.CharField(max_length=200)
    project = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.project
    



class comment(models.Model):
    title = models.CharField(max_length=200)
    email= models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.email
    

class author(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.published_date
    









