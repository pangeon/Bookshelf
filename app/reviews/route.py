from django.urls import path, re_path

from . import views





urlpatterns = [
    path('/add', views.add_question),
    path('/show-id/<int:question_id>', views.show_id),
    re_path(r'^/show-year/(?P<year>[0-9]{4})/$', views.show_by_year)

]