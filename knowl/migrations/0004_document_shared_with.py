# Generated by Django 4.2.8 on 2023-12-09 12:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('knowl', '0003_document_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='shared_with',
            field=models.ManyToManyField(blank=True, related_name='shared_files', to=settings.AUTH_USER_MODEL),
        ),
    ]
