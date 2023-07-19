# Generated by Django 4.2.3 on 2023-07-19 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='enter city name', max_length=40, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(blank=True, help_text='enter class name ', null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Committment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruiters', models.CharField(blank=True, help_text='enter recruiters names ', max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text=' enter position field', max_length=40, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='enter offer name  ', max_length=250, null=True)),
                ('url', models.URLField(blank=True, help_text='enter offer logo url ', max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='enter state name', max_length=40, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(blank=True, help_text='enter player image url ', max_length=300, null=True)),
                ('full_name', models.CharField(help_text='enter player full name ', max_length=150)),
                ('height', models.CharField(blank=True, help_text='enter player height ', max_length=30, null=True)),
                ('weight', models.IntegerField(blank=True, help_text='enter player weight ', null=True)),
                ('city', models.ForeignKey(help_text='foreign key with player city ', null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.city')),
                ('clas', models.ForeignKey(help_text='foreign key with player class ', null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.class')),
                ('commitment', models.ForeignKey(help_text='foreign key with commitment', null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.committment')),
                ('position', models.ForeignKey(help_text='foreign key with player position ', null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.position')),
                ('school', models.ForeignKey(help_text='foreign key with school', null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.school')),
                ('state', models.ForeignKey(help_text='foreign key with player state ', null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.state')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(help_text='foreign key with player', null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.player')),
                ('schools', models.ManyToManyField(help_text='many schools with many offer', to='players.school')),
            ],
        ),
        migrations.AddField(
            model_name='committment',
            name='school',
            field=models.ForeignKey(help_text='foreign key with school', null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.school'),
        ),
    ]
