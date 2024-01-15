from django.shortcuts import render
from rest_framework import serializers

from app.models import Book
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


@api_view(['GET'])
def index(request):
    books = Book.objects.all()
    ser = BookSerializer(books, many=True)
    return Response(ser.data)


@api_view(['POST'])
def create(request):
    create_book = {
        'name':request.data.get('name'),
        'author':request.data.get('author'),
        'status':request.data.get('status')
    }
    Book.objects.create(**create_book)

    return Response({"msg":"添加成功！"})


@api_view(['PUT'])
def update(request, pk):
    book = Book.objects.get(id=pk)
    if not book:
        return Response({'msg':'没有相关数据！'})

    update_book = {
        'name':request.data.get('name'),
        'author':request.data.get('author'),
        'status':request.data.get('status')
    }
    book.name = request.data.get('name')
    book.author = request.data.get('author')
    book.status = request.data.get('status')
    book.save()
    return Response({"msg":'更新成功！'})

