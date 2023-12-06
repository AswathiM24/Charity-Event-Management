# Generated by Django 5.0 on 2023-12-06 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_organization_address_organization_fund_raised_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('location', models.TextField()),
                ('org_name', models.CharField(max_length=255)),
                ('org_email', models.EmailField(max_length=254)),
                ('org_phone', models.IntegerField()),
                ('is_booking', models.BooleanField(default=False)),
                ('ticket_price', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]