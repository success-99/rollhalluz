from django.contrib import admin
from django.urls import path, include
from users.views import home, signup_view, success, table_user, login_admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-admin/', admin.site.urls),
    path('', home, name='index'),
    path('signup/', signup_view, name='signup'),
    path('success/', success, name='success'),
    path('list/', table_user, name='table-users'),
    path('javohir/', login_admin, name='login-admin'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'users.views.handling_404'
handler500 = 'users.views.handling_500'
