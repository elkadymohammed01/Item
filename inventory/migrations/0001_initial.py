# Generated by Django 3.2.16 on 2023-01-28 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='الإسم')),
            ],
            options={
                'verbose_name': 'المخزن',
                'verbose_name_plural': 'المخازن',
            },
        ),
        migrations.CreateModel(
            name='InventoryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='الإسم')),
            ],
            options={
                'verbose_name': 'المخزن',
                'verbose_name_plural': 'المخازن',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='الإسم')),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='inventory.inventory')),
            ],
            options={
                'verbose_name': 'المخزن',
                'verbose_name_plural': 'المخازن',
            },
        ),
        migrations.AddField(
            model_name='inventory',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='inventory.inventorytype'),
        ),
    ]