from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from code_manager.models import Code
from code_manager.serializers import CodeSerializer


# Create your views here.


@api_view(['POST'])
def check_code(request):
    if 'code' in request.data:
        f = Code.objects.filter(code=request.data['code'])
        if len(f) == 1:
            c = f.first()
            c.last_used = datetime.now()
            c.save()
            r = CodeSerializer(c).data
            r['valid'] = True
            return Response(r)
        return Response(
            {
                'error': 'Code invalid or not found!',
            }, status=status.HTTP_404_NOT_FOUND)
    return Response(
        {
            'error': 'Bad request',
            'wanted': {
                'code': 'int'
            }
        }, status=status.HTTP_400_BAD_REQUEST)
