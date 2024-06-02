# Generated by Django 5.0.4 on 2024-05-16 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0004_weeklynews'),
    ]

    operations = [
        migrations.AddField(
            model_name='latestnews',
            name='wfield',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='latestnews',
            name='wimg',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='latestnews',
            name='wnewsdetails',
            field=models.TextField(default='NOTHING', null=True),
        ),
        migrations.AddField(
            model_name='latestnews',
            name='wnewsline',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='latestnews',
            name='field',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='latestnews',
            name='img',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='latestnews',
            name='newsline',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]