# Generated by Django 2.1 on 2020-06-10 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
    ]
