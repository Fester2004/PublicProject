# Generated by Django 3.0.5 on 2020-04-27 14:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GGuide', '0023_related_name_into_comments_for_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
