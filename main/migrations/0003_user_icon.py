# Generated by Django 4.1.5 on 2023-03-12 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_talk'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]