# Generated by Django 3.2.5 on 2021-08-15 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ewaste', '0002_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='desktops',
            name='category',
        ),
        migrations.RemoveField(
            model_name='laptops',
            name='category',
        ),
        migrations.RemoveField(
            model_name='others',
            name='category',
        ),
        migrations.RemoveField(
            model_name='phones',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
