# Generated by Django 3.0.7 on 2020-08-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200728_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sex',
            field=models.CharField(choices=[('men', 'Men'), ('women', 'Women')], default='men', max_length=30),
        ),
    ]