# Generated by Django 5.0.7 on 2024-09-14 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_counted_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='truncated_content',
            field=models.TextField(null=True),
        ),
    ]
