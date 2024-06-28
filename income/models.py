from django.db import models
import datetime
from django.contrib.auth.hashers import make_password,check_password
# Create your models here.
class Login(models.Model):
    si_number = models.IntegerField(unique=True, null=True, blank=True)
    # si_number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def save(self, *args, **kwargs):
        if not self.si_number:
            last_login = Login.objects.order_by('-si_number').first()
            if last_login and last_login.si_number >= 1819:
                raise ValueError("Maximum SI number of 1819 reached")
            self.si_number = (last_login.si_number + 1) if last_login else 1
        super(Login, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
class Registration(models.Model):
    name = models.CharField(max_length=50)
    phon = models.IntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=150)
    # confirm_password = models.CharField(max_length=150)

    # def set_password(self,raw_password):
    #     self.password = make_password(raw_password)
    #
    # def check_password(self,raw_password):
    #     return check_password(raw_password,self.password)

    def __str__(self):
        return self.name

class Home(models.Model):
    # si_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)



    def __str__(self):
        return self.name

    def add_points_to_ancestors(self,points):
        parent = self.parent
        while parent is not None:
            parent.points += points
            parent.save()
            if parent.points >= 100:
                parent.rebirth()
            parent = parent.parent

    def rebirth(self):
        # Create a new node (rebirth)
        new_user = Home.objects.create(name=f"{self.name}_reborn", points=0, parent=self.parent)

        # Reset the current node's points to 0
        self.points = 0
        self.save()

        return new_user