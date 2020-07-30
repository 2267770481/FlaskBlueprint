from flask.views import View


class Third(View):
    print('third')

    def dispatch_request(self, name=None):
        return 'Third'
