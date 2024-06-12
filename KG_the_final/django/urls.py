from django.conf.urls import url
from django.urls import path, re_path
from .views import *
urlpatterns = [

    url(r"^$", index, name="index"),
    url(r"^index$", index, name="index"),
    url(r"^search$", search, name="search"),

    url(r"^wenda$", wenda, name="wenda"),

    url(r"^init_node_datas$", init_node_datas, name="init_node_datas"),
    url(r"^init_relation_datas$", init_relation_datas, name="init_node_datas"),

]
