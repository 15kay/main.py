'''this program ask the user to enter the number of weeks thye would like to attend  afternoon lesson and also ask them to choose a course using codes'''
print("Welcome to KG afternoon lessons")
numweeks = int(input("ENTER THE NUMBER OF WEEKS YOU WILL ATTEND: "))
print("We only offer two courses A and B ")
print("Course code A = Computer science")
print("Course code B = Networking")
Code = str(input("Choose course code(A or B): "))
if Code != "A" or "B":    # it is suppose to only accept A and B, other than that it should display "invalid input"
    print("Invalid input")
    exit()

if Code == "A":
    price = 234 * numweeks
    print("The total price for course code", Code, "is R",price)
else:
    price = 287.5 * numweeks
    print("The total price for course code", Code, "is R",price)
exit()
