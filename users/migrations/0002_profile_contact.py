# Generated by Django 3.2.5 on 2021-08-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact',
            field=models.CharField(default='07xxxxxxxx', max_length=20),
        ),
    ]
