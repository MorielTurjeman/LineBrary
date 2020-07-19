# Generated by Django 3.0.3 on 2020-07-18 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Books', '0013_auto_20200718_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='Books/Images/'),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN13', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contributions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.IntegerField()),
                ('condition', models.CharField(choices=[('Like New', 'Like New'), ('Used', 'Used'), ('Collectible', 'Collectible')], default='LikeNew', max_length=20)),
                ('ISBN13', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]