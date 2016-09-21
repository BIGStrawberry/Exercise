def pay(hourlyPay, hours):
    if (hours > 40):
        pay = (hours - 40) * hourlyPay * 1.5 + 40 * hourlyPay
        return pay
    else:
        return hourlyPay * hours

# print(pay(10, 35))
# print(pay(10, 45))

def abbrev(day):
    print(day[0: 2].capitalize())

# abbrev(input("Give me a day pls: "))
def average():
    userInput = input("Enter a sentence:")

    split = userInput.split()
    totalLength = 0

    for i in split:
        totalLength = totalLength + len(i)
        averageLength = totalLength / len(split)
    print(round(averageLength,1))
average()

