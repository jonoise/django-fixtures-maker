import json

class Fixture():
    def __init__(self, app, model, headers=None, list_of_fields=None, json_fn):
        self.app = app
        self.model = model
        self.headers = headers
        self.fields = list_of_fields
        self.objects = []
        self.object_ = {}
        self.body = {}
        self.json_filename = json_fn

    def create_objects(self):
        pk = 0
        for row in self.fields:
            pk += 1
            self.object_ = {}
            self.body = {}
            self.object_['model'] = '{}.{}'.format(self.app, self.model).lower()
            self.object_['pk'] = pk
            for index, value in enumerate(row):
                self.body[self.headers[index]] = value
            self.object_['fields'] = self.body
            self.objects.append(self.object_)

    def return_objects(self):
        return self.objects
        
    def return_json(self):
        return json.dumps(self.objects, indent=2)
    
    def create_json_file(self):
        with open(f'{self.json_filename}.json', 'w') as f:
            f.write(self.return_json())



