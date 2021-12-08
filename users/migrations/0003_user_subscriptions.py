# Generated by Django 3.2.9 on 2021-12-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_alter_product_id'),
        ('users', '0002_user_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subscriptions',
            field=models.ManyToManyField(related_name='users', to='billing.Product'),
        ),
    ]