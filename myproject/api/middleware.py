import json
import jwt
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.utils.deprecation import MiddlewareMixin

SECRET_KEY = "JWT_SECRET_KEY"

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/getToken'):
            return None

        token = request.headers.get('Authorization', None)
        if token is not None:
            try:
                user_jwt = jwt.decode(
                    token,SECRET_KEY, algorithms=['HS256']
                )
                if(user_jwt['user_name'] == 'testpayload' and user_jwt['email']=='testdjango@gmail.com'):
                    return None

                response = {"message": "Invalid credentials"}
                return HttpResponse(json.dumps(response), status=401)
            except Exception as e: # NoQA
                response = {"message": "Authorization not found, Please send valid token in headers"}
                return HttpResponse(json.dumps(response), status=401)

        response = {"message": "Authorization not found, Please enter the token"}
        return HttpResponse(json.dumps(response), status=401)
 
        
       