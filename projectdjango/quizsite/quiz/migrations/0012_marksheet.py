# Generated by Django 5.0.6 on 2024-08-28 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_alter_form_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marksheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'result',
            },
        ),
    ]
