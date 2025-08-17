import json
import os
from event import Event
from day import Validate_date, Validate_time
from datetime import datetime

class EventManager:
    def __init__(self, file_path="../data/events.json"):
        self.file_path = file_path
        self.events = self.load_events()
        
    def load_events(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r') as f:
            return [Event.from_dict(e) for e in json.load(f)]
            
    def save_events(self):
        with open(self.file_path, 'w') as f:
            json.dump([e.to_dict() for e in self.events], f, indent=4)
            
    def add_event(self, event):
        if self._is_duplicate(event):
            raise ValueError("Duplicate event with same date and name.")
        if self._has_conflict(event):
            raise ValueError("Conflict: Another event exists at the same time.")
        self.events.append(event)
        self.save_events()
        
    def _is_duplicate(self, new_event):
        return any(e.name == new_event.name and e.date == new_event.date for e in self.events)
        
    def _has_conflict(self, new_event):
        return any(e.date == new_event.date and e.time == new_event.time for e in self.events)
        
    def delete_event(self, identify):
        initial = len(self.events)
        self.events = [e for e in self.events if e.id != identify and e.name != identify]
        self.save_events()
        return len(self.events) < initial
        
    def edit_event(self, identify, field, new_value):
        for e in self.events:
            if e.id == identify or e.name == identify:
                if field in e.__dict__:
                    setattr(e, field, new_value)
                    self.save_events()
                    return True
        return False
        
    def view_events_by_date(self, date_str):
        return sorted([e for e in self.events if e.date == date_str], key=lambda x: x.time)
        
    def view_today_events(self):
        today = datetime.today().strftime('%d-%m-%Y')
        return self.view_events_by_date(today)
        
    def search_events(self, keyword):
        keyword = keyword.lower()
        return [e for e in self.events if keyword in e.name.lower() or keyword in e.type.lower()]
