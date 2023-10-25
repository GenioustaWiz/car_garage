from django.urls import path
from .views import *
from .ajax_common_data_send_V import *

urlpatterns = [
    path('', main_index, name='main_index'),
    # AJAX COMMON DATA GET AND SEND
    path('get-common-data/', get_common_data, name='get_common_data'),
    # ==========================
]