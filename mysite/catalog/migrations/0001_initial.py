# Generated by Django 4.0.4 on 2022-06-25 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=20)),
                ('cost', models.TextField(max_length=20)),
            ],
        ),
    ]