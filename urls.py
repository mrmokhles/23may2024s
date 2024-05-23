
from django.contrib import admin
from django.urls import path,include
from app1 import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.SignupPage,name='signup'),

    path('login/',views.LoginPage,name='login'),

    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    
    path('saveEnquiry/',views.saveEnquiry,name='saveEnquiry'),

    path('contacts/',views.contactPage,name='contacts'),

    path('update/',views.UpdateBlog,name='update'),

    path('update/edit/<int:id>',views.EditBlog,name='edit'),

    path('up/<int:id>',views.up,name='up'),

    path('update/delete/<int:id>',views.deleteData,name='delete'),

    path('searchEmployee/',views.searchEmp,name='searchEmployee'),

    path('search/',views.searchBar,name='search'),

    path('countries_gdp_list', views.countries_gdp_list, name='countries_gdp_list'),

    path('countries_gdp_excel', views.countries_gdp_excel, name='countries_gdp_excel'),

    path('savecountries/',views.savecountries,name='savecountries'),

    path('import/',views.importExcel,name='import'),

    path('gallery', views.gallery, name="gallery"),
    
    path('cascade', views.Cascade, name="cascade"),

    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    
    
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX

    path('json/', views.json, name='json'),

    path('jsonData',views.jsonITs,name='jsonData'),


    path('api',include('api.urls')),

    path('dropdown', views.dp, name='dropdown'),


    path('adminemplist/', views.AdminEmployeeList, name='adminemployeeList'),
    path('adminaddemplist', views.AdminaddSaveData, name='adminaddemplist'),

    path('adminemplist/adsming',views.admin_update,name='adsming'),

    path('adminemplist/empedit/<int:id>',views.adminemployeeEdit,name='empedit'),

    path('adminup/<int:id>',views.adminup,name='adminup'),

    path('adminemplist/delete/<int:id>',views.admindeleteData,name='delete'),

    path('deleteall',views.adminMultipledeleteData,name='deleteall'),

# try edit and delete
    path('edi',views.ediId,name='edi'),
    path('delID',views.deleteId,name='delID'),
    path('delmultipleID',views.deletmultipleId,name='delmultipleID'),



    path('adminemplist/filteradminEmployeeList',views.FilteradminEmployeeList,name='filteradminEmployeeList'),
    
    path('checkpdfresult/',views.funcpdf,name='checkpdfresult'),

    path('pdf_view', views.ViewPDF.as_view(), name="pdf_view"),
    # path('pdf_download', views.DownloadPDF.as_view(), name="pdf_download"),

    path('pdf_download', views.DownloadPDF, name="pdf_download"),


    path('excel_download', views.AdminEmployeeexcel, name="excel_download"),

    path('reportlabpdf', views.reportLabdownloadPDF, name="reportlabpdf"),

    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),

    path('pdf_with_watermark/', views.generate_pdf_with_watermark, name='generate_pdf_with_watermark'),


 
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
