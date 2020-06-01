# Generated by Django 3.0.5 on 2020-05-06 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('item_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('current_level', models.IntegerField(default=0)),
                ('target_level', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
                ('refillNeeded', models.BooleanField(default=False)),
                ('isOrdered', models.BooleanField(default=False))
                
            ],
        ),
    ]