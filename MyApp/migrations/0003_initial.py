# Generated by Django 4.1.6 on 2023-03-23 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MyApp', '0002_delete_userinput'),
    ]

    operations = [
        migrations.CreateModel(
            name='userinput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retailer', models.CharField(max_length=45)),
                ('region', models.CharField(max_length=45)),
                ('state', models.CharField(max_length=45)),
                ('city', models.CharField(max_length=45)),
                ('product', models.CharField(max_length=45)),
                ('method', models.CharField(max_length=45)),
            ],
        ),
    ]
