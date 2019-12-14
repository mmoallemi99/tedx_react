# Generated by Django 2.2.8 on 2019-12-14 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20191214_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='account_status',
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='email',
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='speaker',
            name='instagram_account',
            field=models.CharField(blank=True, help_text='instagram.com/[User_Account]', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='speaker',
            name='linkedin_account',
            field=models.CharField(blank=True, help_text='linkedin.com/in/[User_Account]', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='speaker',
            name='topic',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
