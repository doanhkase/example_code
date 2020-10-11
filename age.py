# Chương trình nhập tuổi đúng quy định: 

while True:
    print('Nhập tuổi của bạn:')
    age = input()
    try:
        age = int(age)
    except:
        print('Vui lòng nhập vào một số. \n')
        continue
    if age < 1:
        print('Bạn ơi, hãy nhận số dương nhé. \n')
        continue
    break
print('Tuổi của bạn là: ' + str(age))
