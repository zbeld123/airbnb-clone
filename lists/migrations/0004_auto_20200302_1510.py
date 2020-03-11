# Generated by Django 2.2.5 on 2020-03-02 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20200302_1413'),
        ('lists', '0003_auto_20200302_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='room',
        ),
        migrations.AddField(
            model_name='list',
            name='rooms',
            field=models.ManyToManyField(blank=True, related_name='lists', to='rooms.Room'),
        ),
    ]