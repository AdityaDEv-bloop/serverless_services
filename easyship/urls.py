from django.urls import path
from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from easyship.views import MultilanguageTranslate

description = "The Ship Easy is a RESTful service designed to streamline and automate the invoicing and shipment documentation process within the global shipping and export industry. This API allows logistics companies, exporters, and freight forwarders to efficiently manage invoices, link them to shipments, and maintain accurate, real-time records of transactions and export details.Key Features:Invoice Management: Create, update, retrieve, and delete invoices with support for multi-currency, tax handling, and associated shipment information.Shipment Linking: Associate invoices with corresponding shipment data including container numbers, ports of origin/destination, vessel details, and delivery timelines.Export Document Support: Store and manage essential export-related documents such as bills of lading, certificates of origin, and customs invoices.Status Tracking: Monitor shipment and invoice status throughout the export process—from draft to finalized, shipped, and completed.Data Consistency & Compliance: Ensure invoice data meets regulatory requirements for customs, VAT, and international trade documentation"

schema_view = get_schema_view(
    openapi.Info(
        title="Ship Easy APIs",
        default_version="v1",
        description=description,
        license=openapi.License(name="MIT License"),
    ),
    public=False,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path(
        "ship-easy/translate/", view=MultilanguageTranslate.as_view(), name="translate"
    ),
    path(
        "ship-easy/swagger<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "ship-easy/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "ship-easy/redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
