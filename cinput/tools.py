import colorama as color
import sys, clr
import System

def writeGostWords(gword):
    '''
    :param gword: This word will write as hidden
    :return:None
    '''
    print(color.Fore.LIGHTBLACK_EX, end='')
    for letter in gword:
        print(letter, end='', sep='\r')
    print(color.Fore.RESET, end='')
def popstr(word,
           lett):
    '''
    :param word: This word you want to clear the letter from it
    :param lett: This is a letter index that you want to delete it
    :return: str new word
    '''
    word = list(word)
    if len(word) == 0:
        return ''
    word.pop(lett)
    return ''.join(word)
def clearfore(lens='a', wordslist=[]):
    '''
    :param lens: If the lens is 'a', then it will take the most value from the list in terms of letters or write the word you want to take amount the letters from it
    :return: None
    '''
    print(wordslist)
    if lens == 'a': lens = len(max(wordslist)) + 2
    sys.stdout.write(' ' * (lens))
    sys.stdout.write('\b' * (lens))
def clearlast(enter):
    '''
    :param enter: This will delete the pre-letter index
    :return: None
    '''
    sys.stdout.write('\b' * (len(enter)))
    sys.stdout.write(' ' * (len(enter)))
    sys.stdout.write('\b' * (len(enter)))

def ReadKey():
    return System.Console.ReadKey()