# Generated by Django 4.1.7 on 2023-06-09 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_subcategory_remove_category_parent_category_s1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ana_kategori', to='main.category'),
        ),
    ]
