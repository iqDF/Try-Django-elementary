# Generated by Django 2.0.7 on 2019-01-07 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='PRODUCT')),
                ('description', models.TextField()),
                ('price', models.TextField()),
                ('summary', models.TextField(default='This is cool!')),
            ],
        ),
    ]
