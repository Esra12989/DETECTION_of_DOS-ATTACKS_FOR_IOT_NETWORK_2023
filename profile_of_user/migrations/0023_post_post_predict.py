# Generated by Django 4.1.1 on 2023-05-08 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profile_of_user", "0022_post_post_case_post_post_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="post_predict",
            field=models.CharField(default={}, max_length=5000),
            preserve_default=False,
        ),
    ]
