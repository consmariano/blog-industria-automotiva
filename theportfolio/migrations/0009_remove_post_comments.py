# Generated by Django 4.2.7 on 2023-11-19 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theportfolio', '0008_comment_post_alter_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
    ]
