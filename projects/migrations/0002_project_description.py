# Generated by Django 4.2.2 on 2023-06-08 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default='sdsds'),
            preserve_default=False,
        ),
    ]
