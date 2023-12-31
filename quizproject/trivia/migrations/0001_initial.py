# Generated by Django 3.2.8 on 2023-10-19 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TriviaQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.PositiveIntegerField(unique=True)),
                ('question_text', models.TextField()),
                ('answer_text', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Вопрос викторины',
                'verbose_name_plural': 'Вопросы викторины',
            },
        ),
    ]
