# Generated by Django 3.2.4 on 2021-06-11 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_react_ai_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='react',
            name='img_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
