# Generated by Django 3.2.7 on 2021-09-27 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('tags', '0005_auto_20210927_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taggeditem',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.contenttype'),
        ),
    ]
