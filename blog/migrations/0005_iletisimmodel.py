# Generated by Django 3.1.7 on 2021-03-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_yorummodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='IletisimModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('isim_soyisim', models.CharField(max_length=200)),
                ('mesaj', models.TextField()),
                ('gonderim_tarihi', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'İletişim',
                'verbose_name_plural': 'İletişim',
                'db_table': 'iletisim',
            },
        ),
    ]
