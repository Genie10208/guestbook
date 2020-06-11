from django.db import models

# Create your models here.
class Message(models.Model):
    user = models.CharField("姓++++名", max_length=50)
    subject = models.CharField("主題",max_length=280)
    content = models.TextField("內++容")
    publication_date = models.DateTimeField("留言時間", auto_now_add=True)

    def __str__(self):
        return self.user + ":" + self.subject