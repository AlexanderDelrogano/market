# Generated by Django 4.1.5 on 2023-02-11 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_app', '0002_category_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/noimage.jpg', upload_to='images/'),
        ),
    ]
