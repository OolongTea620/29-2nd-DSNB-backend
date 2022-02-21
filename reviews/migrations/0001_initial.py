# Generated by Django 4.0.2 on 2022-02-21 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_user_profile_image'),
        ('books', '0004_book_file_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.CharField(max_length=600)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('is_spoiler', models.BooleanField(default=0)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='books.book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer', to='users.user')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
    ]