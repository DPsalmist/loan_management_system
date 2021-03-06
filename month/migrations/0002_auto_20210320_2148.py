# Generated by Django 3.1.7 on 2021-03-20 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0027_auto_20210320_2129'),
        ('month', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month1',
            name='loan_month1',
            field=models.ForeignKey(default='month 1', null='blank', on_delete=django.db.models.deletion.CASCADE, to='loan.loan'),
        ),
        migrations.AlterField(
            model_name='month2',
            name='loan_month2',
            field=models.ForeignKey(default='month 2', null='blank', on_delete=django.db.models.deletion.CASCADE, to='loan.loan'),
        ),
        migrations.AlterField(
            model_name='month3',
            name='loan_month3',
            field=models.ForeignKey(default='month 3', null='blank', on_delete=django.db.models.deletion.CASCADE, to='loan.loan'),
        ),
        migrations.AlterField(
            model_name='month4',
            name='loan_month4',
            field=models.ForeignKey(default='month 4', null='blank', on_delete=django.db.models.deletion.CASCADE, to='loan.loan'),
        ),
        migrations.AlterField(
            model_name='month5',
            name='loan_month5',
            field=models.ForeignKey(default='month 5', null='blank', on_delete=django.db.models.deletion.CASCADE, to='loan.loan'),
        ),
        migrations.AlterField(
            model_name='month6',
            name='loan_month6',
            field=models.ForeignKey(default='month 6', null='blank', on_delete=django.db.models.deletion.CASCADE, to='loan.loan'),
        ),
        migrations.CreateModel(
            name='Month7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('loan_month7', models.ForeignKey(default='month 7', null='blank', on_delete=django.db.models.deletion.CASCADE, to='loan.loan')),
            ],
        ),
    ]
