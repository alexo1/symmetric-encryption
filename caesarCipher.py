#s = 'foobar';
s = 'hello from the other side'

def encrypt(letter):
    if letter == 'a':
        return 'b';
    if letter == 'b':
        return 'c';
    if letter == 'c':
        return 'd';
    if letter == 'd':
        return 'e';
    if letter == 'e':
        return 'f';
    if letter == 'f':
        return 'g';
    if letter == 'g':
        return 'h';
    if letter == 'h':
        return 'i';
    if letter == 'i':
        return 'j';
    if letter == 'j':
        return 'k';
    if letter == 'k':
        return 'l';
    if letter == 'l':
        return 'm';
    if letter == 'm':
        return 'n';
    if letter == 'n':
        return 'o';
    if letter == 'o':
        return 'p';
    if letter == 'p':
        return 'q';
    if letter == 'q':
        return 's';
    if letter == 'r':
        return 'r'
    if letter == 's':
        return 't';
    if letter == 't':
        return 'u';
    if letter == 'u':
        return 'v';
    if letter == 'v':
        return 'w';
    if letter == 'w':
        return 'x';
    if letter == 'x':
        return 'y';
    if letter == 'y':
        return 'z';
    if letter == 'z':
        return 'a';
    if letter == ' ':
        return ' '
    # if letter == 'b':
    #     return 'c'
    # if letter == 'b':
    #     return 'q'
    # if letter == 'a':
    #     return 'z'
    # if letter == 'r':
    #     return 'w'
    # if letter == 'f':
    #     return 'a'
    # if letter == 'o':
    #     return 'c'
    # if letter == 'b':
    #     return 'q'
    # if letter == 'a':
    #     return 'z'
    # if letter == 'r':
    #     return 'w'
    # if letter == 'f':
    #     return 'a'
    # if letter == 'o':
    #     return 'c'
    # if letter == 'b':
    #     return 'q'
    # if letter == 'a':
    #     return 'z'
    # if letter == 'r':
    #     return 'w'


def decrypt(letter):
    if letter == 'b':
        return 'a';
    if letter == 'c':
        return 'b';
    if letter == 'd':
        return 'c';
    if letter == 'e':
        return 'd';
    if letter == 'f':
        return 'e';
    if letter == 'g':
        return 'f';
    if letter == 'h':
        return 'g';
    if letter == 'i':
        return 'h';
    if letter == 'j':
        return 'i';
    if letter == 'k':
        return 'j';
    if letter == 'l':
        return 'k';
    if letter == 'm':
        return 'l';
    if letter == 'n':
        return 'm';
    if letter == 'o':
        return 'n';
    if letter == 'p':
        return 'o';
    if letter == 'q':
        return 'p';
    if letter == 's':
        return 'q';
    if letter == 'r':
        return 'r'
    if letter == 't':
        return 's';
    if letter == 'u':
        return 't';
    if letter == 'v':
        return 'u';
    if letter == 'w':
        return 'v';
    if letter == 'x':
        return 'w';
    if letter == 'y':
        return 'x';
    if letter == 'z':
        return 'y';
    if letter == 'a':
        return 'z';
    if letter == ' ':
        return ' '


def Main():
    #print len(s)
    #prompt user
    s = raw_input("Enter text to encrypt\n")
    b=[]
    for letter in s:
        #print (letter)
        a = encrypt(letter)
        #print (a), # print on one line
        b.append(a)
    print "\n"
    for letter in b:
        print (letter),
    #print "\nprinting b "+ str(b)

    c=[]
    print "\n\ndecrypt\n"
    for letter in b:
        c = decrypt(letter)
        print (c),
    print "\n"



if __name__ == '__main__':
    Main()
