from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.views import APIView
from .serializers import RecordSerializer
from app.models import Record
from rest_framework import generics




class RecordView(generics.ListAPIView):
	
	serializer_class = RecordSerializer  
	authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
	
	def get_queryset(self):
		user=self.request.user
		return Record.objects.filter(owner=user)


# class RecordView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    
# 	def get(self, request):
        
# 		if user:
# 			token, created=Token.objects.get_or_create(user=user)
# 			data={'token' : token.key}
# 			return Response(data, status=status.HTTP_201_CREATED)		
# 		raise exceptions.AuthenticationFailed('인증 정보 x')