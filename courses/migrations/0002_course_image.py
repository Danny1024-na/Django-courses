# Generated by Django 4.1.4 on 2022-12-28 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='default.png', upload_to='Media/'),
        ),
    ]
