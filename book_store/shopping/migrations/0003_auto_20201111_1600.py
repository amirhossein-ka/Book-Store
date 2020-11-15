# Generated by Django 3.1.2 on 2020-11-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_remove_product_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='profile_image',
            new_name='product_image',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, help_text='product description', null=True),
        ),
    ]
