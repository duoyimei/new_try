from django.db import models

# Create your models here


# class CrawlDetail(models.Model):
#     user_id = models.CharField(max_length=255)
#     user_name = models.CharField(max_length=255)
#     post_time = models.CharField(max_length=255)
#     blog_text = models.TextField()
#     check_in_location = models.CharField(max_length=255)
#
#     class Meta:
#         abstract = True
#
#
# class crawl_blog(CrawlDetail):
#     class Meta:
#         managed = False
#         db_table = 'crawl_blog'
#
#
# class InfoDetail(models.Model):
#     user_id = models.CharField(max_length=255)
#     user_name = models.CharField(max_length=255)
#     user_gender = models.CharField(max_length=255)
#     user_place = models.CharField(max_length=255)
#     user_label = models.CharField(max_length=255)
#     user_introduction = models.CharField(max_length=255)
#     user_birthday = models.CharField(max_length=255)
#     user_sentiment = models.CharField(max_length=255)
#     user_authentication = models.CharField(max_length=255)
#     user_study = models.CharField(max_length=255)
#     user_work = models.CharField(max_length=255)
#
#     class Meta:
#         abstract = True
#
#
# class user_info(InfoDetail):
#     class Meta:
#         managed = False
#         db_table = 'user_info'
