import json
import datetime

#function for reading notes from a file
def read_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

#function for writing notes to a file
def write_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4) # отступ в 4 пробела

#function for adding a new note
def add_note():
    title = input("Enter the title of the note: ")
    msg = input("Enter the msg of the note: ")
    note = {
        'id': len(notes) + 1,
        'title': title,
        'msg': msg,
        'created_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'updated_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    notes.append(note)
    write_notes(notes)
    print("Note saved!")

#function for editing an existing note
def edit_note():
    note_id = int(input("Enter the ID of the note to edit: "))
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input("Enter a new note title: ")
            note['msg'] = input("Enter a new note body: ")
            note['updated_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            write_notes(notes)
            print("Note edited!")
            return
    print("Not founded")

#function to delete an existing note
def delete_note():
    note_id = int(input("Enter the ID of the note to delete: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            write_notes(notes)
            print("Note deleted")
            return
    print("Not founded")

#function for displaying a list of notes
def list_notes():
    filter_date = input("Enter the date to filter (yyyy-mm-dd): ")
    filtered_notes = [note for note in notes if note['created_at'].startswith(filter_date)]
    if filtered_notes:
        for note in filtered_notes:
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Msg: {note['msg']}")
            print(f"Date of creation: {note['created_at']}")
            print(f"Last modified date: {note['updated_at']}")
            print('-' * 20)
    else:
        print("Not founded")

notes = read_notes()

while True:
    command = input("Enter (add, edit, delete, list, exit): ")
    
    if command == 'add':
        add_note()
    elif command == 'edit':
        edit_note()
    elif command == 'delete':
        delete_note()
    elif command == 'list':
        list_notes()
    elif command == 'exit':
        break
    else:
        print("Error")


