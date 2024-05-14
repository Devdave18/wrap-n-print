# Generated by Django 4.2.5 on 2024-02-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('number', models.CharField(blank=True, max_length=15, null=True)),
                ('category', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=20)),
            ],
        ),
    ]
