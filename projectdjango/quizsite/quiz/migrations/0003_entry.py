# Generated by Django 5.0.6 on 2024-08-10 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_cock'),
    ]

    operations = [
        migrations.CreateModel(
            name='entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booltitle', models.CharField(max_length=100)),
                ('authorname', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'entry',
            },
        ),
    ]
