from datetime import datetime

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from code_manager.models import Code
from code_manager.permissions import CodeModelPermissions, CodeCheckPermission
from code_manager.serializers import CodeSerializer


# Create your views here.


class CodeView(ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    permission_classes = [CodeModelPermissions]
    throttle_scope = 'code'

    @action(detail=False, methods=['post'], permission_classes=[CodeCheckPermission])
    def check(self, request):
        print(request.user)
        if 'code' in request.data:
            f = Code.objects.filter(code=request.data['code'])
            if len(f) == 1:
                c = f.first()
                c.last_used = datetime.now()
                c.save()
                r = dict()
                r['valid'] = True
                return Response(r)
            return Response(
                {
                    'error': 'Code invalid or not found!',
                    'valid': False
                }, status=status.HTTP_404_NOT_FOUND)
        return Response(
            {
                'error': 'Bad request',
                'wanted': {
                    'code': 'int'
                }
            }, status=status.HTTP_400_BAD_REQUEST)
