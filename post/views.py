from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def posts(request):
    content = {
        'content':[
            {'Title': 'America', 'Id': '2390', 'Createdate':'12/03/2023'},
            {'Title': 'Chicago', 'Id': '2930', 'Createdate':'26/09/2023'},
            {'Title': 'Moscow', 'Id': '3245', 'Createdate':'03/10/2023'},
            {'Title': 'Tashkent', 'Id': '4859', 'Createdate':'29/05/2023'},
            {'Title': 'Mercedes', 'Id': '6754', 'Createdate':'14/07/2023'},
            {'Title': 'Audi RS7', 'Id': '9978', 'Createdate':'19/02/2023'},
            ]
    }
    return render(request=request, template_name='main.html', context=content)
    