# Generated by Django 3.2.16 on 2022-12-10 08:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(default='', max_length=30)),
                ('uuid_name', models.UUIDField(default=uuid.UUID('e306d9a1-1ba6-4a91-9005-7bd9296607fb'))),
                ('size', models.PositiveIntegerField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
