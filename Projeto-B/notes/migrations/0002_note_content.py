# Generated by Django 3.2.7 on 2021-09-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
