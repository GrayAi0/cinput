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

import Exceptions
from tools import *



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




        self.words = list(dict.fromkeys(words))
        self.color = color
        self.ghostLetters = ghostLetters
        self.readenter = readenter

    def Help(self):
        return help(cinput)

    def readline(self,
                 msg='.cInput>'):
        '''
        :arg msg: this message will view behind the user input
        :return:str user input
        '''
        if len(self.words) < 1:
            raise Exceptions.EmptylistError('can\'t continue with empty list')
        print(msg, end=' ')
        enter = ''
        getword = False
        while True:
            try:
                key = ReadKey()
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
                clearfore(wordslist=self.words)
                enter = popstr(enter, -1)
            elif key.Key == 8 and enter == '':
                clearlast(msg + ' ')
                print(msg, end=' ')

            if key.Key == 9:
                clearlast(msg + ' ')
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
                                clearfore(wordslist=self.words)
                                writeGostWords(word.replace(enter, '', 1))
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
                        clearfore(wordslist=self.words)
                        writeGostWords(word.replace(enter, '', 1))
                        sys.stdout.write('\b' *
                                         len(word.replace(enter, '', 1)))
                        getword = True
                        break

                elif self.color:
                    if word.startswith(enter):
                        getword = True

            if not getword and self.ghostLetters:
                clearfore(wordslist=self.words)
            if not getword and self.color:
                print(color.Fore.RED, end='')
                clearlast(enter)
                sys.stdout.write(enter)
                print(color.Fore.RESET, end='')
            elif getword and self.color:
                print(color.Fore.GREEN, end='')
                self.clearlast(enter)
                sys.stdout.write(enter)
                print(color.Fore.RESET, end='')

        clearlast(msg + ' ' + enter)
        clearfore(wordslist=self.words)
        print(color.Fore.RESET, end='')
        return enter
    def readPassword(self, msg, privatelen='o', minlens=8, maxlens=15):
        '''
        :arg msg: This message will view behind the user input

        :arg privatelen: This letter will appear instead of any letter the user writes

        :arg minlens: If user letters under this number he cant prees enter

        :arg maxlens: If user letters more this number he cant write more

        :return:str user password input
        '''
        print(msg, end=' ')
        enter = ''
        while True:
            try:
                key = ReadKey()
            except KeyboardInterrupt:
                exit(2)
            except:
                print('WARN:This console does not accept this command WARN:"YOUR PASSWORD IS NOT SAVE NOW"')
                return input(msg + ' ')

            if key.Key == 13:
                if len(enter) <= maxlens and len(enter) >= minlens:
                    break
                else:
                    if len(enter) <= maxlens:
                        if privatelen != '':
                            clearlast(enter)
                        print(msg,
                              color.Fore.RED + len(enter) * privatelen,
                              end=color.Fore.RESET)
                    else:
                        if privatelen != '':
                            clearlast(enter)
                        print(msg,
                              color.Fore.RED + maxlens * privatelen,
                              end=color.Fore.RESET)

            if key.Key == 8 and enter != '':
                sys.stdout.write(' ')
                sys.stdout.write('\b')
                enter = popstr(enter, -1)
            elif key.Key == 8 and enter == '':
                clearlast(msg + ' ')
                print(msg, end=' ')

            if key.Key == 9:
                for _ in range(8):
                    sys.stdout.write('\b')
                    sys.stdout.write(' ')
                    sys.stdout.write('\b')

            if key.Key == System.ConsoleKey.Escape:
                sys.stdout.write('\b')
                sys.stdout.write(' ')
                sys.stdout.write('\b')


            if key.Key not in [
                    13, 8, 9, 39, 37, 38, 409, 39, 112, 113, 114, 115, 116,
                    117, 118, 119, 120, 121, 121, 123, 91
            ] and key.Key is not System.ConsoleKey.Escape and len(enter) < maxlens:
                enter += key.KeyChar
            elif key.Key in [
                    38, 39, 37, 40, 112, 113, 114, 115, 116, 117, 118, 119,
                    120, 121, 12, 91
            ]:
                sys.stdout.write('\b')
                sys.stdout.write(' ')
                sys.stdout.write('\b')

            elif key.Key in [8]:
                pass

            if len(enter) >= minlens and len(enter) < maxlens and self.color:
                print(color.Fore.GREEN, end='')
                if privatelen != '':
                    clearlast(' ' + enter)
                sys.stdout.write(' ' + (len(enter)  * privatelen))
                print(color.Fore.RESET, end='')

            elif len(enter) < minlens and self.color:
                print(color.Fore.YELLOW, end='')
                if privatelen != '':
                    clearlast(' ' + enter)
                sys.stdout.write(' ' + (len(enter)  * privatelen))
                print(color.Fore.RESET, end='')
            if len(enter) >= maxlens:
                print('\b ', end='\b')

        clearlast(msg + ' ' + enter)
        print(color.Fore.RESET, end='')
        return enter


def LineExample():
    cin = cinput(['print', 'ensure', 'start', 'stop', 'System', 'Random', 'random'])
    result = cin.readline('.cInput>')
    print('result is:', result)

def PassExample():
    Input = cinput()
    read = Input.readPassword('Enter your password:', privatelen='*', minlens=8, maxlens=15)
    print('Your enter password:', read)




if __name__ == "__main__":
    PassExample()
