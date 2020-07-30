from flask.views import View


class First(View):
    print('first')

    def dispatch_request(self, name=None):
        return '<h2>first</h2>'
