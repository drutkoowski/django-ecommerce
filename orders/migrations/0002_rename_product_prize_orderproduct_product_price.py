# Generated by Django 4.0.4 on 2022-05-16 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='product_prize',
            new_name='product_price',
        ),
    ]
