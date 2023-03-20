# Generated by Django 2.2.4 on 2020-12-08 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0033_auto_20201203_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='StAnnPatients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=250)),
                ('processed', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Group')),
            ],
        ),
    ]
