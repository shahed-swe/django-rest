# Generated by Django 3.1.1 on 2020-10-03 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookSelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('description', models.TextField(blank=True, default='', max_length=500, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('publication_name', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('published_data_time', models.DateTimeField(auto_now=True, null=True)),
                ('cover', models.FileField(default='', upload_to='cover/')),
            ],
            options={
                'db_table': 'book_table',
            },
        ),
    ]
