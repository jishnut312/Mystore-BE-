import json
import stripe
import traceback
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from orders.models import DeliveryAddress


stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            items = data.get('items', [])
            
            if not isinstance(items, list) or not items:
                return JsonResponse({'error': 'Invalid or empty items list'}, status=400)

            print(f"Stripe checkout attempt with {len(items)} item(s)")

            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=items,
                mode='payment',
                success_url='https://your-frontend/success',
                cancel_url='https://your-frontend/cancel',
            )
            return JsonResponse({'id': session.id})
        except Exception as e:
            print("Stripe error:", e)
            traceback.print_exc()
            return JsonResponse({'error': str(e)}, status=400)
# views.py
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def has_saved_address(request):
    address = DeliveryAddress.objects.filter(user=request.user).last()
    has_address = address is not None
    return Response({ "has_address": has_address })

# views.py
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_address(request):
    address = DeliveryAddress.objects.filter(user=request.user).last()
    if address:
        return Response({
            "fullName": address.full_name,
            "phone": address.phone,
            "house": address.address,
            "city": address.city,
            "state": address.state,
            "pincode": address.pincode
        })
    return Response({ "error": "No address found" }, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_user_address(request):
    data = request.data

    DeliveryAddress.objects.create(
        user=request.user,
        full_name=data.get("fullName"),
        phone=data.get("phone"),
        pincode=data.get("pincode"),
        address=data.get("house"),  # or data.get("address") based on your frontend
        city=data.get("city"),
        state=data.get("state")
    )

    return Response({"message": "Address saved"})