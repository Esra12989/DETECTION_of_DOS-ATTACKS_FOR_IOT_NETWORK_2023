from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)    
    image = models.ImageField(upload_to="images",default="default/user.png")
    
    
class Post(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_id = models.AutoField
    post_price = models.CharField(max_length=5000)
    post_predict = models.CharField(max_length=5000)

    timestamp= models.DateTimeField(default=now)
    image = models.ImageField(upload_to="images",default="")


    


