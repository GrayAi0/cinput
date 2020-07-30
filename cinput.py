import sys, clr, colorama as color

color.init()

import System

class cinput:

    def __init__(self, words, color=True, ghostLetters=True):
        self.words = words
        self.color = color
        self.ghostLetters = ghostLetters



    def writeGostWords(self ,gword):
        print(color.Fore.LIGHTBLACK_EX, end='')
        for letter in gword:
            print(letter, end='', sep='\r')
        print(color.Fore.RESET, end='')

    def popstr(self ,word, lett):
        word = list(word)
        if len(word) == 0:
            return ''
        word.pop(lett)
        return ''.join(word)

    def clearfore(self, lens='a'):
        if lens == 'a':lens = len(max(self.words)) + 2
        for l in range(lens):
            sys.stdout.write(' ')
        for l in range(lens):
            sys.stdout.write('\b')

    def clearlast(self, enter):
        for l in range(len(enter)):
            sys.stdout.write('\b')
        for l in range(len(enter)):
            sys.stdout.write(' ')
        for l in range(len(enter)):
            sys.stdout.write('\b')

    def readline(self, msg='.cInput>'):
        print(msg, end=' ')
        enter = ''
        while True:
            key = System.Console.ReadKey()
            if key.Key == 13:
                break

            if key.Key == 8 and enter != '':
                sys.stdout.write(' ')
                sys.stdout.write('\b')
                self.clearfore()
                enter = self.popstr(enter, -1)
            elif key.Key == 8 and enter == '':
                self.clearlast(msg + ' ')
                print(msg, end=' ')

            if key.Key == 9:
                self.clearlast(msg + ' ')
                for k in range(8):
                    sys.stdout.write('\b')
                    sys.stdout.write(' ')
                    sys.stdout.write('\b')
                cwords = []
                for word in self.words:
                    if word.startswith(enter):
                        cwords.append(word)
                if len(cwords) == 1:
                    enter = cwords[0]
                    print(msg, enter, end='')
                elif len(cwords) > 1:
                    print(color.Fore.LIGHTBLUE_EX, end='')
                    for word in cwords:
                        print(word, end='    ')
                    print(color.Fore.RESET, end='')
                    print('\n' + msg, enter, end='')

            if key.Key == System.ConsoleKey.Escape:
                sys.stdout.write('\b')
                sys.stdout.write(' ')
                sys.stdout.write('\b')

            if key.Key not in [13, 8, 9, 39, 37, 38, 409, 39, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 121,
                               123, 91] and key.Key is not System.ConsoleKey.Escape:
                enter += key.KeyChar
            elif key.Key in [38, 39, 37, 40, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 12, 91]:
                sys.stdout.write('\b')
                sys.stdout.write(' ')
                sys.stdout.write('\b')
                continue
            elif key.Key in [8]:
                pass
            else:
                continue

            getword = False
            for word in self.words:
                if len(enter) < 1:
                    break
                if self.ghostLetters:
                    if word.startswith(enter):
                        self.clearfore()
                        self.writeGostWords(word.replace(enter, '', 1))
                        for l in range(len(word.replace(enter, '', 1))):
                            sys.stdout.write('\b')
                        getword = True
                        break

                elif self.color:
                    if word.startswith(enter):
                        getword = True

            if not getword and self.ghostLetters:
                self.clearfore()
            if not getword and self.color:
                print(color.Fore.RED, end='')
                self.clearlast(enter)
                sys.stdout.write(enter)
            elif getword and self.color:
                print(color.Fore.GREEN, end='')
                self.clearlast(enter)
                sys.stdout.write(enter)
        self.clearlast(msg + ' ' + enter)
        self.clearfore()
        print(color.Fore.RESET, end='')
        return enter



if __name__ == "__main__":
    cin = cinput(['print', 'ensure', 'start', 'stop', 'System', 'Random', 'random'])
    cin.readline()
