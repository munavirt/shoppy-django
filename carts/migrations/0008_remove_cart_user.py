# Generated by Django 4.1.4 on 2023-05-07 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0007_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]
