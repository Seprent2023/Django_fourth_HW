# Generated by Django 4.2.4 on 2023-08-04 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPortal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='to_many_category',
            field=models.ManyToManyField(related_name='n', through='NewsPortal.PostCategory', to='NewsPortal.category'),
        ),
    ]
