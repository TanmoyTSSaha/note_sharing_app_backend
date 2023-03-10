# Generated by Django 4.1.5 on 2023-02-04 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('imgUrl', models.TextField()),
                ('user_name', models.CharField(max_length=100)),
                ('user_description', models.TextField()),
                ('university_college', models.CharField(max_length=100)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.courses')),
            ],
        ),
    ]
