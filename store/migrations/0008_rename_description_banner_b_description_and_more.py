# Generated by Django 4.1.4 on 2023-04-25 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_banner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='description',
            new_name='b_description',
        ),
        migrations.RenameField(
            model_name='banner',
            old_name='images',
            new_name='b_images',
        ),
        migrations.RenameField(
            model_name='banner',
            old_name='product_name',
            new_name='banner_name',
        ),
    ]