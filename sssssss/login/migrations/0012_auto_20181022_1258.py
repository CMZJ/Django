# Generated by Django 2.1.2 on 2018-10-22 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20181022_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='dataTime',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='comment',
            name='userid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dianzan',
            name='number',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='dianzan',
            name='userid',
            field=models.IntegerField(),
        ),
    ]
