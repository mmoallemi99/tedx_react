# Generated by Django 2.2.3 on 2019-12-08 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20191206_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='role',
            field=models.CharField(blank=True, choices=[('Curation', 'Curation'), ('Organizer', 'Organizer'), ('Co Organizer', 'Co Organizer'), ('Marketing', 'Marketing'), ('Documentation', 'Documentation'), ('Creativity', 'Creativity'), ('Frontend Developer', 'Frontend Developer'), ('Backend Developer', 'Backend Developer'), ('UI Designer', 'UI Designer'), ('Graphic Designer', 'Graphic Designer')], default='others', help_text="team's way of association in team", max_length=30, null=True),
        ),
    ]
