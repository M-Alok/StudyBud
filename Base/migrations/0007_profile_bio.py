# Generated by Django 5.1.4 on 2025-03-09 08:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Base", "0006_alter_profile_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
    ]
