
from rest_framework import generics
from rest_framework import status, filters

from users.models import User
from users.serializers import UserSerializer

from user_contacts.models import UserContacts
from user_contacts.serializers import UserContactsSerializer

# def search_by_name(request):        
#     if request.method == 'GET': # this will be GET now      
#         book_name =  request.GET.get('search') # do some research what it does       

#         status = Add_prod.objects.filter(bookname__icontains=book_name) 
#         # filter returns a list so you might consider skip except part
#         return render(request,"search.html",{"books":status})
#     else:
#         return render(request,"search.html",{})



class Search_by_name(generics.ListCreateAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = UserContacts.objects.all()
    serializer_class = UserContactsSerializer