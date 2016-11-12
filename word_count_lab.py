def words(n):
    # words = n.split()
    # counts =dict()
    counts = {}
    for word in n.split():
        if word.isdigit():
            word = int(word)
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts