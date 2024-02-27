import argparse
import datetime
import sqlite3

# Function creates table in database
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute(
    'CREATE TABLE IF NOT EXISTS contacts_list(id INTEGER PRIMARY KEY, name TEXT, number INTEGER, date DATETIME)')
    conn.commit()

# Function deletes table from  database
def delete_table(conn):
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS contacts_list")
    conn.commit()

# Function to save contact information into database
def save_contact(conn, name, number, date):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts_list(name, number, date) VALUES(?, ?, ?)", ((name), (number), (date)))
    conn.commit()

# Function to update_contact in database
def update_contact(conn, name, number, date):
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts_list SET name = ?, date = ? WHERE number = ?", (name, date, number))
    conn.commit()

# Function to get contacts
def list_contacts(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts_list")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.commit()

# Functon for argparser initilizaton
def main():
    parser = argparse.ArgumentParser(description="Contact Manager")
    parser.add_argument("command", choices=["add", "update", "list"], help="Command to execute")
    parser.add_argument("__name", type=str, help="Name of person")
    parser.add_argument("__number", type=int, help="Phone number of person")
    parser.add_argument("__date", type=str, default=datetime.date.today().strftime("%Y-%m-%d"), help="current date")
    args = parser.parse_args()
    print(args.__name, args.__number, args.__date)

    conn = sqlite3.connect('contacts')
    

    if args.command == "add":
        create_table(conn)
        if not args.__name or not args.__number:
            print("NAME AND NUMBER MUST BE DEFINE")
            return
        save_contact(conn, args.__name, args.__number, args.__date)
    elif args.command == "update":
        if not args.__name or not args.__number:
            print("NAME AND NUMBER MUST BE DEFINE")
            return
        update_contact(conn, args.__name, args.__number, args.__date)
    else:
        list_contacts(conn)
    conn.close()


if __name__ == "__main__":
    main()

        
        


    

   


