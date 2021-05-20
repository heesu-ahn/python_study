import random as rn
import numpy as np
import time

# x축 숫자 y축 숫자를 관리하는 변수
x_count = 5
y_count = 5
# 중복 숫자를 관리하는 변수
dp_count = 3
# 카운트 다운 횟수
count_number = 3

# 빙고에 들어갈 숫자 목록
nums = []
# 1차원 배열
lst = [0] * x_count
# 빙고판 배열
board = np.zeros((x_count,y_count), int)
# one빙고 조건(종,횡,사선)
onebingo = ([])
# 중복 숫자 당첨인지 확인하는 리스트
duplicate_list = np.zeros(((x_count*y_count),2),int)
# 어떤 숫자들이 연속으로 중복이 되었는지 보여주는 변수
duple_number_list = ''
# 중복 횟수 N 개씩 차감하기 위해 값을 따로 가지고 있음
summary = 0

# input 값이 문자열로 들어왔는지 검증하는 함수
# 숫자로만 들어와야 함
def is_Integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    except TypeError:
        return False


# 빙고에 들어갈 숫자 배열 초기화
def initiallize_nums ():
    for i in range(1,(x_count*y_count) + 1):
        nums.append(str(i))
    return

# 1차원 배열 생성해서 다중 배열에 집어넣는 준비 과정
def random_swap():
    # 배열에서 삭제하는 과정에서 index out of range 가 너무 자주 발생해서
    # 삭제를 하지 않고 서로 위치를 변경하는 것으로 방식을 바꿈
    pos = 0
    for i in nums:
        r = rn.randint(0, (x_count*y_count) - 1) # (x * y) - 1 이 배열의 주소 길이
        change_vale = nums[r]
        nums[r] = nums[pos]
        nums[pos] = change_vale
        pos += 1
    return

# 1차원 배열을 5 * 5 다차원 배열로 행열 변환하여 반환하는 함수
def insert_into_board():
    try:
        arr = np.array(nums) # Convert List to Array
        arr = np.reshape(arr,(x_count,y_count)) # Reshape Multi Demension (5 * 5)
        return  arr #Array 반환 하여 board 의 값을 arr로 바꾼다
    # 에러 처리 관련 항목
    except ValueError as e:
        print('From insert_into_board occured ValueError : ', e, 'reactivate.')
    except IndexError as e1:
        print('From insert_into_board occured IndexError : ', e1, 'reactivate.')
    except TypeError as e2:
        print('From insert_into_board occured TypeError : ', e2, 'reactivate.')
    return

# 종복 대상 리스트
def set_duple_list():
    num = 0
    for i in duplicate_list:
        duplicate_list[num][0] = num + 1
        num += 1
    return

# 종복 횟수 세기
def duple_count(total):
    global dp_count
    global duple_number_list
    if(total >= dp_count):
        confirm = input('중복 숫자를 %s번 뽑으셨습니다. '
                        '\n중복 된 숫자 내역 : %s'
                        '\n원하는 번호를 뽑으시겠습니까?\nYES : [ Y ] or NO : [ N ]'
                        '\n----------------------------------------------\n'
                        %(dp_count,duple_number_list))
        if (confirm in ('Y', 'N')):
            if (confirm == 'Y'):
                confirm = input('원하는 번호를 입력하세요.'
                                '\n----------------------------------------------\n')
                if(is_Integer(confirm)):
                    duplicate_list[int(confirm)-1][1] = 1
                    x = np.where(board == confirm)[0][0]
                    y = np.where(board == confirm)[1][0]
                    board[x][y] = 'X'
                    total = total - dp_count
                    # 연속으로 중복된 숫자 내역 초기화
                    duple_number_list = ''
                    print('번호', confirm, '에 대한 처리가 완료 되었습니다.')
                    print('----------------------------------------------')
                    return  total
                else:
                    print('잘못된 입력입니다 %s' %confirm)
                    print('----------------------------------------------')
            else:
                print('번호를 뽑습니다.')
                print('----------------------------------------------')
                return total
        else :
            input('\n잘못된 입력입니다.\n다시 입력해 주세요.\nYES : [ Y ] or NO : [ N ]'
                  '\n----------------------------------------------\n')
            duple_count(summary)
    return total

def ask_get_number():

    bingo = get_bingo()
    if(bingo == (x_count * y_count)):
        print('빙고가 완료되었습니다.'
              '\n프로그램을 종료합니다.')
        print('----------------------------------------------')
    else:
        confirm = input('번호를 뽑으시겠습니까?'
                        '\nYES : [ Y ] or NO : [ N ]'
                        '\n----------------------------------------------\n')
        if (confirm in ('Y', 'N')):
            if (confirm == 'Y'):
                num = getnumber(count_number)
                if (duplicate_list[num - 1][1] == 1):
                    global  summary
                    global  duple_number_list
                    # 중복 횟수 카운트
                    summary += 1
                    # 연속으로 중복된 숫자 기록
                    duple_number_list += str(num) + ','
                    summary = duple_count(summary)
                    if(summary > 0):
                        print('중복 번호 : ', num)
                        print(board)
                        print('(총)중복횟수 : ', summary)
                        print('----------------------------------------------')
                        ask_get_number()
                    else :
                        ask_get_number()
                else:
                    x = np.where(board == str(num))[0][0]
                    y = np.where(board == str(num))[1][0]
                    board[x][y] = 'X'
                    duplicate_list[num - 1][1] = 1
                    summary = duple_count(summary)
                    print('----------------------------------------------'
                          '\n빙고 번호 : ',num,'\n위치 : [',x,'],[', y,']')
                    print(board)
                    print('(총)중복횟수 : ', summary)
                    print('----------------------------------------------')
                    ask_get_number()
            else:
                print('빙고 프로그램을 종료합니다.')
                print('----------------------------------------------')
                return
        else :
            input('\n잘못된 입력입니다.\n다시 입력해 주세요.\nYES : [ Y ] or NO : [ N ]'
                  '\n----------------------------------------------\n')
            print(duplicate_list)
            print(summary)
            ask_get_number()
    return

def getnumber(t):
    while t:
        print('countdown : ',t)
        time.sleep(0.5)
        t -= 1
    print('번호 추첨')
    r = rn.randint(1, (x_count * y_count))
    return r

def get_bingo():
    num = 0
    bingo = 0
    for i in duplicate_list:
        bingo += duplicate_list[num][1]
        num += 1
    return bingo




#
initiallize_nums()
random_swap()
board = insert_into_board()
set_duple_list()
ask_get_number()
#



# print(duplicate_list)
# print('sum = ', summary)
# print('board\n',board)



