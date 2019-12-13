# Generated by Django 3.0 on 2019-12-10 22:20

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20191208_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('career', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('study', models.CharField(max_length=100)),
                ('start', models.SmallIntegerField()),
                ('end', models.SmallIntegerField()),
                ('before_tedxes', models.TextField(max_length=400)),
                ('what_made_you', models.TextField(max_length=400)),
                ('how_familiar', models.TextField(max_length=400)),
                ('expects', models.TextField(max_length=400)),
            ],
        ),
    ]