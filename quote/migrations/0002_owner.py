# Generated by Django 3.2.21 on 2023-11-28 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]