# Generated by Django 3.2 on 2021-04-27 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_alter_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='commenter',
        ),
    ]
