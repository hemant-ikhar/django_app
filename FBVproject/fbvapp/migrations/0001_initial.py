# Generated by Django 3.1.1 on 2021-04-04 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('duration', models.FloatField()),
            ],
        ),
    ]
