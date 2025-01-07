# Generated by Django 5.1.1 on 2024-09-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneapp', '0005_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('image', models.ImageField(default='phone_images/default_image.jpg', upload_to='phone_images/')),
                ('description', models.TextField(default='Açıklama mevcut değil.')),
            ],
        ),
    ]
