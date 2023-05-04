def my_mp3_playlist(file_path):
    with open(file_path, 'r') as file:
        songs_list = file.read().splitlines()

    song_list = [song.split(';') for song in songs_list]
    song_lengths = [song[2] for song in song_list]
    longest_song_index = song_lengths.index(max(song_lengths))
    longest_song_name = song_list[longest_song_index][0]
    performers = [song[1] for song in song_list]
    performer_count = {performer: performers.count(performer) for performer in set(performers)}
    most_common_performer = max(performer_count, key=performer_count.get)

    return longest_song_name, len(song_list), most_common_performer
