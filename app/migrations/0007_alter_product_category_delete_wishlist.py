# Generated by Django 5.1.4 on 2024-12-16 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_wishlist_delete_wishlistitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Ho', 'Hoodies'), ('La', 'Laptop'), ('Sh', 'Shoes'), ('Wa', 'Watches'), ('El', 'Electronics'), ('Su', 'Sunglasses'), ('Ac', 'Accessories')], max_length=5),
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
