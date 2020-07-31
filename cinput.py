import sys, clr, colorama as color
# --------------------------------
#
# cinput v1.0
#
# p1-words: List of words like ['command1', 'testcommand']
#
# p2-color: If entered word not in words list then will be colored to red or will be to green
#
# p3-ghostLetters: The entered word will be completed if is in words list
#
# p4-redenter: If word not in list and user press enter nothing will happen
#
# --------------------------------
color.init()
import System


class EmptylistError(Exception):
    '''
    :return:self if words list is empty this error will be threw
    '''
    pass


class cinput:
    def __init__(self,
                 words=[],
                 color=True,
                 ghostLetters=True,
                 readenter=True):
        '''
         :arg words: List of words like ['command1', 'testcommand']

         :arg color: If entered word not in words list then will be colored to red or will be to green

         :arg ghostLetters: The entered word will be completed if is in words list

         :arg redenter: If word not in list and user press enter nothing will happen

         :return:object self
        '''



        if len(words) < 1:
            raise EmptylistError('can\'t continue with empty list')
        self.words = list(dict.fromkeys(words))
        self.color = color
        self.ghostLetters = ghostLetters
        self.readenter = readenter

    def Help(self):
        return help(cinput)

    def writeGostWords(self,
                       gword):
        '''
        :param gword: This word will write as hidden
        :return:None
        '''
        print(color.Fore.LIGHTBLACK_EX, end='')
        for letter in gword:
            print(letter, end='', sep='\r')
        print(color.Fore.RESET, end='')

    def popstr(self,
               word,
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

    def clearfore(self,
                  lens='a'):
        '''
        :param lens: If the lens is 'a', then it will take the most value from the list in terms of letters or write the word you want to take amount the letters from it
        :return: None
        '''
        if lens == 'a': lens = len(max(self.words)) + 2
        sys.stdout.write(' ' * (lens))
        sys.stdout.write('\b' * (lens))

    def clearlast(self,
                  enter):
        '''
        :param enter: This will delete the pre-letter index
        :return: None
        '''
        sys.stdout.write('\b' * (len(enter)))
        sys.stdout.write(' ' * (len(enter)))
        sys.stdout.write('\b' * (len(enter)))

    def readline(self,
                 msg='.cInput>'):
        '''
        :arg msg: this message will view behind the user input
        :return:str user input
        '''
        print(msg, end=' ')
        enter = ''
        getword = False
        while True:
            try:
                key = System.Console.ReadKey()
            except:
                print('ERROR:This console does not accept this command')
                return input(msg + ' ')

            if key.Key == 13:
                if self.readenter and enter in self.words:
                    break
                elif not self.readenter:
                    break
                else:
                    if getword:
                        print(msg,
                              color.Fore.GREEN + enter,
                              end=color.Fore.RESET)
                    else:
                        print(msg,
                              color.Fore.RED + enter,
                              end=color.Fore.RESET)

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
                for _ in range(8):
                    sys.stdout.write('\b')
                    sys.stdout.write(' ')
                    sys.stdout.write('\b')
                del _
                cwords = []
                for word in self.words:
                    if word.startswith(enter):
                        cwords.append(word)
                if len(cwords) == 1:
                    enter = cwords[0]
                    print(msg, color.Fore.GREEN + enter, end=color.Fore.RESET)
                elif len(cwords) > 1:
                    print(color.Fore.LIGHTBLUE_EX, end='')
                    for word in cwords:
                        print(word, end=' ' * 4)
                    print(color.Fore.RESET, end='')
                    print('\n' + msg,
                          color.Fore.GREEN + enter,
                          end=color.Fore.RESET)
                    if self.ghostLetters:
                        for word in self.words:
                            if word.startswith(enter):
                                self.clearfore()
                                self.writeGostWords(word.replace(enter, '', 1))
                                sys.stdout.write(
                                    '\b' * len(word.replace(enter, '', 1)))
                                break
                else:
                    print(msg, color.Fore.RED + enter, end=color.Fore.RESET)

            if key.Key == System.ConsoleKey.Escape:
                sys.stdout.write('\b')
                sys.stdout.write(' ')
                sys.stdout.write('\b')

            if key.Key not in [
                    13, 8, 9, 39, 37, 38, 409, 39, 112, 113, 114, 115, 116,
                    117, 118, 119, 120, 121, 121, 123, 91
            ] and key.Key is not System.ConsoleKey.Escape:
                enter += key.KeyChar
            elif key.Key in [
                    38, 39, 37, 40, 112, 113, 114, 115, 116, 117, 118, 119,
                    120, 121, 12, 91
            ]:
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
                        sys.stdout.write('\b' *
                                         len(word.replace(enter, '', 1)))
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
                print(color.Fore.RESET, end='')
            elif getword and self.color:
                print(color.Fore.GREEN, end='')
                self.clearlast(enter)
                sys.stdout.write(enter)
                print(color.Fore.RESET, end='')

        self.clearlast(msg + ' ' + enter)
        self.clearfore()
        print(color.Fore.RESET, end='')
        return enter


if __name__ == "__main__":
    cin = cinput(['print', 'ensure', 'start', 'stop', 'System', 'Random', 'random'])
    result = cin.readline('.cInput>')
    print('result is:', result)