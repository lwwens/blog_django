#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
author:Ewen Lai
email:lwwens@gmail.com ; lai_wei_wen@qq.com ;
time:2019-04-25 week4 14:15:18
"""


from django.db import models
from django.utils import timezone


class Category(models.Model):
    """
    博客类别
    """
    name = models.CharField(verbose_name='博客类别', max_length=20)
    number = models.IntegerField(verbose_name='分类数目', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客类别'
        verbose_name_plural = '博客类别'


class Tag(models.Model):
    """
    博客标签
    """
    name = models.CharField(verbose_name='博客标签', max_length=20)
    number = models.IntegerField(verbose_name='标签数目', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客标签'
        verbose_name_plural = '博客标签'


class Blog(models.Model):
    """
    博客
    """
    title = models.CharField(verbose_name='标题', max_length=100)
    content = models.TextField(verbose_name='正文', default='')
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    modify_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    click_nums = models.IntegerField(verbose_name='点击量', default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='博客类别')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='博客标签')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'


class Comment(models.Model):
    """
    博客评论
    """
    name = models.CharField(verbose_name='姓名', max_length=20, default='佚名')
    content = models.CharField(verbose_name='内容', max_length=300)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='博客')

    def __str__(self):
        return self.content[:10]

    class Meta:
        verbose_name = '博客评论'
        verbose_name_plural = '博客评论'


class Counts(models.Model):
    """
    统计博客、分类和标签的数目
    """
    blog_nums = models.IntegerField(verbose_name='博客数目', default=0)
    category_nums = models.IntegerField(verbose_name='分类数目', default=0)
    tag_nums = models.IntegerField(verbose_name='标签数目', default=0)
    visit_nums = models.IntegerField(verbose_name='网站访问量', default=0)

    class Meta:
        verbose_name = '数目统计'
        verbose_name_plural = '数目统计'
