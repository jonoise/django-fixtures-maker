class Fixture():
    def __init__(self, app, model, fields):
        self.app = app
        self.model = model
        self.fields = fields

    def check_fields(self):
        if self.fields is not list:
            return False
        else:
            return True