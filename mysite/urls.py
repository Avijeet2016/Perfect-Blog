from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .views import user_login, user_logout 
from users.views import profile, contact, contact_list, contact_details, create_about, show_about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/preferences', TemplateView.as_view(template_name='admin/preferences.html')),
    path('', include('blog.urls')),

    path('profile/admin/', profile, name='profile'),
    path('contact/form', contact, name='contact'),
    path('contact/list', contact_list, name='contact-list'),
    path('contact/details/<int:id>', contact_details, name='contact-details'),

    path('create/about', create_about, name='create-about'),
    path('show/about', show_about, name='about'),

    path('summernote/', include('django_summernote.urls')),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)