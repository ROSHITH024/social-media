# Generated by Django 4.1.4 on 2023-01-04 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_user_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follower',
            name='followers',
        ),
        migrations.AddField(
            model_name='follower',
            name='followers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
