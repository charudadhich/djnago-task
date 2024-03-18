# Generated by Django 5.0.3 on 2024-03-11 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('message', models.TextField()),
            ],
            options={
                'db_table': 'base',
            },
        ),
    ]
