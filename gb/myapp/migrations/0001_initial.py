# Generated by Django 5.0.2 on 2024-03-31 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=128)),
                ('date_of_registration', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
                ('date_of_edit', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, default='empty.jpg', null=True, upload_to='item_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_sum', models.IntegerField(default=0)),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_client', to='myapp.client')),
                ('id_item', models.ManyToManyField(related_name='id_item', to='myapp.item')),
            ],
        ),
    ]
