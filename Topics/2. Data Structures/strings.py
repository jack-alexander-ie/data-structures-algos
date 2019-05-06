# String Reversal
def string_reverser(our_string):
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """

    # TODO: Write your solution here

    reversed_string = ''

    i = len(our_string) - 1

    while i >= 0:
        reversed_string += our_string[i]
        i -= 1

    return reversed_string


# Test Cases
#print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
#print("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
#print("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")


def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """

    # TODO: Write your solution here

    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    # Edge case check
    if len(str1) > len(str2) or len(str2) > len(str1):
        return False

    str1_list = sorted([character for character in str1])
    str2_list = sorted([character for character in str2])

    matches = 0

    for index, character in enumerate(str1_list):

        if str1_list[index] == str2_list[index]:
            matches += 1
        else:
            return False

    if matches != len(str1):
        return False

    return True


# Test Cases
# print("Pass" if not (anagram_checker('water','waiter')) else "Fail")
# print("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
# print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
# print("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
# print("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")

def word_flipper(our_string):
    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """

    # TODO: Write your solution here
    # reversed_word = ''
    #
    # i = len(our_string) - 1
    #
    # words = []
    #
    # while i >= 0:
    #
    #     if i > 0 and our_string[i] != ' ':
    #         reversed_word += our_string[i]
    #         i -= 1
    #     elif i == 0:
    #         reversed_word += our_string[i]
    #         words.append(reversed_word)
    #         i -= 1
    #     else:
    #         words.append(reversed_word)
    #         reversed_word = ''
    #         i -= 1
    #
    # reversed_string = []
    #
    # for i in range(len(words)):
    #     reversed_string.append(words.pop())
    #
    # return ' '.join(reversed_string)

    # Their solution
    word_list = our_string.split(" ")

    for idx in range(len(word_list)):
        word_list[idx] = word_list[idx][::-1]

    return " ".join(word_list)

# Test Cases
# print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
# print("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
# print("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")


def hamming_distance(str1, str2):
    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """

    # TODO: Write your solution here
    # Edge case check
    if len(str1) != len(str2):
        return None

    count = 0
    for index in range(len(str1)):
        if str1[index] != str2[index]:
            count += 1

    if count is 0:
        return None

    return count

# Test Cases
print("Pass" if (10 == hamming_distance('ACTTGACCGGG','GATCCGGTACA')) else "Fail")
print("Pass" if  (1 == hamming_distance('shove','stove')) else "Fail")
print("Pass" if  (None == hamming_distance('Slot machines', 'Cash lost in me')) else "Fail")
print("Pass" if  (9 == hamming_distance('A gentleman','Elegant men')) else "Fail")
print("Pass" if  (2 == hamming_distance('0101010100011101','0101010100010001')) else "Fail")
