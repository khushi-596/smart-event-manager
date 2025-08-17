from event import Event
from event_manager import EventManager
from day import Validate_date, Validate_time
from admin import Admin

def main():
    EM = EventManager()
    admin = Admin()
    
    print("Admin login")
    user = input("Username: ")
    pw = input("Password: ")
    
    if not admin.login(user, pw):
        print("Invalid Username or Password")
        return
        
    while True:
        print("\n--Menu--")
        print("1. Add Event")
        print("2. Edit Event")
        print("3. Delete Event")
        print("4. View Events by Date")
        print("5. View Today's Events")
        print("6. Search Events")
        print("7. Send Reminders")
        print("8. Exit")
        
        choice = input("Enter Choice: ")
        
        if choice == "1":
            name = input("Name: ")
            date = input("Date (DD-MM-YYYY): ")
            time = input("Time (HH:MM): ")
            type_ = input("Type: ")
            location = input("Location: ")
            
            if not Validate_date(date) or not Validate_time(time):
                print("Invalid date or time format")
                continue
            
            try:
                event = Event(name, date, time, type_, location)
                EM.add_event(event)
                print(f"Event added with ID: {event.id}")
            except Exception as e:
                print("Not valid", e)
                
        elif choice == "2":
            eid = input("Event ID or Name: ")
            field = input("Field to edit (name, date, time, type, location): ")
            value = input("New Value: ")
            if field in ["date", "time"]:
                if field == "date" and not Validate_date(value):
                    print("Invalid date format")
                    continue
                if field == "time" and not Validate_time(value):
                    print("Invalid time format")
                    continue
            if EM.edit_event(eid, field, value):
                print("Event updated")
            else:
                print("Event not found")
                
        elif choice == "3":
            eid = input("Event ID or name: ")
            if EM.delete_event(eid):
                print("Event deleted")
            else:
                print("Event not found")
                
        elif choice == "4":
            date = input("Date (DD-MM-YYYY): ")
            events = EM.view_events_by_date(date)
            if not events:
                print("No events found")
            for e in events:
                print(f"[{e.id}] {e.time} | {e.name} | {e.type} | {e.location}")
                
        elif choice == "5":
            events = EM.view_today_events()
            if not events:
                print("No events found")
            for e in events:
                print(f"[{e.id}] {e.time} | {e.name} | {e.type} | {e.location}")
                
        elif choice == "6":
            keyword = input("Search: ")
            results = EM.search_events(keyword)
            for e in results:
                print(f"[{e.id}] {e.date} {e.time} | {e.name} | {e.type}")
                
        elif choice == "7":  # <-- New reminder feature
            identify = input("Event ID or name: ")
            file_path = input("Enter attendance CSV file path (default: attendance.csv):").strip() or "attendance.csv"

            matched_event = next((e for e in EM.events if e.id == identify or e.name == identify), None)

            if not matched_event:
                print("Event not found.")
            else:
                from notifier import send_reminder
                send_reminder(matched_event, file_path)
                
        elif choice == "8":
            print("Exiting..")
            break
        
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()
            
