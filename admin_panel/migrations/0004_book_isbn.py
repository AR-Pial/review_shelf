# Generated by Django 5.1.4 on 2025-01-08 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0003_author_created_at_author_updated_at_book_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
