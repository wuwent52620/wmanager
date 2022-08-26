import importlib
import os


def get_blue(base):
    base_name = os.path.basename(os.path.dirname(base))
    from sanic import Blueprint
    import views as view_pack
    args = []
    for filename in os.listdir(os.path.dirname(base)):
        if filename.endswith('.py') and not filename.startswith('__'):
            res = filename.rstrip('.py')
            package = f"{view_pack.__name__}.{base_name}.{res}"
            ret = importlib.import_module(package)
            _blue = getattr(ret, 'blue')
            args.append(_blue)

    return Blueprint.group(*args, url_prefix=f"/{base_name}")
