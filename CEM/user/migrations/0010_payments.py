# Generated by Django 5.0 on 2023-12-06 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_tickets_action'),
    ]

    operations = [
        migrations.CreateModel(
            name='payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('merchant_key', models.CharField(max_length=255)),
            ],
        ),
    ]
