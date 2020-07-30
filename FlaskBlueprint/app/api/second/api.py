from flask.views import View


class Second(View):
    print('second')

    def dispatch_request(self, name=None):
        return 'second'

    def get(self):
        return {
            "code": 000,
            "msg": ""
        }