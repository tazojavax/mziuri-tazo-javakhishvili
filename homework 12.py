#  #1
# while True:
#      try:
#     num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
#         num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
#
#          result = num1 / num2
#         print("გაყოფის შედეგია:", result)
#        break
#
#     except ValueError:
#         print("შეცდომა! გთხოვთ შეიყვანოთ მხოლოდ რიცხვები.")
#
#     except ZeroDivisionError:
#         print("შეცდომა! ნულზე გაყოფა შეუძლებელია.")
#
#  #2
#
#  def divide_numbers(a, b):
#    try:
#        result = a / b
#        return result
#    except ZeroDivisionError:
#         return "შეცდომა: ნულზე გაყოფა შეუძლებელია."
#      except TypeError:
#         return "შეცდომა: გადაეცა არასწორი ტიპის მონაცემი."
#
#
#print(divide_numbers(10, 2))
#print(divide_numbers(10, 0))
# print(divide_numbers(10, "a"))
#
#3
# my_list = [10, 20, 30, 40, 50]
#
# try:
#     index = int(input("შეიყვანეთ ინდექსი (0-4): "))
#     print("არჩეული ელემენტია:", my_list[index])
#
# except IndexError:
#     print("შეცდომა! ასეთი ინდექსი არ არსებობს სიაში.")
#
# except ValueError:
#     print("შეცდომა! გთხოვთ შეიყვანოთ მხოლოდ მთელი რიცხვი.")
#4

# try:
#     file = open("myresult.txt", "r")
#     content = file.read()
#     print(content)
#     file.close()
# except FileNotFoundError:
#     print("შეცდომა: ფაილი 'myresult.txt' არ არსებობს.")
# #5
#
    # print("გაუთვალისწინებელი შეცდომა:", e)