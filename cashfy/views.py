from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import Icon
from .models import Account





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
            'name': account.name,
            'icon': account.icon,
            'checked': account.checked,
        }
        for account in accounts
    ]
    return JsonResponse({'accounts': accounts_list})
