# Generated by Django 5.1.1 on 2024-09-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneapp', '0008_earphones_tablet'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewRealeses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newrealeses_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('image', models.ImageField(default='newrealeses_images/default_image.jpg', upload_to='newrealeses_images/')),
                ('description', models.TextField(default='Açıklama mevcut değil')),
            ],
        ),
        migrations.AlterField(
            model_name='earphones',
            name='description',
            field=models.TextField(default='Açıklama mevcut değil'),
        ),
    ]