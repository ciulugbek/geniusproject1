# Generated by Django 4.1 on 2022-08-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursedata', '0010_studentgroup_studentgroup_student_group_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_email',
            field=models.EmailField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='student_photo',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]