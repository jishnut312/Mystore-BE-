import json
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            items = data['items']
            
            # Optional: print items to debug
            print("Received items for Stripe:", items)

            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=items,
                mode='payment',
                success_url='http://localhost:3000/success',
                cancel_url='http://localhost:3000/cancel',
            )
            return JsonResponse({'id': session.id})
        except Exception as e:
            print("Stripe error:", e)
            return JsonResponse({'error': str(e)}, status=400)
