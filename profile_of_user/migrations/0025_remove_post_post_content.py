# Generated by Django 4.1.1 on 2023-05-30 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "profile_of_user",
            "0024_remove_post_post_case_remove_post_post_location_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="post_content",),
    ]
