# Generated by Django 4.1.5 on 2023-02-11 12:45

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_product_slug'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('db', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(error_messages={'null': 'please fill the input', 'unique': 'No Duplicates.'}, help_text='Please enter a unique value.', max_length=150, unique=True),
        ),
    ]
