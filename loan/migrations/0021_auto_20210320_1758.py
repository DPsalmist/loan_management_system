# Generated by Django 3.1.7 on 2021-03-20 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0020_auto_20210320_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='interest_rate',
            field=models.CharField(default=0.1, max_length=10),
        ),
    ]