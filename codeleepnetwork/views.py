import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Item
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# Create your views here.

@csrf_exempt
def careers(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Item.objects.create(
            username = data['username'], 
            created_datetime = datetime.now(), 
            title = data['title'],
            content = data['content'] 
        )
        
        return HttpResponse(status=200)
    
    elif request.method == "GET":
        itens = Item.objects.all()
        response = []
        for item in itens:
            response.append({
                'id': item.id,
                'username': item.username,
                'created_datetime': item.created_datetime,
                'title': item.title,
                'content': item.content
            })
            
        return JsonResponse(response, content_type="application/json", safe=False)

@csrf_exempt
def careersArgs(request, id):
    if request.method == "PATCH":
        data = json.loads(request.body)
        item_to_edit = Item.objects.get(id=id)
        item_to_edit.title = data['title']
        item_to_edit.content = data['content']
        item_to_edit.save()
        return HttpResponse(status=200)
    
    elif request.method == "DELETE":
        item_to_delete = Item.objects.get(id=id)
        item_to_delete.delete()
        return HttpResponse(status=200)
