# Generated by Django 2.0.5 on 2018-06-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kandleapp', '0003_auto_20180529_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='finishVote',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='startVote',
            field=models.DateField(),
        ),
    ]