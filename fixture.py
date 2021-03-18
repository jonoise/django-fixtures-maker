class Fixture():
    def __init__(self, app, model, fields):
        self.app = app
        self.model = model
        self.fields = fields
    
    def listing_fields(self):
        ls = []
        ls.append(self.fields)
        return ls

    def check_fields(self):
        if type(self.fields) is list:
            return self.fields            
        else:
            return self.listing_fields()