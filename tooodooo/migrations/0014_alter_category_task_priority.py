# Generated by Django 4.2.6 on 2023-11-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tooodooo', '0013_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category_task',
            name='priority',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=1, help_text='Select a priority level from 1 to 10.'),
        ),
    ]
