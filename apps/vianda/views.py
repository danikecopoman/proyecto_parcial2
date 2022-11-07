from django.shortcuts import redirect, render

from apps.vianda.forms import ViandaForm
from apps.vianda.models import Vianda
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='usuario:login')
#@permission_required('vianda.add_vianda', raise_exception=True)
def registrar_vianda(request):
    id_user = request.POST.get('username', None)
    if(request.method == 'POST'):
        vianda_form = ViandaForm(request.POST, prefix='vianda')
        if vianda_form.is_valid():
            vianda_form.save()
            return redirect(to="vianda:registrar_vianda")
    else:
        vianda_form = ViandaForm(prefix='vianda')
    return render(request,'vianda/agregarVianda.html',{'vianda_form': vianda_form})

@login_required(login_url='usuario:login')
def listar_vianda(request,pk):
    # id_user = request.POST.get('username', None)
    vianda = Vianda.objects.filter(user_id=pk)
    return render(request,'vianda/listaVianda.html',{'vianda':vianda})

