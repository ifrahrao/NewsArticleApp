# Generated by Django 4.1.6 on 2023-02-09 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsArticles',
            new_name='NewsArticle',
        ),
    ]
