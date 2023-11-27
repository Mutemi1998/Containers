from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("refrigerated-containers", views.refrigerated_containers, name="refrigerated-containers"),
    path("storage-containers", views.storage_containers, name="storage-containers"),
    path("shipping-containers", views.shipping_containers, name="shipping-containers"),
    path("high-cube-containers", views.high_cube_containers, name="high-cube-containers"),
    path("tunnel-containers", views.tunnel_containers, name="tunnel-containers"),
    path("side-access-containers", views.side_access_containers, name="side-access-containers"),
    path("containers-for-sale", views.containers_for_sale, name="containers-for-sale"),
    path("deliveries", views.deliveries, name="deliveries"),
    path("faq", views.faq, name="faq"),
    path("contact", views.contact, name="contact"),
    path("quotation", views.quotation, name="quotation"),
    path("modification", views.modification, name="modification"),
    path("24-7-technical-container-support", views.technical_container_support, name="24-7-technical-container-support"),
    path("container-commissioning", views.container_commissioning, name="container-commissioning"),
    path("container-site-surveys", views.container_site_surveys, name="container-site-surveys"),
    path("container-painting", views.container_painting, name="container-painting"),
        path("container-dimensions", views.container_dimensions, name="container-dimensions"),
]