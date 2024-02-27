# Generated by Django 5.0.2 on 2024-02-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options_alter_customer_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
        migrations.AddField(
            model_name='products',
            name='image_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]