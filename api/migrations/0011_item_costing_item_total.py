# Generated by Django 4.1.3 on 2023-07-11 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_items_item_id_item_item_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='costing',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
