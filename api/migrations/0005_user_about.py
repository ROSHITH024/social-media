# Generated by Django 4.1.4 on 2023-01-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.CharField(max_length=250, null=True),
        ),
    ]