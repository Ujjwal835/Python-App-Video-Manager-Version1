import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            # will load the file nd convert into json
            test= json.load(file)
            return test
    except FileNotFoundError:
        return []
        
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
    
def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index,video in enumerate(videos,start=1):    
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
    print("*"*70)
def add_video(videos):
    name=input("Enter Video Name: ")
    time=input("Enter Video Time: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)
    print("***** Video Added Successfully *****")    

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter The video Number to update: "))
    if 1<=index<=len(videos):
        name=input("Enter the new Video Name: ")
        time=input("Enter the new Video Time: ")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
        print("***** Details Updated Successfully *****")    
    else:
        print("Invalid Index Selected !! ")
def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter The video Number to be Deleted: "))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("***** Video Deleted Successfully *****")    
    else:
        print("Invalid Video Index Selected !!")
def main():
    videos=load_data()
    # print(videos)
    while True:
        print("\n\t\tYoutube Manager | Choose an Option")
        print("\n")
        print("1. List all Youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video  ")
        print("5. Exit the app  ")
        choice=input("Enter Your Choice ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)        
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice !!! ")
                
if __name__== "__main__":
    main()