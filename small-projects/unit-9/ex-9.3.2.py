def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r') as file:
        list_of_lines = file.readlines()

    if len(list_of_lines) < 3:
        list_of_lines += ['\n'] * (3 - len(list_of_lines))
        list_of_lines[2] = f"{new_song};Unknown;Unknown;\n"
    else:
        l = list_of_lines[2].split(';')
        singer, length = l[1], l[2]
        list_of_lines[2] = f"{new_song};{singer};{length};\n"

    with open(file_path, 'w') as file:
        file.writelines(list_of_lines)

    with open(file_path, 'r') as file:
        print(file.read())
