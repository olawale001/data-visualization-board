from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SalesRecord
from .serializers import SalesRecordSerializer
from django.db.models import Sum
from django.shortcuts import render

@api_view(['GET'])
def sales_data(request):
    sales = SalesRecord.objects.all()
    serializer = SalesRecordSerializer(sales, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def sales_summary(request):
    summary = SalesRecord.objects.values('product').annotate(
        total_quantity=Sum('quantity'),
        total_revenue=Sum('price')
    )
    return Response(summary)



def dashboard_view(request):
    return render(request, 'dashboard/index.html')

def home_view(request):
    return render(request, 'home.html')