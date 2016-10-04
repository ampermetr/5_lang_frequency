import os

if __name__ == '__main__':
    filepath = input('Введи путь к файлу')
    os.system ("cat " + filepath + " | tr ' ' '\n' | sort | uniq -c | sort -rn | head -10")
