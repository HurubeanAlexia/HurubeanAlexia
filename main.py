import sys


def get_largest_prime_below(n):
    """
    returneaza ultimul nr prim mai mic decat cel dat
    :param n: un nr intreg
    :return: numarul cautat
    """
    for i in range(n - 1, 2, -1):
        if is_Prime(i):
            return i

def is_Prime(n):
    """
    verifica daca un nr este prim
    :param n: un nr intreg
    :return: True, daca nr este prim. False, daca nr nu este prim
    """
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def test_is_Prime():
    assert is_Prime(4) == False
    assert is_Prime(7) == True
    assert is_Prime(13) == True
    assert is_Prime(6886) == False

def test_get_largest_prime_below():
    assert get_largest_prime_below(60) == 59
    assert get_largest_prime_below(8) == 7
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(34) == 31
    assert get_largest_prime_below(94) == 89

def is_palindrome(n):
    """
    verifica daca un nr este palindrom
    :param n: un nr intreg
    :return: True, daca nr este palindrom, False in caz contrar
    """
    inverse = 0
    copy = n
    while copy > 0:
        inverse = inverse * 10 + copy % 10
        copy = copy // 10
    if inverse == n:
        return True
    else:
        return False

def main():
    test_get_largest_prime_below()
    test_is_Prime()
    print("Testele au trecut cu succes")
    while True:
        print("1. Ultimul nr prim")
        print("2. Palindrom")
        print("3. Iesire")
        optiune = input("Alege optiunea: ")
        if optiune == '1':
            n = int(input('Dati numarul n: '))
            valoare = get_largest_prime_below(n)
            print(f'numarul prim cautat este {valoare}')
        elif optiune == '2':
            n = int(input('Dati numarul n: '))
            if is_palindrome(n):
                print('Numarul este palindrom')
            elif not is_palindrome(n):
                print('Numarul nu este palindrom')
        elif optiune == '3':
            sys.exit()
        else:
            print("optiune invalida")

main()
