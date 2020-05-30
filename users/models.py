from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.TextField(default='')
	image = models.ImageField(upload_to='profile_pics/')

	def __str__(self):
		return "{}'s profile".format(self.user)



def create_profile(sender, **kwargs):
	user = kwargs['instance']
	if kwargs['created']:
		user_profile = Profile.objects.create(user=user)
		user_profile.save()

post_save.connect(create_profile, sender=User)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{} from {}'.format(self.name, self.email)


class About(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	details = models.TextField(null=True, blank=True)
	website = models.URLField(max_length=200, null=True, blank=True)
	image = models.ImageField(upload_to='about_pics/')

	def __str__(self):
		return self.name 
