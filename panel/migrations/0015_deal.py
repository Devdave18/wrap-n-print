# Generated by Django 4.2.5 on 2024-02-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0014_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('date', models.DateTimeField()),
                ('link', models.CharField(max_length=20)),
            ],
        ),
    ]
