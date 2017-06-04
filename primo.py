def primo(x):
    fator = 2
    while(x % fator != 0) and (fator <=x/2):
        fator = fator + 1
        print(fator)
    if (x % fator != 0) or (x == 2):
        return True
    else:
        return False

print(primo(3))
