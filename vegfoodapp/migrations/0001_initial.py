# Generated by Django 4.1.3 on 2022-12-17 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetailes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('confirm_password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
