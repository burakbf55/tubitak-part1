from django.db import models

types = [('employee','employee'),('visitor','visitor')]
class Profile(models.Model):
    first_name = models.CharField(max_length=70)#isim
    last_name = models.CharField(max_length=70)#soyisim
    date = models.DateField()#tarih
    phone = models.BigIntegerField()#telefon numarası
    email = models.EmailField()#email
    ranking = models.IntegerField()#rank
    profession = models.CharField(max_length=200)#profesyonel alan
    status = models.CharField(choices=types,max_length=20,null=True,blank=False,default='employee')#statü
    present = models.BooleanField(default=False)
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True)
    shift = models.TimeField()
    def __str__(self):
        return self.first_name +' '+self.last_name


class LastFace(models.Model):
    last_face = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.last_face

