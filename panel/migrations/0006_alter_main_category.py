# Generated by Django 4.2.5 on 2024-02-17 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_gifting_category_gifting_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='category',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
