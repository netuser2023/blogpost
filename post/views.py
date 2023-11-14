from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def posts(request):
    content = {
        'content':[
            {'Title': 'America', 'Id': '2390', 'Createdate':'12/03/2023', 'image':'images/america.jpg'},
            {'Title': 'Chicago', 'Id': '2930', 'Createdate':'26/09/2023', 'image':'images/chicago.jpg'},
            {'Title': 'Moscow', 'Id': '3245', 'Createdate':'03/10/2023', 'image':'images/moscow.jpg'},
            {'Title': 'Dubai', 'Id': '4859', 'Createdate':'29/05/2023', 'image':'images/dubai.jpg'},
            ]
    }
    return render(request=request, template_name='main.html', context=content)
    