# Generated by Django 5.1.1 on 2024-09-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JioProduct',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('mrp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount_pct', models.FloatField(blank=True, null=True)),
                ('availability_status', models.CharField(blank=True, max_length=50, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
