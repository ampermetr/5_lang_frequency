import os

if __name__ == '__main__':
    filepath = input('Введи путь к файлу')    
    os.system ("sed 's/[ ,./!@#$%^&*()№:;_-–]/\\n/g' " + filepath + " | tr -s '\n' | tr '[A-Z]' '[a-z]' | sort | uniq -c | sort -rn | head -10")
