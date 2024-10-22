# Generated by Django 5.1.1 on 2024-10-11 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0003_book_publish_alter_book_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publish',
        ),
        migrations.AddField(
            model_name='book',
            name='publish_date',
            field=models.DateField(null=True, verbose_name='publish_date'),
        ),
    ]
