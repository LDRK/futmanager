from drf_yasg.utils import swagger_auto_schema

def swagger_get(serializer, desc="Listado de objetos"):
    def decorator(func):
        return swagger_auto_schema(
            method='get',
            operation_description=desc,
            responses={200: serializer(many=True)}
        )(func)
    return decorator


def swagger_post(serializer, desc="Crea un nuevo objeto"):
    def decorator(func):
        return swagger_auto_schema(
            method='post',
            operation_description=desc,
            request_body=serializer,
            responses={201: serializer}
        )(func)
    return decorator


def swagger_put(serializer, desc="Actualiza un objeto existente"):
    def decorator(func):
        return swagger_auto_schema(
            method='put',
            operation_description=desc,
            request_body=serializer,
            responses={200: serializer}
        )(func)
    return decorator


def swagger_delete(desc="Elimina un objeto existente"):
    def decorator(func):
        return swagger_auto_schema(
            method='delete',
            operation_description=desc,
            responses={204: 'Eliminado correctamente'}
        )(func)
    return decorator
