# Generated by Django 3.2.16 on 2023-02-03 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='desc',
            new_name='description',
        ),
    ]
