from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import ContactUs
from .serializers import ContactUsSerializer

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check for duplicates
        if ContactUs.objects.filter(phone=serializer.validated_data['phone'], date=timezone.now().date()).exists():
            return Response({'error': 'This phone number has already been used today.'}, status=status.HTTP_400_BAD_REQUEST)
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
