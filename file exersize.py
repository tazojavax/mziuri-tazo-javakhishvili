# 1
# file = open("text.txt", "w")
#
# file.write("hello world")
#
# file.close()

#2

# file = open("text.txt", "r")
#
# content = file.read()
#
# print("ფაილის შიგთავსი:")
#
# print(content)
#
# characters_count = len(content)
#
# print("სიმბოლოების რაოდენობა:", characters_count)
#
# file.close()

#3
# file = open("example.txt", "a")
#
# file.write("\nThis text is appended to the file.")
#
# file.close()

#4
#
# source_file = open("source.txt", "r", encoding="utf-8")
#
# content = source_file.read()
#
# source_file.close()
#
# target_file = open("target.txt", "w", encoding="utf-8")
#
# target_file.write(content)
#
# target_file.close()[]

 #5
#
# file1 = open("file1.txt", "r")
# content1 = file1.read()
# file1.close()
#
# file2 = open("file2.txt", "r")
# content2 = file2.read()
# file2.close()
#
# merged_file = open("merged.txt", "w")
# merged_file.write(content1)
# merged_file.write("\n")
# merged_file.write(content2)
# merged_file.close()

#6
#
#
# file = open("text.txt", "r", encoding="utf-8")
#
# content = file.read()
#
# file.close()
#
# print(content.upper())


#7
#
# with open("data.txt", "w") as file:
#     while True:
#         data = input("შეიყვანეთ ინფორმაცია (შეჩერება 0-ით): ")
#         if data == "0":
#             break
#         file.write(data + "\n")
#8
# with open("input.txt", "r") as infile:
#     lines = infile.readlines()
#
# one_line = " ".join(line.strip() for line in lines)
#
# with open("output.txt", "w") as outfile:
#     outfile.write(one_line)