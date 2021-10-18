from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from gas import Gas


@api_view(['POST'])
@csrf_exempt
def calc(request):
    print(request.data)
    g = Gas(float(request.data['C1']),
            float(request.data['C2']),
            float(request.data['C3']),
            float(request.data['iC4']),
            float(request.data['nC4']),
            float(request.data['neoC5']),
            float(request.data['iC5']),
            float(request.data['nC5']),
            float(request.data['C6+']),
            float(request.data['CO2']),
            float(request.data['N2']),
            int(request.data['Nm'].split(sep="N")[1]))
    g.calc_MN()
    print(request.data)
    return Response({"MN": g.MN})
