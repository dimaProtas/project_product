# Generated by Django 4.2.7 on 2023-11-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChapterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='productmodel',
            name='chapter',
            field=models.ManyToManyField(to='product.chaptermodel'),
        ),
    ]
