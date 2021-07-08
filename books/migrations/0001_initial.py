# Generated by Django 3.2.3 on 2021-06-20 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='enter book name', max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('is_available', models.BooleanField(default=True)),
                ('pub_date', models.DateField()),
                ('pic', models.ImageField(blank=True, null=True, upload_to='book_pic')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('document', models.FileField(blank=True, null=True, upload_to='book_doc')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('mobile', models.IntegerField()),
                ('no_of_books_taken', models.IntegerField()),
                ('books', models.ManyToManyField(to='books.Books')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.genre'),
        ),
    ]