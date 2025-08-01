import json
import stripe
import traceback
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
