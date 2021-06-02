from django.urls import path
from . import views

app_name = 'content'

urlpatterns = [
    path('',views.contentView,name="content_view"),
    path('test',views.test,name="test"),
    path('<single_slug>',views.single_slug,name='single_slug'),
    path('enroll/<single_slug>',views.enroll_single_slug,name='enroll'),
    path('details/<single_slug>',views.detailed_single_slug,name='details'),
]

'''path('', views.contentView),
path('reviews/', views.reviewsView),
path('kunal/',views.kunalView)'''

#urlpatterns = format_suffix_patterns(urlpatterns)