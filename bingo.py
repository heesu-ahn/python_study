import random as rn
import numpy as np
import time

# 빙고에 들어갈 숫자 목록
nums = []
# 1차원 배열
lst = [0] * 5
# 빙고판 배열
board = np.zeros((5,5), int)

# one빙고 조건(종,횡,사선)
onebingo = ([])

# 중복 숫자 당첨인지 확인하는 리스트
duplicate_list = np.zeros((25,2),int)

#중복 횟수 10 개씩 차감하기 위해 값을 따로 가지고 있음
summary = 0

# 빙고에 들어갈 숫자 배열 초기화
def initiallize_nums ():
    for i in range(1,26):
        nums.append(str(i))
    return

# 1차원 배열 생성해서 다중 배열에 집어넣는 준비 과정
def random_swap():
    # 배열에서 삭제하는 과정에서 index out of range 가 너무 자주 발생해서
    # 삭제를 하지 않고 서로 위치를 변경하는 것으로 방식을 바꿈
    pos = 0
    for i in nums:
        r = rn.randint(0, 24)
        change_vale = nums[r]
        nums[r] = nums[pos]
        nums[pos] = change_vale
        pos += 1
    return

# 1차원 배열을 5 * 5 다차원 배열로 행열 변환하여 반환하는 함수
def insert_into_board():
    try:
        arr = np.array(nums) # Convert List to Array
        arr = np.reshape(arr,(5,5)) # Reshape Multi Demension (5 * 5)
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
    if(total >= 3):
        confirm = input('중복 숫자를 3번 뽑으셨습니다. 원하는 번호를 뽑으시겠습니까?\nYES : [ Y ] or NO : [ N ]\n')
        if (confirm in ('Y', 'N')):
            if (confirm == 'Y'):
                confirm = input('원하는 번호를 입력하세요.\n')
                duplicate_list[int(confirm)-1][1] = 1
                x = np.where(board == confirm)[0][0]
                y = np.where(board == confirm)[1][0]
                board[x][y] = 'X'
                total = total - 3
                print('번호', confirm, '에 대한 처리가 완료 되었습니다.')
                return  total
            else:
                print('번호를 뽑습니다.')
        else :
            input('\n잘못된 입력입니다. 다시 입력해 주세요.\nYES : [ Y ] or NO : [ N ]  ')
            duple_count(summary)
    return total

def ask_get_number():

    bingo = get_bingo()
    if(bingo == 25):
        print('빙고가 완료되었습니다. 프로그램을 종료합니다.')
    else:
        confirm = input('번호를 뽑으시겠습니까?\nYES : [ Y ] or NO : [ N ]\n')
        if (confirm in ('Y', 'N')):
            if (confirm == 'Y'):
                num = getnumber(3)
                if (duplicate_list[num - 1][1] == 1):
                    global  summary
                    summary += 1
                    summary = duple_count(summary)
                    if(summary > 0):
                        print('중복 번호 : ', num)
                        print(board)
                        print('(총)중복횟수 : ', summary)
                        ask_get_number()
                    else :
                        ask_get_number()
                else:
                    x = np.where(board == str(num))[0][0]
                    y = np.where(board == str(num))[1][0]
                    board[x][y] = 'X'
                    duplicate_list[num - 1][1] = 1
                    summary = duple_count(summary)
                    print('추첨 번호 : ',num,'위치 : [',x,'],[', y,']')
                    print(board)
                    print('(총)중복횟수 : ', summary)
                    ask_get_number()
            else:
                print('빙고 프로그램을 종료합니다.')
                return
        else :
            input('\n잘못된 입력입니다. 다시 입력해 주세요.\nYES : [ Y ] or NO : [ N ]  ')
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
    r = rn.randint(1, 25)
    return r

def get_bingo():
    num = 0
    bingo = 0
    for i in duplicate_list:
        bingo += duplicate_list[num][1]
        num += 1
    return bingo

initiallize_nums()
random_swap()
board = insert_into_board()
set_duple_list()
ask_get_number()




# print(duplicate_list)
# print('sum = ', summary)
# print('board\n',board)



