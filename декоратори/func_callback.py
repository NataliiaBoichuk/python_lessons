# Функция обратного вызова — это функция,
# которая вызывается при срабатывании определенного события (переходе на страницу,
# получении сообщения или окончании обработки процессором).
app = {}


def callback(route):
    def wrapper(func):
        app[route] = func

        def wrapped():
            ret = func()
            return ret

        return wrapped

    return wrapper


@callback('/')
def index():
    print('index')
    return 'OK'


print('> старт')
route = app.get('/')
if route:
    resp = route()
    print('ответ:', resp)

print('> конец')
