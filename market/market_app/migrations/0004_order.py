# Generated by Django 4.1.5 on 2023-03-04 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market_app', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=40)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market_app.product')),
            ],
        ),
    ]
