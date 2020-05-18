# Generated by Django 2.2 on 2020-04-20 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200409_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigcategory',
            name='keywords',
            field=models.TextField(default='IT,技术,博客,Python', help_text='用来作为SEO中keywords,长度参考SEO标准', max_length=240, verbose_name='关键字'),
        ),
    ]
