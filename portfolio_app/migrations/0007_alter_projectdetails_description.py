# Generated by Django 4.2.15 on 2024-09-05 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_alter_projectdetails_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetails',
            name='description',
            field=models.TextField(),
        ),
    ]
