while True:
    print("\nMENU")
    print("1. Count the frequency of words in a sentence")
    print("2. Count the frequency of letters in a word")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        sentence = input("Enter a sentence: ")
        words = sentence.split()  
        word_frequency = {}

        for word in words:
            word = word.lower()  
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

        print("Word frequency:", word_frequency)

    elif choice == '2':
        word = input("Enter a word: ")
        letter_frequency = {}  

        for letter in word:
            if letter in letter_frequency:
                letter_frequency[letter] += 1
            else:
                letter_frequency[letter] = 1

        print("Letter frequency:", letter_frequency)

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
