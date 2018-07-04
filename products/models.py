from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
	title = models.CharField(max_length=120)
	pub_date = models.DateTimeField()
	url = models.TextField()
	body = models.TextField()
	thumbnail = models.ImageField(upload_to='images/')
	image = models.ImageField(upload_to='images/')
	votes_total = models.IntegerField(default = 0)
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:60]

	def pub_date_good(self):
			return self.pub_date.strftime('%b %e %Y')