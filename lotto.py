
import random as rn
import numpy as np

# 숫자를 담을 배열
numarray = []
# 로또 배열 6개 숫자가 정해져 있으므로 굳이 가변으로 만들 필요 없음
# (배열 크기가 크지 않은 것도 이유에 포함)
lotto = [0,0,0,0,0,0]
# 뽑혀진 숫자
now_number = 0

#  insertnumber() : 최초 1 ~ 45 까지 숫자를 변수에 담는다
def insertnumber () :
    for i in range(1,46):
        numarray.append(i)

# 로또번호 입력 Function
def insetlotto(i):
    try:
        # 현재 배열의 크기를 구한다
        len = (numarray.__len__()) - 1
        # 배열 크기까지 범위 내애서 난수를 생성한다
        # (인덱스를 추출하기 위해)
        idx = rn.randint(0, len)
        # 추출된 순번의 숫자를 구해서 로또 배열에 삽입한다
        now_number = numarray[idx]
        # 중복된 번호가 있을 경우 다시 번호 채번
        if(i == 0):
            lotto[i] = now_number
            return np.delete(numarray, idx, 0)
        else :
            if(lotto.index(now_number) > -1):
                insetlotto(i)
    except ValueError:
        lotto[i] = now_number
        # 로또 배열에서 추출된 번호의 순번 값을 삭제한다
        return np.delete(numarray, idx, 0)

# 로또번호 생성 Function
def activate_lotto():
    insertnumber()
    for i in range(0,6) :
        numarray = insetlotto(i)


# 생성된 로또 번호 순차 정렬 Function
def sort_by_number():
    small_index = 0
    switching_value = 0
    inum_index = 0

    for i in range(0,6):
        inum_index = i
        for j in range(i,6):
            if((j+1) < 6):
                if(lotto[i] > lotto[j+1]):
                    small_index = j+1
                    switching_value = lotto[inum_index]
                    lotto[inum_index] = lotto[small_index]
                    lotto[small_index] = switching_value

                else :
                    small_index = i
                    switching_value = lotto[inum_index]
                    lotto[inum_index] = lotto[small_index]
                    lotto[small_index] = switching_value




# 로또번호 다시 생성할 지 묻는 Function
def confirm_choice ():
    confirm = input('다시 번호를 뽑으시겠습니까?\nYES : [ Y ] or NO : [ N ]\n')
    if (confirm in ('Y','N')):
        if(confirm == 'Y'):
            activate_lotto()
            print('정렬 전 : ',lotto)
            sort_by_number()
            print('정렬 후 : ',lotto)
            print('----------------------------------------------')
            print('로또 실행 결과 : ', lotto)
            print('----------------------------------------------')
            confirm_choice()
        else :
            print('로또 프로그램을 종료합니다.')
            print('----------------------------------------------')
    else :
        input('\n잘못된 입력입니다. 다시 입력해 주세요.\nYES : [ Y ] or NO : [ N ]  ')
        print('----------------------------------------------')

# 최초 로또 번호를 생성
print('----------------------------------------------')
activate_lotto()
print('정렬 전 : ',lotto)
sort_by_number()
print('정렬 후 : ',lotto)
print('로또 실행 결과 : ', lotto)
print('----------------------------------------------')
# 로또 번호를 다시 생성할 지 묻는다
confirm_choice ()