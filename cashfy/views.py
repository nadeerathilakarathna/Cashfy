from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import Icon
from .models import Account
from .models import Category






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
        return render(request, 'dashboard.html')

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
            'id' : account.id,
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
            object = Account.objects.create(uid=uid, name=account, icon=icon, checked=False)
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
        amount = request.POST['amount']
        description = request.POST['description']

        object = Category.objects.create(uid=uid, timestamp=date, icon=icon, expense=False)
        object.save()



    return HttpResponse("Done")
