# Generated by Django 2.2.4 on 2019-08-09 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapi', '0004_auto_20190807_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertasks',
            name='state',
            field=models.CharField(choices=[('TO_DO', 'To do'), ('DONE', 'Done')], max_length=300),
        ),
    ]