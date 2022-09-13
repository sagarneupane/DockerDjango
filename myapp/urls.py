from django.urls import path
import myapp.views as mv

urlpatterns = [
    path("", mv.index, name="index"),
    path("contact/", mv.contact, name="contact"),
]