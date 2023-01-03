# Generated by Django 3.2.16 on 2023-01-02 05:32

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=mdeditor.fields.MDTextField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='preview',
            field=models.TextField(default='', max_length=120),
        ),
    ]