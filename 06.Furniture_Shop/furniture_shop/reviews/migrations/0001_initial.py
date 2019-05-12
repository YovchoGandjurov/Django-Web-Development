# Generated by Django 2.2.1 on 2019-05-11 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('furniture', '0002_auto_20190511_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('score', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
                ('furniture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='furniture.Furniture')),
            ],
        ),
    ]