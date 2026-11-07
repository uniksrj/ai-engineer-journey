"""
Day 2 — Python Practice
Goal: Practice functions, lists, dictionaries, loops,
exceptions, and type hints.
"""

def check_even_odd(number :int):
    if not number:
        return
    
    if number % 2 == 0:
        print("this is even")
    else:
        print("this is odd")


# check_even_odd(7)

def find_largest(numbers : list[int]):
    numbers.sort()
    lenValue = len(numbers)
    maxValue = 0
    for i in range(0, lenValue):
        if maxValue < numbers[i]:
            maxValue = numbers[i]

    return maxValue
    # return max(numbers)


# print(find_largest([20,40,10,5,60]))


def count_words(sentence : str) -> dict[str, int]:
    listSentence = sentence.split(" ")
    dictDetails = {}
    for word in listSentence:
        if word in dictDetails:
            dictDetails[word] += 1
        else:
            dictDetails[word] = 1  

    return dictDetails     
    # print(listSentence)

# print(count_words("ai is powerful and ai is useful"))


def reverse_string(string : str) -> str:
    reveredText = []
    for word in string:
        reveredText.insert(0, word)
    return "".join(reveredText)

# print(reverse_string("python"))


def is_palindrome(string : str) -> bool:
    reveredText = []
    for word in string:
        reveredText.insert(0, word)
    reveresdText = "".join(reveredText)
    if reveresdText.lower() == string.lower():
        return True
    
    return False

# print(is_palindrome("Level"))  
# print(is_palindrome("python")) 


def top_student(marks :dict[str, int]) -> str:
    if not marks:
        return ""

    maxVal = float("-inf") 
    top_student = ""
    for value in marks:
        if maxVal < marks[value]:
            maxVal = marks[value]
            top_student = value 

    return top_student

    # pass

students = {
    "Suraj": 85,
    "Ravi": 92,
    "Neha": 78,
}

# print(top_student(students))  # Ravi


def remove_duplicates(numbers : list[int]) -> list[int]:
    return list(set(numbers))
    

print(remove_duplicates([1, 2, 2, 3, 1, 4]))  # [1, 2, 3, 4]


def main() -> None:
    print(check_even_odd(4))
    print(check_even_odd(7))

    print(find_largest([3, 17, 8, 42, 5]))

    print(count_words("ai is powerful and ai is useful"))

    # print(reverse_text("python"))

    # print(sum_even_numbers([1, 2, 3, 4, 5, 6]))

    # print(is_palindrome("Level"))
    # print(is_palindrome("python"))

    # students = {
    #     "Suraj": 85,
    #     "Ravi": 92,
    #     "Neha": 78,
    # }
    # print(top_student(students))

    # print(celsius_to_fahrenheit(0))
    # print(celsius_to_fahrenheit(37))

    # print(remove_duplicates([1, 2, 2, 3, 1, 4]))

    # number = get_number()
    # print(f"You entered: {number}")


if __name__ == "__main__":
    main()