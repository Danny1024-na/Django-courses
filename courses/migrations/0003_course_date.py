# Generated by Django 4.1.4 on 2022-12-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date',
            field=models.DateField(default=''),
            preserve_default=False,
        ),
    ]
