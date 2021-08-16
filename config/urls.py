from django.contrib import admin
from django.urls import path, include
from accounts import views as views_accounts
from aluno.views import (home, create_aluno, update_aluno, delete_aluno, visualizar_perfil, indicacoes)
from indicado.views import (create_indicado, update_indicado, delete_indicado)


app_name = 'aluno'


urlpatterns = [
    #USUERIO E ADMIN
    path('admin/', admin.site.urls),
	path('Mais_Amigos_Mais_Descontos/', views_accounts.registerPage, name="registerPage"),
	path('login/', views_accounts.loginPage, name="login"),  
	path('logout/', views_accounts.logoutUser, name="logout"),
    path('entrar/', views_accounts.loginAPI, name="loginAPI"), 

    #ALUNO
	path('', home, name='home'),
    path('meus-dados/aluno/', create_aluno, name='create_aluno'),
    path('meus-dados/<str:profile>/', create_aluno, name='create_aluno'),
    path('atualizar/<str:user>/', update_aluno, name='update_aluno'),
    path('profile/<str:user>/', visualizar_perfil, name='visualizar_perfil'),
    path('apagar/aluno-<int:id>/', delete_aluno, name='delete_aluno'),

    #INDICADO
    path('indique-um-amigo/', create_indicado, name='create_indicado'),
    path('indicado/update/<int:id>/', update_indicado, name='update_indicado'),
    path('indicado/delete/<int:id>/', delete_indicado, name='delete_indicado'),
    path('minhas-indicacoes/', indicacoes, name='indicacoes'),
]

#ADMINISTRATIVE
admin.site.index_title = 'Luiz Henrique Chaves'
admin.site.site_title = 'Administrativo'
admin.site.site_header = 'Luiz Henrique'