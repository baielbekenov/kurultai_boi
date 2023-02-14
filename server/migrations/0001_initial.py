# Generated by Django 4.1.2 on 2023-02-14 19:24

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('birth_of_place', models.CharField(blank=True, max_length=50, null=True, verbose_name='Место рождения')),
                ('birth_of_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('living_place', models.CharField(blank=True, max_length=80, null=True, verbose_name='Место проживания')),
                ('nation', models.CharField(blank=True, max_length=30, null=True, verbose_name='Нация')),
                ('occupation', models.CharField(blank=True, max_length=50, null=True, verbose_name='Профессия')),
                ('phone_number', models.IntegerField(blank=True, null=True, verbose_name='Номер телефона')),
                ('is_tor_aga', models.BooleanField(default=False, verbose_name='Тор Ага')),
                ('is_zam', models.BooleanField(default=False, verbose_name='Заместитель Тор Ага')),
                ('is_katchy', models.BooleanField(default=False, verbose_name='Катчы')),
                ('is_delegat', models.BooleanField(default=False, verbose_name='Делегат')),
                ('image', models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Аватар')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'ordering': ['first_name'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='.', max_length=123, verbose_name='Название')),
                ('description', models.TextField(blank=True, default='.')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/avatars/%Y/%m/%d/', verbose_name='Изображение')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('is_privat', models.BooleanField(blank=True, default=False)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('users', models.ManyToManyField(related_name='chats_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'Чаты',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rubrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24, verbose_name='Название рубрики')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
                ('content', models.TextField()),
                ('chat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='voting_chat', to='server.chat')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='questionmessage/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user_questions', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user_questions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Вопрос от товарища',
                'verbose_name_plural': 'Вопросы от людей',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('users', models.ManyToManyField(blank=True, null=True, related_name='users_votes', to=settings.AUTH_USER_MODEL)),
                ('voting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions_vote', to='server.voting')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('rubric_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.rubrics', verbose_name='Рубрика')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
                ('title_en', models.CharField(max_length=123, null=True)),
                ('title_ru', models.CharField(max_length=123, null=True)),
                ('title_ky', models.CharField(max_length=123, null=True)),
                ('preview', models.CharField(max_length=244)),
                ('preview_en', models.CharField(max_length=244, null=True)),
                ('preview_ru', models.CharField(max_length=244, null=True)),
                ('preview_ky', models.CharField(max_length=244, null=True)),
                ('content', models.TextField()),
                ('content_en', models.TextField(null=True)),
                ('content_ru', models.TextField(null=True)),
                ('content_ky', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='news/')),
                ('rubric', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.rubrics')),
                ('voting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='server.voting')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Сообщение')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.chat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщении',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False, verbose_name='Active')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='server.news')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.AddField(
            model_name='account',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.region'),
        ),
        migrations.AddField(
            model_name='account',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
