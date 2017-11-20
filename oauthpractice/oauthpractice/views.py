from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')
#
@login_required()
def secret_page(request, *args, **kwargs):
    print(request.user)
    return HttpResponse('Secret contents!', status=200)

# 실패할시 logged in requered 로 넘어감 신기하게.
