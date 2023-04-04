# Generated by Django 4.1.7 on 2023-04-03 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_books_deliveries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('code_author', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('year_of_birth', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('code_publish', models.IntegerField(primary_key=True, serialize=False)),
                ('publish', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('code_book', models.IntegerField(primary_key=True, serialize=False)),
                ('title_book', models.CharField(max_length=40)),
                ('pages', models.IntegerField()),
                ('code_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
                ('code_publish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.publishinghouse')),
            ],
        ),
    ]
