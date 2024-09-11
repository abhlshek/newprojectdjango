# Generated by Django 5.0.6 on 2024-08-26 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_admission_phonebook_rename_booltitle_entry_booktitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'bankbook',
            },
        ),
    ]
