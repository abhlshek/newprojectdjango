# Generated by Django 5.0.6 on 2024-08-27 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_alter_bankbook_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='collage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('cla', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'collage',
            },
        ),
        migrations.DeleteModel(
            name='BankBook',
        ),
    ]
