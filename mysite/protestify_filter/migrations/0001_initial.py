# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=50)),
                ('date_posted', models.DateTimeField(verbose_name='date posted')),
                ('retweeted', models.CharField(max_length=20)),
                ('lang_tweet', models.CharField(max_length=20)),
                ('lang_user', models.CharField(max_length=20)),
                ('tz_user', models.CharField(max_length=20)),
            ],
            options={
                u'abstract': False,
                u'db_table': 'tweet_db',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instagram',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=50)),
                ('date_posted', models.DateTimeField(verbose_name='date posted')),
            ],
            options={
                u'abstract': False,
                u'db_table': 'instagram_db',
            },
            bases=(models.Model,),
        ),
    ]
