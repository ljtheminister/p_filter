from django.db import models

from abc import ABCMeta
# Create your models here.

class Media(models.Model):
    channel = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
    user = models.CharField(max_length=50)
    date_posted = models.DateTimeField('date posted')
    
    class Meta:
	abstract = True

class Tweet(Media):
    retweeted = models.CharField(max_length=20)
    lang_tweet = models.CharField(max_length=20)
    lang_user = models.CharField(max_length=20)
    tz_user = models.CharField(max_length=20)

    class Meta(Media.Meta):
	db_table = 'tweet_db'
    
class Instagram(Media):
    class Meta(Media.Meta):
	db_table = 'instagram_db' 
