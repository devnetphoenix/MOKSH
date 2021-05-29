# Generated by Django 3.1.6 on 2021-05-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=20, null=True)),
                ('age', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('pincode', models.CharField(max_length=20, null=True)),
                ('gender', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=20, null=True)),
                ('phone', models.IntegerField()),
                ('status', models.BooleanField(verbose_name=0)),
            ],
        ),
    ]