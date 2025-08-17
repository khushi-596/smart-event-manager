# 📅 Smart Event Manager

A simple, terminal-based Event Management System built in Python. 
It allows an admin to manage events, view schedules, search, and send reminders to attendees — all from the command line.

---

## 🚀 Features

- ✅ Admin Login (Username/Password)
- 📝 Add, Edit, Delete Events
- 📆 View Events by Specific Date or Today
- 🔍 Search Events by Name or Type
- 🔔 Send Event Reminders (console-based simulation)
- ✅ Date and Time Format Validation
- 💾 Persistent storage via `JSON` and `CSV`

---

## 📁 Project Structure

smart-event-manager/
├── README.md
├── Smart_Event_Manager/
│ ├── main.py # Main CLI program
│ ├── event.py # Event class
│ ├── day.py # Date & time validation
│ ├── admin.py # Admin authentication
│ ├── event_manager.py # Core logic: CRUD, search, etc.
│ ├── notifier.py # Simulated email reminders
├── data/
│ ├── events.json # Event storage
│ └── attendance.csv # Recipients list (email)

## 🔧 Requirements

- Python 3.7+
- No external libraries required

---

## ⚙️ Setup & Usage

### 📥 Clone the Repository

```bash
git clone https://github.com/yourusername/smart-event-manager.git
cd smart-event-manager

Run the program:
python3 Smart_Event_Manager/main.py

Admin Credentials
Username: admin
Password: admin@123

Sample Run
--Menu--
1. Add Event
2. Edit Event
3. Delete Event
4. View Events by Date
5. View Today's Events
6. Search Events
7. Exit

Date & Time Format
Date: DD-MM-YYYY
Time: HH:MM (24-hour format)

