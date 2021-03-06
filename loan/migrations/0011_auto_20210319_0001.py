# Generated by Django 3.1.7 on 2021-03-19 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loan', '0010_auto_20210318_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='username',
            field=models.ForeignKey(null='blank', on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='loan',
            name='frequency',
            field=models.IntegerField(blank=True, default=23),
        ),
    ]
