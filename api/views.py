from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from api.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .mypagination import MyLimit
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Count, Sum
from django.db.models import Q

from api.serializers import *

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime

from django.shortcuts import get_object_or_404

#



class DealWonRevinueViewSet(APIView):
    def get(self, request):
        year = request.query_params.get("year")

        def get_monthly_total_costs(year):
            # quotations = Quotation.objects.filter(date__contains=year)
            deal_won_status = Status.objects.get(status="DEAL WON").id

            quotations = Quotation.objects.filter(
                date__contains=year, status=deal_won_status
            )
            monthly_costs = {}
            # quotations = 0

            for quotation in quotations:
                if quotation.date:
                    date_parts = quotation.date.split(
                        "/"
                    )  # Assuming date is in DD/MM/YY format
                    if len(date_parts) == 3:
                        month = int(date_parts[1])  # Extracting the month part
                        cost = float(quotation.total_with_discount or 0)

                        # Add the cost to the existing total for the specific month
                        if month in monthly_costs:
                            monthly_costs[month]["total_cost"] += cost
                            # quotations=quotations+1
                            monthly_costs[month]["quotations"] += 1
                        else:
                            monthly_costs[month] = {
                                "month": month,
                                "total_cost": cost,
                                "quotations": 1,
                            }

            return list(monthly_costs.values())

        if year:
            results = get_monthly_total_costs(year)
            return Response(results)
        else:
            return Response({"error": "Please provide a year"}, status=400)

class RevinueR01ViewSet(APIView):
    def get(self, request):
        year = request.query_params.get("year")

        def get_monthly_total_costs(year):
            # quotations = Quotation.objects.filter(date__contains=year)
            quotations = Quotation.objects.filter(
                date__contains=year, revision_no="R01"
            )
            monthly_costs = {}
            # quotations = 0

            for quotation in quotations:
                if quotation.date:
                    date_parts = quotation.date.split(
                        "/"
                    )  # Assuming date is in DD/MM/YY format
                    if len(date_parts) == 3:
                        month = int(date_parts[1])  # Extracting the month part
                        cost = float(quotation.total_with_discount or 0)

                        # Add the cost to the existing total for the specific month
                        if month in monthly_costs:
                            monthly_costs[month]["total_cost"] += cost
                            # quotations=quotations+1
                            monthly_costs[month]["quotations"] += 1
                        else:
                            monthly_costs[month] = {
                                "month": month,
                                "total_cost": cost,
                                "quotations": 1,
                            }

            return list(monthly_costs.values())

        if year:
            results = get_monthly_total_costs(year)
            return Response(results)
        else:
            return Response({"error": "Please provide a year"}, status=400)


class RevinueViewSet(APIView):
    def get(self, request):
        year = request.query_params.get("year")

        def get_monthly_total_costs(year):
            quotations = Quotation.objects.filter(
                date__contains=year, quotation_number__startswith="SM"
            ).order_by("quotation_number", "-revision_no")

            latest_quotations = {}
            for quotation in quotations:
                key = quotation.quotation_number
                if (
                    key not in latest_quotations
                    or latest_quotations[key].revision_no < quotation.revision_no
                ):
                    latest_quotations[key] = quotation

            monthly_costs = {}
            for quotation in latest_quotations.values():
                if quotation.date:
                    date_parts = quotation.date.split(
                        "/"
                    )  # Assuming date is in DD/MM/YY format
                    if len(date_parts) == 3:
                        month = int(date_parts[1])  # Extracting the month part
                        cost = float(quotation.total_with_discount or 0)

                        if month in monthly_costs:
                            monthly_costs[month]["total_cost"] += cost
                            monthly_costs[month]["quotations"] += 1
                        else:
                            monthly_costs[month] = {
                                "month": month,
                                "total_cost": cost,
                                "quotations": 1,
                            }

            return list(monthly_costs.values())

        if year:
            results = get_monthly_total_costs(year)
            return Response(results)
        else:
            return Response({"error": "Please provide a year"}, status=400)


class QuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer
    pagination_class = MyLimit

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Save the data and return the serialized representation
        # print(serializer)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def get_queryset(self):
        queryset = super().get_queryset()
        user_client_id = self.request.query_params.get("user_client_id")
        quotation_number = self.request.query_params.get("quotation_number")
        client_name = self.request.query_params.get("client_name")

        if client_name:
            queryset = queryset.filter(
                Q(client_name__icontains=client_name)
                | Q(client_id__icontains=client_name)
            )
        if user_client_id:
            queryset = queryset.filter(user_client_id=user_client_id)
        if quotation_number:
            queryset = queryset.filter(quotation_number=quotation_number)

        return queryset


# class QuotationNumberCountView(APIView):
#     def get(self, request, *args, **kwargs):
#         # queryset = Quotation.objects.all()
#         queryset = Quotation.objects.exclude(status__isnull=True).exclude(status='')
#         # Apply filters based on query parameters
#         user_client_id = self.request.query_params.get('user_client_id')
#         client_name = self.request.query_params.get('client_name')
#         quotation_number = self.request.query_params.get('quotation_number')

