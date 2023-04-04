COLUMN_NAMES = {
    'code_author': 'Код автора',
    'name': 'Имя',
    'surname': 'Фамилия',
    'year_of_birth': 'Дата рождения',
    'code_book' : 'Код книги',
    'title_book' : 'Название книги',
    'pages' : 'Количество страниц',
    'code_author_id': 'Код автора',
    'code_publish_id': 'Код издательства',
    'code_publish': 'Код издательства',
    'publish': 'Издательство',
    'city' : 'Город',
    'id_book' : 'Код книги',
    'book_price': 'Цена книги',
    'supplier_id': 'Код поставщика',
    'supplier_name': 'Название поставщика',
    'article_id' : 'Код статьи увольнения',
    'article_name' : 'Cтатья увольнения',
    'reason' : 'Причина',
    'article_number' : 'Номер статьи увольнения',
    'paragraph_number' : 'Пункт увольнения',
    'doc_id' : 'Код документа',
    'doc_number' : 'Название документа',
    'registration_date' : 'Дата регистрации',
    'dismissal_date' : 'Дата увольнения',
    'compensation' : 'Денежная компенсация',
    'dismissal_article_id': 'Код статьи увольнения',
    'emp_id': 'Код сотрудника',
    'last_name' : 'Фамилия',
    'first_name' : 'Имя',
    'middle_name' : 'Отчество',
    'position' : 'Должность',
    'department' : 'Департамент',
    'hire_date' : 'Дата найма'
}

from django.shortcuts import render
from django.db import connection
from .models import Employees,User
from .forms import RegistrationForm,AuthForm,DocumentForm
from django.contrib import messages
from django.contrib.auth import login

def home(request):
    return render(request, 'blog/home.html', {})

def employee_list(request):
    employee_list = Employees.objects.all()
    context = {'employee_list': employee_list}
    return render(request, 'blog/employee_list.html', context)

def analyze(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        with connection.cursor() as cursor:
            cursor.execute("CALL `analyze`(%s)" ,[query])
            length = cursor.fetchall()
            cursor.nextset()
            rows = cursor.fetchall()

        context = {
            'query': query,
            'rows': rows,
            'length': length,
            'query_type': 'analyze',
        }
        return render(request, 'blog/result.html', context)
    return render(request, 'blog/analyze.html')

def execute_query(request):
    if request.method == 'POST':
        context = {}
        query = request.POST.get('query', '')
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                columns = [col[0] for col in cursor.description]
                columns = [COLUMN_NAMES.get(name, name) for name in columns]
                rows = cursor.fetchall()
            context = {
                'query': query,
                'rows': rows,
                'columns': columns,
                'query_type': 'request',
            }
            return render(request, 'blog/result.html', context)
        except:
            messages.error(request,"Неправильный запрос")
    return render(request, 'blog/request.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                middle_name = form.cleaned_data['middle_name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            user.save()
            return home(request)
    else:
        form = RegistrationForm()

    return render(request, 'blog/register.html', {'form': form})

def examples(request):
    if request.method == 'POST':
        columns =[]
        if 'button1' in request.POST:
            with connection.cursor() as cursor:
                cursor.execute("CALL `count_supplier`()")
                result = cursor.fetchall()
                query_type = 'count_supplier'
        elif 'button2' in request.POST:
            with connection.cursor() as cursor:
                cursor.execute('select code_book,title_book,PublishingHouse.publish from Book INNER JOIN PublishingHouse on Book.code_publish_id = PublishingHouse.code_publish;')
                columns = [col[0] for col in cursor.description]
                columns = [COLUMN_NAMES.get(name, name) for name in columns]
                result = cursor.fetchall()
                query_type = 'cursor'
        elif 'button3' in request.POST:
            with connection.cursor() as cursor:
                cursor.execute('select AVG(book_price)*123.34 from blog_books')
                result = cursor.fetchall()
                query_type = 'avg_price'
        context = {
            'result':result,
            'query_type':query_type,
            'columns':columns
            }
        return render(request, 'blog/result.html', context)
    return render(request, 'blog/examples.html')

def _login(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM user_reg WHERE username=%s AND password=%s", [username, password])
                row = cursor.fetchone()
            if row:
                my_dict = dict(zip([col[0] for col in cursor.description], row))
                user = User(**my_dict)
                login(request, user)
                return home(request)
            messages.error(request, "Неправильный логин или пароль")
    else:
        form = AuthForm()
    return render(request, 'blog/login.html', {'form': form})

def create_person(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    else:
        form = DocumentForm()
    return render(request, 'blog/create_person.html', {'form': form})











