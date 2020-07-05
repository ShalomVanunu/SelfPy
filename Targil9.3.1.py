

def my_mp3_playlist(file_path):
    time_song = []
    all_song = []
    each_song = []
    dict_songs ={}
    dict_atritst = {}
    names_of_atrist = []
    input_file = open(file_path,'r').read() #loading the content of file
    songs_file = input_file.split('\n') # split with enter
    print('1',songs_file)
    for items in songs_file:
        each_song.append(items.split(';')) #split each song to words in string
    print('2',each_song)
    for i in each_song :
        dict_songs[i[0]] = i[2] #create dictionary with song name and time
    print('3',dict_songs)
    time_song = (sorted(dict_songs.items(),key = lambda kv:(kv[1], kv[0])))

    for i in each_song:
        names_of_atrist.append(i[1])
        dict_atritst[i[1]] = names_of_atrist.count(i[1])
    count_many = (sorted(dict_atritst.items(),key = lambda kv:(kv[1], kv[0])))
    print('The artist that show many time :', count_many[-1][0])
    print('the longest song is: ',time_song[-1][0])
    print('numbers of songs: ',len(songs_file))
    result = (time_song[-1][0],len(songs_file),count_many[-1][0])
    return (result)
  #  destination_file = open(r"C:\Users\Shalom\PycharmProjects\SelfPy\found.txt",'w')
   # destination_file.write(str(number))



def main():  # Call the function func
    print(my_mp3_playlist(r"C:\Users\Shalom\PycharmProjects\Selfpy\songs.txt"))

if __name__ == "__main__":
    main()