from rest_framework.decorators import api_view
from django.http import JsonResponse, FileResponse
from utils.lib import store_media

# Create your views here.

@api_view(['POST', 'GET'])
def user_media(request):
    if request.method == "POST":
        try:
            request_data = request.data.dict()
            store_media(request_data['avatar'], request_data["id"], "users")
            return JsonResponse({"success": True})
        except Exception as e:
            print(str(e))
            return JsonResponse({"success": False})
    elif request.method == 'GET':
        id = request.query_params['id']
        return FileResponse(open(f"./storage/users/{id}.jpg", 'rb'))