# Generated by Django 5.0 on 2023-12-06 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_events_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.CharField(max_length=1000)),
                ('is_active', models.BooleanField(default=True)),
                ('action', models.CharField(blank=True, max_length=1000)),
                ('open_date', models.DateField()),
                ('closed_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
