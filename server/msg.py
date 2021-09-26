import json
class msg:
    def __init__(self, t, b):
        self.type = t
        self.body = b
    def unpack_data(self, data):
        as_str = data.decode("ASCII")
        as_json = json.loads(as_str)
        self.type = as_json["type"]
        self.body = as_json["body"]
    def pack(self):
        return json.dumps(self.__dict__).encode("ASCII")