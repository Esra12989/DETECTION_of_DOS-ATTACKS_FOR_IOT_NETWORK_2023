# Generated by Django 4.1.1 on 2023-05-07 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profile_of_user", "0020_auto_20210621_1159"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="post_price",
            field=models.CharField(default=int, max_length=5000),
            preserve_default=False,
        ),
    ]
