# Generated by Django 3.0.5 on 2020-05-24 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('card_id', models.AutoField(primary_key=True, serialize=False)),
                ('card_question', models.CharField(max_length=100000)),
                ('card_answer', models.CharField(max_length=100000)),
                ('card_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_category', to='mooc.Category')),
            ],
        ),
    ]
