# Generated by Django 5.0.6 on 2024-08-29 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_alter_marksheet_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'company',
            },
        ),
    ]
