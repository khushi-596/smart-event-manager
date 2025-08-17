import uuid

class Event:
    def __init__(self, name, date, time, type_, location=None, id=None):
        self.id = id or str(uuid.uuid4())[:6]
        self.name = name
        self.date = date
        self.time = time
        self.type = type_
        self.location = location or ""
        
    def to_dict(self):
        return {
            "id": self.id, "name": self.name, "date": self.date, "time": self.time, "type": self.type, "location": self.location }
            
    @staticmethod
    def from_dict(data):
        return Event(data["name"], data["date"], data["time"], data["type"], data.get("location", ""), data["id"])
