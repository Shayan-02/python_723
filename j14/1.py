
def count_ch(word:str)-> None:
    """
    Get a word and return count of each letter of that.

    Args:
        word (str): word that function count each letters of that


    """
    letters = list({ch for ch in word})
    # define letters
    letters.sort()
    # sort letters based on alphabet
    count = []
    # The number of occurrences of each letter
    for ch in letters:
        count.append(word.count(ch))
    # Creating a dictionary consisting of letters and their counts
    dic = dict(zip(letters, count))
    for i in dic:
        print(i, ":", dic[i])

    # call the function
print(count_ch("abbas"))
