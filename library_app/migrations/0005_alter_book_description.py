# Generated by Django 5.1.1 on 2024-10-16 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0004_remove_book_publish_book_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=500, verbose_name='description'),
        ),
    ]
