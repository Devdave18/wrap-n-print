# Generated by Django 4.2.5 on 2024-03-22 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_delete_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
                ('productid', models.CharField(max_length=20)),
                ('productname', models.CharField(max_length=20)),
                ('productimage', models.CharField(max_length=20)),
                ('productprice', models.CharField(max_length=20)),
            ],
        ),
    ]
