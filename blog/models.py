from django.db import models
from django.contrib.auth.models import AbstractUser

class Employees(models.Model):
    emp_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    hire_date = models.DateField()

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return str(self.last_name)+' ' + str(self.first_name)+' ' + str(self.middle_name)

class DismissalArticle(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_name = models.CharField(max_length=50)
    reason = models.CharField(max_length=100)
    article_number = models.IntegerField()
    paragraph_number = models.IntegerField()

    class Meta:
        db_table = 'dismissal_articles'

    def __str__(self):
        return str(self.article_name)

class Document(models.Model):
    doc_id = models.AutoField(primary_key=True)
    doc_number = models.CharField(max_length=50)
    registration_date = models.DateField()
    dismissal_date = models.DateField(null=True, blank=True)
    dismissal_article = models.ForeignKey(DismissalArticle, on_delete=models.SET_NULL, null=True, blank=True)
    emp = models.ForeignKey(Employees, on_delete=models.CASCADE)
    compensation = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'documents'

class User(AbstractUser):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['last_name','first_name','middle_name','email','phone_number','password']
    class Meta:
        db_table = 'user_reg'

class Deliveries(models.Model):
    supplier_id = models.IntegerField(primary_key = True)
    supplier_name = models.CharField(max_length = 100)

class Books(models.Model):
    id_book = models.IntegerField(primary_key = True)
    book_price = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        db_table = 'blog_books'


class PublishingHouse(models.Model):
    code_publish = models.IntegerField(primary_key=True)
    publish = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    class Meta:
        db_table = 'PublishingHouse'

class Book(models.Model):
    code_book = models.IntegerField(primary_key=True)
    title_book = models.CharField(max_length=40)
    code_author = models.ForeignKey('Author', on_delete=models.CASCADE)
    pages = models.IntegerField()
    code_publish = models.ForeignKey('PublishingHouse', on_delete=models.CASCADE)
    class Meta:
        db_table = 'Book'

class Author(models.Model):
    code_author = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    year_of_birth = models.IntegerField()
    class Meta:
        db_table = 'Author'

