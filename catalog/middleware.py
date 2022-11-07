from .models import MiddleWare


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        method = request.method
        if path[0:7] == '/admin/':
            pass
        else:
            k = MiddleWare(
                path=path,
                method=method
            )
            q = [k]
            MiddleWare.objects.bulk_create(q)

        response = self.get_response(request)


        return response