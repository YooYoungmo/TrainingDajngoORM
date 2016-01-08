from django.test import TestCase
from Lesson2.models import Reporter, Article
from datetime import date

class ReporterAndArticleTest(TestCase):
    
    def test_save(self):
        # given, when
        reporter = Reporter.objects.create(first_name='Youngmo', last_name='Yoo', email='gigamadness@gmail.com')
        article = Article.objects.create(headline='Django ORM', pub_date=date(2016, 1, 8), reporter=reporter)
        
        # then
        self.assertEqual(Reporter.objects.count(), 1)
        self.assertEqual(Article.objects.count(), 1)
        
        actual_article = Article.objects.get(id=article.id)
        self.assertEqual(actual_article, article)
        self.assertEqual(actual_article.reporter, reporter)
    
    def test_delete(self):
        # given
        reporter = Reporter.objects.create(first_name='Youngmo', last_name='Yoo', email='gigamadness@gmail.com')
        Article.objects.create(headline='Django ORM1', pub_date=date(2016, 1, 8), reporter=reporter)
        Article.objects.create(headline='Django ORM2', pub_date=date(2016, 1, 8), reporter=reporter)
        
        # when
        reporter.delete()
        
        # then
        self.assertEqual(Reporter.objects.count(), 0)
        self.assertEqual(Article.objects.count(), 0)
        
    def test_retrieve_from_reporter(self):
        # given
        reporter = Reporter.objects.create(first_name='Youngmo', last_name='Yoo', email='gigamadness@gmail.com')
        article_django_orm1 = Article.objects.create(headline='Django ORM1', pub_date=date(2016, 1, 8), reporter=reporter)
        Article.objects.create(headline='Django ORM2', pub_date=date(2016, 1, 8), reporter=reporter)
        
        # when
        actual_reporter = Reporter.objects.get(id=reporter.id)
        actual_article_django_orm1 = actual_reporter.article_set.get(id=article_django_orm1.id)
        
        # then
        self.assertEqual(article_django_orm1, actual_article_django_orm1)
        
    def test_retrieve_from_article(self):
        # given
        reporter = Reporter.objects.create(first_name='Youngmo', last_name='Yoo', email='gigamadness@gmail.com')
        article_django_orm1 = Article.objects.create(headline='Django ORM1', pub_date=date(2016, 1, 8), reporter=reporter)
        Article.objects.create(headline='Django ORM2', pub_date=date(2016, 1, 8), reporter=reporter)
        
        # when
        actual_article_django_orm1 = Article.objects.get(id=article_django_orm1.id)
        actual_reporter = actual_article_django_orm1.reporter
        
        # then
        self.assertEqual(reporter, actual_reporter)
       
        
    