from django.urls import path

from . import views

# learning 3
app_name = 'polls'
# learning 1
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # learning 3
    # # # ex: /polls/5/
    # # # the 'name' value as called by the {% url %} template tag
    # # path('<int:question_id>/', views.detail, name='detail'),
    #
    # # added the word 'specifics'
    # path('specifics/<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    # learning 4
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
