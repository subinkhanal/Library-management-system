# Generated by Django 3.2 on 2021-05-15 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210513_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='quantity',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='forginkey',
        ),
    ]