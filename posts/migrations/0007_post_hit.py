# Generated by Django 2.2 on 2022-02-23 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_slider_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
