# Generated by Django 4.2.5 on 2024-01-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='dfsfa', upload_to='pics'),
            preserve_default=False,
        ),
    ]
