# Generated by Django 4.1.7 on 2023-04-03 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id_book', models.IntegerField(primary_key=True, serialize=False)),
                ('book_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Deliveries',
            fields=[
                ('supplier_id', models.IntegerField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=100)),
            ],
        ),
    ]
