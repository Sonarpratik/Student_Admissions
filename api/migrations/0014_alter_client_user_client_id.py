# Generated by Django 4.1.3 on 2023-07-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_item_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='user_client_id',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
