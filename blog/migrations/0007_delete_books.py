# Generated by Django 4.1.7 on 2023-04-03 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_books_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Books',
        ),
    ]
