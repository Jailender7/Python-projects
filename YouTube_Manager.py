import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def file_save_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)


def list_video(videos):
    print("\n")
    print("* " * 50)

    for index, video in enumerate(videos, start = 1):
        
        print(f"{index}. {video['name']}, {video['time']}")

    print("* " * 50)

def add_new_video(videos):
    title = input("Enter new video tile : ")
    duration = input("Enter duration of this video : ")

    videos.append({'name': title, 'time': duration})
    file_save_helper(videos)

def update_video_detail(videos):
    # printing all videos before to update
    list_video(videos)

    index = int(input("Enter S.No. to update video : "))

    if (1<= index <= len(videos) ) :
        title = input("Enter your title of video : ")
        duration = input("Enter new time duration of video : ")
        videos[index-1] = {'name': title, 'time': duration}
        file_save_helper(videos)
    else:
        print("Enter valid S.No. : ")


def delete_video(videos):
    # listing all video before delete
    list_video(videos)

    index = int(input("Enter video number to delete video : "))

    if (1 <= index <= len(videos)):
        del videos[index-1]
    else:
        print("Enter valid number : ")

def main() :

    videos = load_data()

    while(True) :

        print("\n Your YouTube Manager || Choose an option : ")
        print("1. List your all youTube videos : ")
        print("2. Add a new video in your YouTube feed : ")
        print("3. Update detail of a video : ")
        print("4. Delete a video from your feed : ")
        print("5. Exit : ")

        choice = input("Choose a number : ")

        match choice:
            case '1':
                list_video(videos)
            case '2':
                add_new_video(videos)
            case '3':
                update_video_detail(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Successfully completed. Thank you!")
                break
            case _:
                print("*" * 70)
                print("\n Sorry for your inconvenience, you choose wrong number. Try again! \n")
                print("*" * 70)

# Approach 1: to call main function or basic method to call main function
# main()


# Approach 2: to  call main function / This is industry based practice
if __name__ == "__main__":
    main()