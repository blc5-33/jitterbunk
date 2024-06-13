from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=256)
    photo = models.CharField(max_length=1024)

    def __str__(self):
        return self.username

class Bunk(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bunks_from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bunks_to_user')
    pub_date = models.DateTimeField("Time")

    def __str__(self):
        return self.from_user.username + " to " + self.to_user.username + " | Created at " + str(self.pub_date)

    @classmethod
    def create(cls, nfrom_user, nto_user, npub_date):
        new_bunk = cls(from_user=nfrom_user, to_user=nto_user, pub_date=npub_date)
        return new_bunk