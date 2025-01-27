# Generated by Django 4.2.17 on 2025-01-22 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('picture', models.URLField(default='https://cwdaust.com.au/wpress/wp-content/uploads/2015/04/placeholder-restaurant.png', max_length=1000)),
                ('cuisine', models.CharField(max_length=200)),
                ('rating', models.FloatField()),
            ],
        ),
    ]
