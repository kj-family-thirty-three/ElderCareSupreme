# Generated by Django 3.0.8 on 2020-07-07 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20200707_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='message_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
