from .models import MiddleWare


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST':
            json = request.POST
        else:
            json = request.GET
        if request.path.find('admin') > 0:
            pass
        else:
            MiddleWare(
                path=request.path,
                method=request.method,
                json=json
            ).save()
        response = self.get_response(request)
        return response
