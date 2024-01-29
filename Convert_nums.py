def main():
    phrase = input("Enter your phrase: ")
    # Spit the phrase in a list of words
    broken_phrase = phrase.split(' ')
    # Change the numbers to words
    result = text2int(broken_phrase)
    print(result)


def text2int(broken_phrase):
    # Make lists of words to have a 'dictionary'
    units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
    ]

    decades = {
        90: 'ninety', 80: 'eighty', 70: 'seventy', 60: 'sixty',
        50: 'fifty', 40: 'forty', 30: 'thirty', 20: 'twenty'
    }

    new_phrase = []

    # Loop through each word in the phrase and see if it is a number
    for word in broken_phrase:
        if word.isnumeric():
            # If it is, convert it to an int so we can work with it
            word = int(word)
            if word >= 20:
                # If it's greater than 19, then we need something from the tens dictionary
                for num in decades.keys():
                    # Loop through to find the tens that want
                    if word >= num:
                        new_phrase.append(decades[num])
                        word -= num
                        # If there are units needed, then add them now
                        if word != 0:
                            new_phrase.append(units[word])
                        break
            # If it doesn't need a tens, then just use from the units list
            else:
                new_phrase.append(units[word])
        # If it isn't a number then just add it to the phrase as is
        else:
            new_phrase.append(word)

    # Return the phrase joined together with spaces between
    return ' '.join(new_phrase)


main()
