from rest_framework.views import APIView
from rest_framework.response import Response
from douban.serializers import BookSeri
from douban.models import Book

class BookList(APIView):

    def get(self, request):
        books = Book.objects.all()
        seri = BookSeri(books, many=True)
        return Response(seri.data)
