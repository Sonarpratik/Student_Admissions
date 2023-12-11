# Generated by Django 4.1.3 on 2023-12-09 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_item_depth_item_specifications_item_width_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='items',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='quotation',
            name='remark',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='quotation',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='specifications',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='specifications',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='special_note',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
