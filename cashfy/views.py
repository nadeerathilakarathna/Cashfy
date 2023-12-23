import datetime
from django.contrib.auth.models import User,auth
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import Icon
from .models import Account
from .models import Category
from .models import Transaction
from .models import Config
import datetime




# # Create your views here.
# def dashboard(request):
#     return render(request, 'dashboard.html')

# def dashboard(request):
#     if request.headers.get('Accept') == 'application/json':
#         # Return JSON response
#         json_data = {
#             'key1': 'value1',
#             'key2': 'value2',
#             'key3': 'value3',
#         }
#         return JsonResponse(json_data)
#     else:
#         # Return regular HTML response
#         return render(request, 'dashboard.html')

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        uid = request.user.id
        if not(Config.objects.filter(uid=uid).exists()):
            Config.objects.create(uid=uid,selection='day',start=datetime.date.today().strftime("%Y-%m-%d"),end=datetime.date.today().strftime("%Y-%m-%d")).save()
        return render(request, 'dashboard.html')
    else:
        return render(request, 'index.html')


def geticons(request):
    icons = Icon.objects.all()
    icon_names = [icon.name for icon in icons]

    # Serialize to JSON
    json_data = json.dumps({'icon_names': icon_names}, cls=DjangoJSONEncoder, indent=2)
    print("__________________________")
    print(json_data)
    return JsonResponse(json_data, safe=False)

def getaccounts(request):
    uid = request.GET.get('uid')
    accounts = Account.objects.filter(uid=uid)

    accounts_list = [
        {
            'id': account.id,
            'name': account.name,
            'icon': account.icon,
            'checked': account.checked,
        }
        for account in accounts
    ]
    return JsonResponse({'accounts': accounts_list})

def createaccount(request):
    if request.method =='POST':
        uid = request.POST['uid']
        account = request.POST['account']
        initial = request.POST['initial']
        icon = request.POST['icon']

        account_exists = Account.objects.filter(uid=uid, name=account).exists()
        if not account_exists:
            initial_exists = Category.objects.filter(uid=uid, name="Initial Balance", ).exists()
            if not (initial_exists):
                object = Category.objects.create(uid=uid, name="Initial Balance", icon='label_important', expense=False)
                object.save()
            object = Account.objects.create(uid=uid, name=account, icon=icon, checked=True)
            object.save()
            object = Transaction.objects.create(uid=uid, timestamp=datetime.date.today().strftime("%Y-%m-%d"), amount=initial, account=Account.objects.filter(uid=uid, name=account).first().id,
                                                detail=Account.objects.filter(uid=uid, name=account).first().name, category=Category.objects.filter(uid=uid, name="Initial Balance").first().id, expense=False)
            object.save()

        else:
            raise ("Duplicates found")
    return HttpResponse("Done")

def getexpenses(request):
    uid = request.GET.get('uid')
    expenses = Category.objects.filter(uid=uid , expense=True)
    expense_list = [
        {
            'name': expense.name,
            'icon': expense.icon,
            'id': expense.id,
        }
        for expense in expenses
    ]
    return JsonResponse({'expenses': expense_list})

def getincome(request):
    uid = request.GET.get('uid')
    incomes = Category.objects.filter(uid=uid , expense=False)
    income_list = [
        {
            'name': income.name,
            'icon': income.icon,
            'id': income.id,
        }
        for income in incomes
        if income.name != "Initial Balance"
    ]
    return JsonResponse({'incomes': income_list})


def createexpense(request):
    if request.method =='POST':
        uid = request.POST['uid']
        name = request.POST['name']
        icon = request.POST['icon']

        expense_exists = Category.objects.filter(uid=uid, name=name, expense=True).exists()
        if not expense_exists:
            object = Category.objects.create(uid=uid, name=name, icon=icon, expense=True)
            object.save()
        else:
            raise ("Duplicates found")
    return HttpResponse("Done")


def createincome(request):
    if request.method =='POST':
        uid = request.POST['uid']
        name = request.POST['name']
        icon = request.POST['icon']

        income_exists = Category.objects.filter(uid=uid, name=name, expense=False).exists()
        if not income_exists:
            object = Category.objects.create(uid=uid, name=name, icon=icon, expense=False)
            object.save()
        else:
            raise ("Duplicates found")
    return HttpResponse("Done")

