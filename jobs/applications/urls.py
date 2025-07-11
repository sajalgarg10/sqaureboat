from django.urls import path
from applications import views

urlpatterns = [
    path("jobs/" , views.post_jobs ),
    path("jobs/<int:pk>" , views.apply_job),
    path("" , views.list_jobs ),
    path("<int:pk>" , views.get_application),
    path("all/" , views.list_jobs_applicants )
]

