from django.urls import path, include
from .views import Search_by_name

"""
application URLS--> serach_engine
"""

urlpatterns = [
    path('by_name/', Search_by_name.as_view()),
    
    # path('by_number/', ),
]