#         if client_name:
#             queryset = queryset.filter(Q(client_name__icontains=client_name) | Q(client_id__icontains=client_name))
#         if user_client_id:
#             queryset = queryset.filter(user_client_id=user_client_id)
#         if quotation_number:
#             queryset = queryset.filter(quotation_number=quotation_number)

#         # Get count of unique quotation_number values and their occurrences
#         unique_quotation_count = queryset.values('status').annotate(count=Count('status')).order_by('status')
#         quotation_number_names = []
#         for entry in unique_quotation_count:
#             status = entry['status']
#             try:
#                 status = Status.objects.get(id=status).status
#                 entry['status'] = status
#             except Status.DoesNotExist:
#                 pass  # Handle if ID not found

#             quotation_number_names.append(entry)

#         return Response(unique_quotation_count)


class QuotationNumberCountView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Quotation.objects.exclude(status__isnull=True).exclude(status=False)

        # Apply filters based on query parameters
        user_client_id = self.request.query_params.get("user_client_id")
        client_name = self.request.query_params.get("client_name")
        quotation_number = self.request.query_params.get("quotation_number")

        if client_name:
            queryset = queryset.filter(
                Q(client_name__icontains=client_name)
                | Q(client_id__icontains=client_name)
            )
        if user_client_id:
            queryset = queryset.filter(user_client_id=user_client_id)
        if quotation_number:
            queryset = queryset.filter(quotation_number=quotation_number)

        # Retrieve the latest revisions for each unique quotation_number
        latest_quotations = {}
        for quotation in queryset:
            key = quotation.quotation_number
            if (
                key not in latest_quotations
                or latest_quotations[key].revision_no < quotation.revision_no
            ):
                latest_quotations[key] = quotation

        # Get count of unique quotation_number values and their occurrences
        unique_quotation_count = (
            Quotation.objects.filter(id__in=[q.id for q in latest_quotations.values()])
            .values("status")
            .annotate(count=Count("status"), total=Sum("total_with_discount"))
            .order_by("status")
        )

        quotation_number_names = []
        for entry in unique_quotation_count:
            status = entry["status"]
            try:
                status = Status.objects.get(id=status).status
                entry["status"] = status
            except Status.DoesNotExist:
                pass  # Handle if ID not found

            quotation_number_names.append(entry)

        return Response(unique_quotation_count)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [SearchFilter]
    # search_fields=['item_name','item_category']
    pagination_class = MyLimit


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    filter_backends = [SearchFilter]
    search_fields = ["item_name"]
    pagination_class = MyLimit

    def get_queryset(self):
        item_category = self.request.query_params.get("item_category")
        if item_category:
            return Items.objects.filter(item_category=item_category)
        return Items.objects.all()


class ItemsViewStatistic(APIView):
    def get(self, request, *args, **kwargs):
        # queryset = Items.objects.all()
        queryset = Items.objects.exclude(item_category__isnull=True).exclude(
            item_category=""
        )

        # Apply filters based on query parameters

        # Get count of unique quotation_number values and their occurrences
        unique_item_categories = (
            queryset.values("item_category")
            .annotate(count=Count("item_category"))
            .order_by("item_category")
        )
        # filtered_categories = [entry for entry in unique_item_categories if entry['item_category'] is not None]
        quotation_number_names = []
        for entry in unique_item_categories:
            item_category = entry["item_category"]
            try:
                item_category = Category.objects.get(id=item_category).category
                entry["item_category"] = item_category
                quotation_number_names.append(entry)
            except Category.DoesNotExist:
                pass  # Handle if ID not found

        return Response(unique_item_categories)


class UserViewStatistic(APIView):
    def get(self, request, *args, **kwargs):
        # queryset = Items.objects.all()
        queryset = Quotation.objects.exclude(user_client__isnull=True).exclude(
            user_client=""
        )

        # Apply filters based on query parameters

        # Get count of unique quotation_number values and their occurrences
        unique_item_categories = (
            queryset.values("user_client")
            .annotate(count=Count("user_client"))
            .order_by("user_client")
        )
        # filtered_categories = [entry for entry in unique_item_categories if entry['item_category'] is not None]

        return Response(unique_item_categories)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [SearchFilter]
    search_fields = ["contact_person_name", "user_client_id"]
    pagination_class = MyLimit

    def get_queryset(self):
        queryset = super().get_queryset()
        user_client_id = self.request.query_params.get("user_client_id")

        if user_client_id:
            queryset = queryset.filter(user_client_id=user_client_id)

        return queryset


class InventoysViewSet(viewsets.ModelViewSet):
    queryset = Inventorys.objects.all()
    serializer_class = InventorysSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = InteriorGallery.objects.all()
    serializer_class = ImageSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentAdmission.objects.all()
    serializer_class = StudentAdmissionSerializer


class DesignGalleryViewSet(viewsets.ModelViewSet):
    queryset = DesignGallery.objects.all()
    serializer_class = DesignGallerySerializer
