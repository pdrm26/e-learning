# Generated by Django 5.0.9 on 2024-11-29 12:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0004_alter_content_options_alter_module_options_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="students",
            field=models.ManyToManyField(
                blank=True, related_name="courses_joined", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
