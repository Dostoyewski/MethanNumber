from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
@csrf_exempt
def calc(request):
    print(request.data)
    return Response({"MN": 123})
