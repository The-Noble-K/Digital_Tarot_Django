# Generated by Django 2.2.3 on 2019-07-14 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
