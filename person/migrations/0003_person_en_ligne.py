# Generated by Django 5.1.1 on 2024-10-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_alter_person_options_alter_person_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='en_ligne',
            field=models.BooleanField(default=False),
        ),
    ]
