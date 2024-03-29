# Generated by Django 4.1.5 on 2023-01-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=255)),
                ('img', models.ImageField(upload_to='blogs')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
