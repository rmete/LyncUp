# Generated by Django 2.2.10 on 2020-03-08 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LyncUp', '0003_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='group_pics'),
        ),
    ]
