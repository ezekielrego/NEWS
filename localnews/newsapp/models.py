from django.db import models

# Create your models here.
class latestnews(models.Model) :
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    img = models.ImageField(upload_to='img',null=True,default="NOTHING")
    newsline = models.CharField(max_length=5000,null=True,default="NOTHING")
    field = models.CharField(max_length=50,null=True,default="NOTHING")
    newsdetails = models.TextField(default="NOTHING")
    activityname = models.CharField(max_length=5000,default="NOTHING")  
    activitydetails = models.TextField(default="NOTHING")
    activityheading = models.TextField(default="NOTHING") 
    activityimg = models.ImageField(upload_to='img',default="NOTHING")
    wimg = models.ImageField(upload_to='img',null=True,default="NOTHING")
    wnewsline = models.CharField(max_length=5000,null=True,default="NOTHING")
    wfield = models.CharField(max_length=50,null=True,default="NOTHING")
    wnewsdetails = models.TextField(default="NOTHING",null=True)
    Breaking = models.BooleanField(default=False)
    def strol(self):
        return f"{self.id}{self.img}{self.newsdetails}{self.field}{self.newsline}{self.wimg}{self.wnewsdetails}{self.wfield}{self.wnewsline}"

class activitiess(models.Model) :
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    activityname = models.CharField(max_length=5000)  
    activitydetails = models.TextField()
    activityheading = models.TextField() 
    activityimg = models.ImageField(upload_to='img')
    def __str__(self):
        return f"{self.id}{self.activityname}{self.activitydetails}{self.activityheading}{self.activityimg}"

class weeklynews(models.Model) :
    wimg = models.ImageField(upload_to='img')
    wnewsline = models.CharField(max_length=5000)
    wfield = models.CharField(max_length=50)
    wnewsdetails = models.TextField(default="NOTHING")
    def jjk(self):
        return f"{self.id}{self.wimg}{self.wnewsdetails}{self.wfield}{self.wnewsline}"
