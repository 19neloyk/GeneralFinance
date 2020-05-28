def frequencyFinder(article):
    article = str(article)
    word = ''
    arrayOfWords = []
    disWorFrequencies = []

    for element in article:
        if element in ('.',' ',',','(',')'):
            if len(arrayOfWords) == 0:
                arrayOfWords.append(word)
                disWorFrequencies.append(1)
                word = ''
            for index in range(0,len(arrayOfWords)):
                if word == arrayOfWords[index]:
                    disWorFrequencies[index] += 1
                    word = ''
                    break;
                elif index == len(arrayOfWords)-1:
                    arrayOfWords.append(word)
                    disWorFrequencies.append(1)
                    word = ''
        else:
            word += element

    index = 0
    while index < len(arrayOfWords):
        for element in ['','the', 'to', 'a', 'and', 'in', 'as']:
            if element == arrayOfWords[index]:
                del arrayOfWords[index]
                del disWorFrequencies[index]
        index = index +1

    descendingArray = []
    descendingWordFrequencies = []

    for index in range(0,len(arrayOfWords)):
        holderPosition = 0
        for position in range(0,len(arrayOfWords)):
            if disWorFrequencies[position] > disWorFrequencies[holderPosition]:
                holderPosition = position
        descendingArray.append(arrayOfWords[holderPosition])
        descendingWordFrequencies.append(disWorFrequencies[holderPosition])
        del arrayOfWords[holderPosition]
        del disWorFrequencies[holderPosition]

    for index in range(0, len(descendingArray)):
        spaces = 17 - len(descendingArray[index])
        print((descendingArray[index]) + spaces*' ' + str(descendingWordFrequencies[index]))

frequencyFinder('')
