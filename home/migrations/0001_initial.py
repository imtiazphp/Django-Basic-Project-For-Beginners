# Generated by Django 5.0.7 on 2024-08-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=192)),
                ('phone', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=192)),
                ('message', models.TextField()),
                ('create_at', models.DateField()),
            ],
        ),
    ]
