# Generated by Django 2.0.4 on 2018-04-18 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('university_name', models.CharField(default='', max_length=200)),
                ('university_address', models.CharField(max_length=200)),
                ('food_quality', models.CharField(choices=[('1', 'bad'), ('2', 'bearable'), ('3', 'meidum'), ('4', 'good'), ('5', 'select')], default='5', max_length=20)),
                ('further_comments', models.TextField()),
            ],
        ),
    ]
