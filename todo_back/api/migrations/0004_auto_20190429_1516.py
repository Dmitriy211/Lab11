# Generated by Django 2.2 on 2019-04-29 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190429_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tasklist',
            new_name='task_list',
        ),
    ]
