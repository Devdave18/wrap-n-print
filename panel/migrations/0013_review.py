# Generated by Django 4.2.5 on 2024-02-22 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0012_main_sub_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
