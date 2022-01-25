from django.db import models


class Ipost(models.Model):
    # insta_user = models.ForeignKey(, on_delete=models.CASCADE,
                                #   related_name='PostedBy')
    caption = models.CharField(max_length=150)
    location = models.CharField(max_length=50)
    can_comment = models.BooleanField(default=True)
    tags = models.CharField(max_length=50)
    image = models.ImageField(max_length=50)
    
 
    def __str__(self):
        return self.caption

class InstagramUser(models.Model):
    username = models.CharField(max_length=100)
    E_mail = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    likedpost = models.ForeignKey(Ipost, on_delete=models.CASCADE,
                                  related_name='Likedby')

    def __str__(self):
        return self.username

