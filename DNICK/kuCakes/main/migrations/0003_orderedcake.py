# Generated by Django 3.2.18 on 2023-08-27 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_cake_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedCake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='cakeimages/')),
                ('price', models.IntegerField(default=0)),
                ('url', models.URLField(blank=True, null=True)),
                ('occasion', models.CharField(max_length=255)),
                ('servingSize', models.CharField(max_length=255)),
                ('flavor', models.CharField(max_length=255)),
                ('toppings', models.CharField(max_length=255)),
                ('cardMessage', models.CharField(max_length=255)),
            ],
        ),
    ]
