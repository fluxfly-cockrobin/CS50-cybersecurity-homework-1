
for i in range(26):
    for letter in "Otkz D zvmizy v amzz kjdio! di ocz wjs wzgjr.":
        if (letter.isalpha()):
            if(chr(ord(letter)+int(i)).isalpha()):
                print(chr(ord(letter)+int(i)), end="")
            else:
                print(chr((ord(letter)+int(i))%122+96), end="")
        else:
            print(letter, end='')
    print()