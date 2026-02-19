from app_di_test.views import homepage, about_us

urlpatterns = [
    path('home/', homepage, name="Pagina di home"),
    path('about/', about_us, name="Pagina di presentazione"),

]