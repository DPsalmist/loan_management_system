# Generated by Django 3.1.7 on 2021-03-19 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0012_auto_20210319_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='group',
            field=models.ForeignKey(null='blank', on_delete=django.db.models.deletion.CASCADE, to='loan.group'),
            preserve_default='blank',
        ),
    ]
