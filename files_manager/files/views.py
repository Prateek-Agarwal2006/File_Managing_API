from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from .models import File
from rest_framework import status
from rest_framework.views import APIView



class File_Upload(APIView):
    def post(self, request):
        if 'file' not in request.FILES:
            return Response({'error':'No file found'},status=status.HTTP_400_BAD_REQUEST)
        
        uploaded_file=request.FILES['file']
        filename=uploaded_file.name
        file_content=uploaded_file.read()

        try:
            file_obj=File.objects.create(filename=filename,content=file_content)
            return Response({'message':f'Successfully uploaded "{file_obj.filename}"'},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error':f'Failed to upload file:{str(e)}'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class File_Detail(APIView):
        
    def get(self, request, filename):
        try:
            file_need = File.objects.filter(filename=filename)
            if file_need.exists():
             file=file_need.first()

             content_bytes = bytes(file.content) 
             content_str = content_bytes.decode('utf-8')
            
             response = HttpResponse(content_str,content_type='application/octet-stream')
             response['Content-Disposition'] =f'attachment;filename={filename}'
             response['media_type']='application/octet-stream'
            
            
             return Response({
             "media_type":response['media_type'],
             "content_disposition":response['Content-Disposition'],
              "content":content_str
             },status=status.HTTP_200_OK)
            else:
                return Response({"error":f'No file with name"{filename}"'},status=status.HTTP_404_NOT_FOUND)

        
        except Exception as e:
            return Response({"error":f"An error occurred:{str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self,request,filename):
         files = File.objects.filter(filename=filename)
         if not files.exists():
            return Response({'error':f'NO file with name"{filename}"'},status=status.HTTP_404_NOT_FOUND)
        
         files.delete()
         return Response({'message':'File deleted successfully'},status=status.HTTP_200_OK)    

        




# Create your views here.
