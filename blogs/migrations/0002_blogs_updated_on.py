# Generated by Django 4.1.5 on 2023-01-07 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
