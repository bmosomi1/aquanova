# Generated by Django 3.1.5 on 2021-10-08 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0025_watersystemconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterConfigtAll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=250)),
                ('msisdn', models.CharField(max_length=250)),
                ('client_number', models.CharField(max_length=250)),
                ('id_num', models.CharField(max_length=250, null=True)),
                ('meter_num', models.CharField(max_length=250, null=True)),
                ('customer_rate', models.CharField(max_length=250, null=True)),
                ('connection_fee', models.CharField(max_length=250, null=True)),
                ('last_meter_reading_date', models.CharField(max_length=250, null=True)),
                ('email_address', models.EmailField(max_length=250, null=True)),
                ('court', models.CharField(max_length=250, null=True)),
                ('network', models.CharField(max_length=250, null=True)),
                ('last_meter_reading', models.FloatField(default=0, max_length=250, null=True)),
                ('amount_due', models.FloatField(default=0, max_length=250, null=True)),
                ('units_consumed', models.FloatField(default=0, max_length=250, null=True)),
                ('last_payment_date', models.CharField(max_length=250, null=True)),
                ('meter_change_date', models.CharField(max_length=250, null=True)),
                ('connection_fee_paid', models.FloatField(default=0, max_length=250, null=True)),
                ('message', models.IntegerField(default=0, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Water',
                'verbose_name_plural': 'Waters',
            },
        ),
        migrations.CreateModel(
            name='WaterSysConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=250)),
                ('msisdn', models.CharField(max_length=250)),
                ('readings', models.FloatField(default=0, max_length=250, null=True)),
                ('account_number', models.CharField(max_length=250)),
                ('processed', models.IntegerField(max_length=250, null=True)),
                ('reading_type', models.CharField(max_length=250, null=True)),
                ('read_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'water_sys_config',
                'verbose_name_plural': 'water_sys_config',
            },
        ),
        migrations.AddField(
            model_name='watersystemconfig',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sms.customer'),
        ),
    ]
