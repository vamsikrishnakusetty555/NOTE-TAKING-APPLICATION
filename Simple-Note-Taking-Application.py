import os

notes_directory = "notes"  # Directory to store notes

def create_directory():
    if not os.path.exists(notes_directory):
        os.makedirs(notes_directory)

def add_note():
    create_directory()

    title = input("Enter note title: ")
    content = input("Enter note content: ")

    note_filename = title.lower().replace(" ", "_") + ".txt"
    note_path = os.path.join(notes_directory, note_filename)

    with open(note_path, "w") as file:
        file.write(content)

    print("Note added successfully!")

def view_note():
    create_directory()

    title = input("Enter note title: ")

    note_filename = title.lower().replace(" ", "_") + ".txt"
    note_path = os.path.join(notes_directory, note_filename)

    if os.path.exists(note_path):
        with open(note_path, "r") as file:
            content = file.read()
            print(f"Title: {title}")
            print(f"Content:\n{content}")
    else:
        print("Note not found!")

def list_notes():
    create_directory()

    note_files = os.listdir(notes_directory)

    if not note_files:
        print("No notes found!")
    else:
        print("Available notes:")
        for note_file in note_files:
            note_title = note_file[:-4].replace("_", " ").title()
            print(f"- {note_title}")

def main():
    while True:
        print("\n===== Note-Taking Application =====")
        print("1. Add Note")
        print("2. View Note")
        print("3. List Notes")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_note()
        elif choice == '2':
            view_note()
        elif choice == '3':
            list_notes()
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
