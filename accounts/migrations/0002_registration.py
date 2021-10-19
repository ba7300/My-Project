# Generated by Django 3.1.5 on 2021-10-18 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('pan_number', models.CharField(max_length=10)),
                ('gst_number', models.CharField(max_length=15)),
                ('register_number', models.CharField(max_length=50)),
                ('licence_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('state_name', models.CharField(max_length=50)),
                ('branch_name', models.CharField(max_length=50)),
                ('person_name', models.CharField(max_length=50)),
                ('contact_number1', models.IntegerField()),
                ('email1', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
                ('contact_number2', models.IntegerField()),
                ('location', models.TextField()),
                ('postal_code', models.IntegerField()),
                ('password', models.CharField(max_length=125)),
            ],
        ),
    ]