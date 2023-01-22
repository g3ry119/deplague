filename = input("filename -> ")
fileval = ""

import re
def readf(val):
    match = re.search(r"\"\"\.join\(chr\(ord\(t\)-(\d+)\)", val)
    
    if match:
        number = match.group(1)
        
        return number
    else:
        return 0

def readx(val):
    match = re.search(r"'''(.*?)'''", val, re.DOTALL)
    if match:
        my_string = match.group(1)
        return (my_string)
    else:
        return ("f3acad9a/f3acad9a")


try:
    with open(file=filename, mode='r') as f:
        fileval = f.read()
        f.close()
except FileNotFoundError:
    print("[-] File was not found")

key = int(readf(fileval))

_sparkle = (readx(fileval))

from binascii import unhexlify
_lines_sep_ = "/"
split = _sparkle.split(_lines_sep_)

fkyrie = ""

for line in split:
    fkyrie += (unhexlify(line).decode())

class Make():
    strings = "abcdefghijklmnopqrstuvwxyz0123456789"

class Kyrie():

    def encrypt(e: str, key: str) -> str:
        e1 = Kyrie._ekyrie(e)
        return Kyrie._encrypt(e1, key=key)

    def decrypt(e: str, key: str) -> str:
        text = Kyrie._decrypt(e, key=key)
        return Kyrie._dkyrie(text)

    def _ekyrie(text: str) -> str:

        r = ""
        for a in text:
            if a in Make.strings:
                a = Make.strings[Make.strings.index(a)-1]
            r += a
        return r

    def _dkyrie(text: str) -> str:
        r = ""
        for a in text:
            if a in Make.strings:
                i = Make.strings.index(a)+1
                if i >= len(Make.strings):
                    i = 0
                a = Make.strings[i]
            r += a
        return r

    def _encrypt(text: str, key: str = None) -> str:
        if type(key) == str:
            key = sum(ord(i) for i in key)
        t = [chr(ord(t)+key)if t != "\n" else "ζ" for t in text]
        return "".join(t)

    def _decrypt(text: str, key: str = None) -> str:
        if type(key) == str:
            key = sum(ord(i) for i in key)
        return "".join(chr(ord(t)-key) if t != "ζ" else "\n" for t in text)


decrypted = Kyrie.decrypt(fkyrie, key)

print(decrypted)


print(("\n"*2)+"Press ENTER to exit...")
input()