def createtransaction(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        category = request.POST['category']
        date = request.POST['date']
        account = request.POST['account']
        amount = request.POST['amount']
        description = request.POST['description']
        account_field_type = Transaction._meta.get_field('account').get_internal_type()

        print("Type of 'account' field:", account_field_type)



        expense = Category.objects.get(id=category).expense
        account_id = Account.objects.get(uid=uid, name=account).id

        object = Transaction.objects.create(uid=uid, timestamp=date, amount=amount, account=account_id, detail=description, category=category, expense=expense)
        object.save()
    return HttpResponse("Done")


def selectaccount(request):
    if request.method == 'POST':
        id = request.POST['id']
        Account.objects.filter(id=id).update(checked = not(Account.objects.filter(id=id).values('checked').first()['checked']))
    return HttpResponse("Done")

def getdaybar(request):
    uid = request.GET.get('uid')
    config = Config.objects.filter(uid=uid).first()
    if config.selection == 'day':
        duration = config.start.strftime('%b %d')
    elif config.selection == 'week':
        duration = config.start.strftime('%b %d') +" - "+ config.end.strftime('%b %d')
    elif config.selection == 'month':
        duration = config.start.strftime('%Y %b')
    elif config.selection == 'year':
        duration = config.start.strftime('%Y')
    else:
        duration = ' '
    config ={
        'selection': config.selection,
        'duration': duration,
    }
    return JsonResponse({'config': config})


def changedaybar(request):
    uid = request.POST['uid']
    selection = request.POST['selection']
    object = Config.objects.filter(uid=uid).first()
    object.selection = selection

    today=datetime.datetime.now().date()
    to = (today.weekday() - 0) % 7
    monday = today - datetime.timedelta(days=to)
    sunday = monday + datetime.timedelta(days=6)

    monthstart = datetime.date(today.year,today.month,1)
    monthend = datetime.date(today.year, (today.month + 1)%12, 1) - datetime.timedelta(days=1)

    yearstart = datetime.date(today.year, 1, 1)
    yearend = datetime.date(today.year,12,31)

    if selection=='day':
        object.start = datetime.date.today().strftime("%Y-%m-%d")
        object.end = datetime.date.today().strftime("%Y-%m-%d")
    elif selection == 'week':
        object.start = monday.strftime("%Y-%m-%d")
        object.end = sunday.strftime("%Y-%m-%d")
    elif selection == 'month':
        object.start = monthstart.strftime("%Y-%m-%d")
        object.end = monthend.strftime("%Y-%m-%d")
    elif selection == 'year':
        object.start = yearstart.strftime("%Y-%m-%d")
        object.end = yearend.strftime("%Y-%m-%d")
    else:
        object.start = datetime.date(2000,1,1).strftime("%Y-%m-%d")
        object.end = today.strftime("%Y-%m-%d")

    object.save()

    return HttpResponse("Done")

def navigation(request):
    today = datetime.datetime.now().date()
    uid = request.POST['uid']
    direction = request.POST['direction']

    config = Config.objects.filter(uid=uid).first()
    if direction=='prev':
        if config.selection == 'day':
            config.start = config.start - datetime.timedelta(days=1)
            config.end = config.end - datetime.timedelta(days=1)
        if config.selection == 'week':
            config.start = config.start - datetime.timedelta(days=7)
            config.end = config.end - datetime.timedelta(days=7)
        if config.selection == 'month':
            config.end = config.start - datetime.timedelta(days=1)
            config.start = config.end.replace(day = 1)
        if config.selection == 'year':
            config.start = datetime.datetime(config.start.year - 1, 1, 1)
            config.end = datetime.datetime(config.end.year - 1, 12, 31)
        else:
            pass
    else:
        if config.selection == 'day':
            config.start = config.start + datetime.timedelta(days=1)
            config.end = config.end + datetime.timedelta(days=1)
        if config.selection == 'week':
            config.start = config.start + datetime.timedelta(days=7)
            config.end = config.end + datetime.timedelta(days=7)
        if config.selection == 'month':
            config.start = config.end + datetime.timedelta(days=1)
            config.end = (config.start.replace(day=1) + datetime.timedelta(days=32 - config.start.day)).replace(day=1) - datetime.timedelta(days=1)
        if config.selection == 'year':
            config.start = datetime.datetime(config.start.year + 1, 1, 1)
            config.end = datetime.datetime(config.end.year + 1, 12, 31)
        else:
            pass

    try:
        if config.start.date()<today:
            config.save()
    except:
        if config.start<today:
            config.save()

    return HttpResponse("Done")