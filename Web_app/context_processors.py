from django.contrib.auth import get_user_model

def logged_user_processor(request):
    if request.user.is_authenticated:  # Verificar si el usuario está autenticado
        User = get_user_model()
        user = User.objects.using('secondary').get(pk=request.user.pk)
        return {'user': user}
    else:
        return {}