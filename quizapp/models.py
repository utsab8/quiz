from django.db import models

# Create your models here.


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract =True


class Quiz(TimeStampModel):

	question = models.CharField(max_length = 500)
	option1 = models.CharField(max_length = 200)
	option2 = models.CharField(max_length = 200)
	option3 = models.CharField(max_length = 200)
	option4 = models.CharField(max_length = 200)
	answer = models.CharField(max_length = 200)    
    