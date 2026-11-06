secret_code = input("Enter a secret code ")
length_of_code = len(secret_code)
def main():
    global secret_code
    if length_of_code == 1:
            secret_code = int(secret_code)
    else:
        str(secret_code)
    print(type(secret_code))
    print(F"The code is {length_of_code} character long.")
    secret_code = str(secret_code)
    first_character = secret_code[0]
    last_character = secret_code[-1]
    print(F"The first character is {first_character} and the last character is {last_character}")
    if length_of_code > 2:
            if length_of_code % 2 != 0:
                print(F"{secret_code[length_of_code//2]}")
            else:
                mid = length_of_code // 2
                print(f"{secret_code[mid - 1 : mid + 1]}")



if __name__ == '__main__':
    main()
