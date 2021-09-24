# Generated by Django 3.2.7 on 2021-09-23 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='tag_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='notes.tag'),
        ),
    ]
