# Generated by Django 4.2.7 on 2023-11-21 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameverse', '0002_alter_catogery_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gameverse.product'),
            preserve_default=False,
        ),
    ]
