# Generated by Django 4.1 on 2022-08-05 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursedata', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_fio', models.CharField(max_length=150)),
                ('parent_active', models.BooleanField(default=True)),
                ('parent_phone', models.CharField(max_length=60)),
            ],
        ),
    ]
