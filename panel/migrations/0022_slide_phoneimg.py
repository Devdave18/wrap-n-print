# Generated by Django 4.2.5 on 2024-04-15 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0021_alter_adminpanel_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='phoneimg',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
