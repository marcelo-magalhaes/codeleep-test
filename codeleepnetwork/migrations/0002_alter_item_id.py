# Generated by Django 5.1.4 on 2024-12-16 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeleepnetwork', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
