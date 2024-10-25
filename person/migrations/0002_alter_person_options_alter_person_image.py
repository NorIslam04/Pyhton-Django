# Generated by Django 5.1.1 on 2024-10-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['first_name'], 'verbose_name_plural': 'People'},
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(upload_to='photos/%Y/%m/%d'),
        ),
    ]