# Generated by Django 3.2.8 on 2021-10-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_relationships', '0003_alter_language_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('frameworks', models.ManyToManyField(to='dj_relationships.Frameworks')),
            ],
        ),
    ]
