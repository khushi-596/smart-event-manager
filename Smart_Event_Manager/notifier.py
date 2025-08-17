import csv
from event_manager import EventManager
from datetime import datetime

def load_recipients(csv_path):
    recipients = []
    try:
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if 'email' in row:
                    recipients.append(row['email'])
    except FileNotFoundError:
        print("Recipient list not found.")
    return recipients

def send_reminder(event, csv_path="../data/attendance.csv"):
    recipients = load_recipients(csv_path)
    if not recipients:
        print("No recipients found.")
        return

    for to in recipients:
        print("=== Reminder ===")
        print(f"To: {to}")
        print(f"Subject: Upcoming Event - {event.name}")
        print(f"Body:\nDon't forget:\n")
        print(f"Event: {event.name}")
        print(f"Date: {event.date}")
        print(f"Time: {event.time}")
        print(f"Type: {event.type}")
        if event.location:
            print(f"Location: {event.location}")
        print("================\n")

def main():
    EM = EventManager()
    today = datetime.today().strftime('%d-%m-%Y')
    events = EM.view_events_by_date(today)
    recipients = load_recipients()

    if not events:
        print("No events today.")
        return

    if not recipients:
        print("No recipients to send reminders to.")
        return

    print(f"Sending reminders for {len(events)} event(s) to {len(recipients)} recipient(s)...\n")

    for event in events:
        for recipient in recipients:
            send_reminder(recipient, event)

if __name__ == "__main__":
    main()

