# Generated by Django 3.2.3 on 2021-06-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='books',
            field=models.ManyToManyField(blank=True, null=True, to='books.Books'),
        ),
        migrations.AlterField(
            model_name='user',
            name='no_of_books_taken',
            field=models.IntegerField(default=0),
        ),
    ]
