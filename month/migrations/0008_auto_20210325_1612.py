# Generated by Django 3.1.4 on 2021-03-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('month', '0007_auto_20210324_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='month1',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Transfer', 'Transfer'), ('Other', 'Other')], default='Cash', max_length=30),
        ),
        migrations.AddField(
            model_name='month2',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Transfer', 'Transfer'), ('Other', 'Other')], default='Cash', max_length=30),
        ),
        migrations.AddField(
            model_name='month3',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Transfer', 'Transfer'), ('Other', 'Other')], default='Cash', max_length=30),
        ),
        migrations.AddField(
            model_name='month4',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Transfer', 'Transfer'), ('Other', 'Other')], default='Cash', max_length=30),
        ),
        migrations.AddField(
            model_name='month5',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Transfer', 'Transfer'), ('Other', 'Other')], default='Cash', max_length=30),
        ),
        migrations.AddField(
            model_name='month6',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Transfer', 'Transfer'), ('Other', 'Other')], default='Cash', max_length=30),
        ),
        migrations.AddField(
            model_name='month7',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Transfer', 'Transfer'), ('Other', 'Other')], default='Cash', max_length=30),
        ),
    ]
