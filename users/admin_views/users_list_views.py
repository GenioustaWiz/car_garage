from django.shortcuts import render
from ..models import User

from django.contrib.auth.decorators import login_required, permission_required
@login_required
#only users authorized to view users profile will get acces to this
@permission_required('auth.view_user', raise_exception=True) 
def user_list(request):
    profiles = User.objects.all()
    return render(request, 'maindashboard/users_admin/users_list.html', {'profiles': profiles})
