three_pigs_num = input("Enter three digits number please: ")
three_pigs_num = int(three_pigs_num)
pig_1 = three_pigs_num // 100
pig_2 = (three_pigs_num // 10) % 10
pig_3 = three_pigs_num % 10
total_bricks = pig_1 + pig_2 + pig_3
print("Totle number of bricks: ", total_bricks)
print("The average number of bricks: ", total_bricks // 3)
print("The number of remainder bricks: ", total_bricks % 3)
print("The number of remainder bricks is 0: ", total_bricks % 3 == 0)