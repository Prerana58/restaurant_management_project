from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Coupon

# Create your views here.
class CouponValidationView(APIView):
    def Post(self,request):
        code=request.data.get('code')
        if not code:
            return Response({'error':'Coupon code is required.'},status=status.HTTP_400_BAD_REQUEST)
        try:
            coupon=Coupon.objects.get(code=code)
        except Coupon.DoesNotExist:
            return Response({'error':'Coupon code is required.'},status=status.HTTP_400_BAD_REQUEST)

        today=timezone.now().date()
        if not coupon.is_active:
            return Response({'error':'This coupon is not active.'},status=status.HTTP_400_BAD_REQUEST)
        if today<coupon.valid_from or today>coupon.valid_until:
            return Response({'error':'This coupon is not valid at this time.'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'success':'True',
        'discount_percentage':coupon.discount_percentage,
        'message':f'Coupon{coupon.code} applied successfully!'},status=status.HTTP_200_OK)
