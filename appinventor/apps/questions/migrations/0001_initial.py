# Generated by Django 2.0.1 on 2018-11-13 19:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_num', models.IntegerField(default=0, verbose_name='回复数')),
                ('vote_num', models.IntegerField(default=0, verbose_name='点赞数')),
                ('answer_desc', models.TextField(max_length=50000, verbose_name='回答正文内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '回答',
                'verbose_name_plural': '回答',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(1, '待解决'), (2, '已解决'), (3, '悬赏')], default=1, help_text='问题状态', verbose_name='问题状态')),
                ('name', models.CharField(max_length=100, verbose_name='问题名')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('reply_num', models.IntegerField(default=0, verbose_name='回复数')),
                ('vote_num', models.IntegerField(default=0, verbose_name='点赞数')),
                ('question_brief', models.TextField(max_length=500, verbose_name='问题简短描述')),
                ('question_desc', models.TextField(max_length=50000, verbose_name='问题正文内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('label_1', models.CharField(blank=True, max_length=20, null=True, verbose_name='标签名1')),
                ('label_2', models.CharField(blank=True, max_length=20, null=True, verbose_name='标签名2')),
                ('label_3', models.CharField(blank=True, max_length=20, null=True, verbose_name='标签名3')),
                ('label_4', models.CharField(blank=True, max_length=20, null=True, verbose_name='标签名4')),
                ('label_5', models.CharField(blank=True, max_length=20, null=True, verbose_name='标签名5')),
            ],
            options={
                'verbose_name': '问题',
                'verbose_name_plural': '问题',
            },
        ),
        migrations.CreateModel(
            name='SubAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=0, verbose_name='位于回答跟帖中的索引下标')),
                ('sub_answer_desc', models.TextField(max_length=50000, verbose_name='跟帖正文内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('parent_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Answers', verbose_name='父回答')),
            ],
            options={
                'verbose_name': '回答跟帖',
                'verbose_name_plural': '回答跟帖',
            },
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Questions', verbose_name='问题'),
        ),
    ]
