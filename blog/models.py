from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
