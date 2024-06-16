from django.contrib import admin
from django.urls import path, include
from users.views import home, signup_view, success, table_user, login_admin, delete_user, user_detail, signup_view1, table_user1
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-admin/', admin.site.urls),
    path('', home, name='index'),
    path('signup-1/', signup_view, name='signup-1'),
    path('signup-2/', signup_view1, name='signup-2'),
    path('success/', success, name='success'),
    path('list/', table_user, name='table-users'),
    path('list1/', table_user1, name='table-users1'),
    path('javohir/', login_admin, name='login-admin'),
    path('users/delete/<int:user_id>/', delete_user, name='delete-user'),
    path('users/detail/<int:user_id>/', user_detail, name='user-detail'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'users.views.handling_404'
handler500 = 'users.views.handling_500'
