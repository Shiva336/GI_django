from .services import process_csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserCSVUploadAPIView(APIView):
    """
    API to upload CSV and process user data
    """
    
    def post(self, request):
        file = request.FILES.get("file")
    
        if not file:
            return Response(
                {"error": "No file provided"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try: 
            result = process_csv(file)
            return Response(result, status=status.HTTP_200_OK)
        
        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        except Exception as e: 
            return Response(
                {"error": "Internal server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

