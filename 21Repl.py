import datetime

def add_note():
    note_text = input("Enter your note: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("note.txt", "a") as file:
        file.write(f"{timestamp}: {note_text}\n")
    print("Note added successfully!")

def list_notes():
    try:
        with open("note.txt", "r") as file:
            notes = file.readlines()
            if not notes:
                print("No notes available!")
            else:
                for note in notes:
                    print(note.strip())
    except FileNotFoundError:
        print("No notes found!!! Please add a note first.")
    except Exception as e:
        print(f"An error occurred while reading the notes: {e}")

def main():
    while True:
        print("\nNote Taking App Menu:")
        print("1.Add Note")
        print("2.List All Notes")
        print("3.Exit")

        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                add_note()
            elif choice == 2:
                list_notes()
            elif choice == 3:
                # open("note.txt", "w").close()
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


# add_note()
# list_notes()
main()