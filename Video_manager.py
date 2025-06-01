import sqlite3

conn = sqlite3.connect('video_database.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS Videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL, 
               time TEXT NOT NULL)
''')

def list_all_video():
    cursor.execute("SELECT * FROM Videos")
    print("\n")
    print("*"*50)
    
    for row in cursor.fetchall():
        print(row)

    print("*"*50)

def add_video(name, time):
    cursor.execute("INSERT INTO Videos (name, time) VALUES(?,?)", (name, time))
    conn.commit()

def update_video(video_id,new_name, new_time):
    cursor.execute("UPDATE Videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id) )
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM Videos WHERE id=?", (video_id,))
    conn.commit()

def main():
    while True:
        print("\n Your Video Manager Database | choose an option frow below: ")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update video")

        print("4. Delete video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_video()
        
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        
        elif choice == '3':
            video_id = input("Enter video id you want to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id, name, time)

        elif choice == '4':
            video_id = input("Enter video id to delete: ")
            delete_video(video_id)

        elif choice == '5':
            break

        else:
            print("Invalid Choice")

    conn.close()
if __name__  == "__main__":
    main()
