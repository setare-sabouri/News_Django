# Generated by Django 4.0.1 on 2022-02-02 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_news_delete_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]