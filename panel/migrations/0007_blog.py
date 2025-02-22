# Generated by Django 4.2.5 on 2024-02-18 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0006_alter_main_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('img1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('discription1', models.CharField(max_length=20)),
                ('discription2', models.CharField(max_length=20)),
                ('discription3', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('author', models.CharField(max_length=20)),
            ],
        ),
    ]
