from django.shortcuts import render
from ..models import Visit
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
@login_required
@staff_member_required
def visit_list(request):
    total_visitors, total_visits = Visit.get_total_visitors_and_visits()
    visitors = Visit.objects.all()
    
    # Pass these values to your template or do whatever you need to do with them.
    
    return render(request, 'maindashboard/visitors_counter/visit_list.html', {
        'visitors': visitors,
        'total_visitors': total_visitors,
        'total_visits': total_visits,
    })