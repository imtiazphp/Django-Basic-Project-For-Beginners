# Generated by Django 5.0.7 on 2024-08-07 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
