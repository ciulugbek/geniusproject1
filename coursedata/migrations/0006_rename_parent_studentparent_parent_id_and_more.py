# Generated by Django 4.1 on 2022-08-06 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursedata', '0005_rename_parent_id_studentparent_parent_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentparent',
            old_name='parent',
            new_name='parent_id',
        ),
        migrations.RenameField(
            model_name='studentparent',
            old_name='student',
            new_name='student_id',
        ),
    ]
