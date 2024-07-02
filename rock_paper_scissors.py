import random

cont = 0
cont_win = 0
cont_lose = 0
list_user = ['가위','바위','보']
restart_game = 'y'

while restart_game == 'y':
 num = random.randint(1, 3)

 if num == 1:
    com = '가위'
 elif num == 2:
    com = '바위'
 else:
    com = '보'


 while True:
   user = input('게임을 시작합니다.(가위,바위,보 중 하나를 입력해주세요)')
   if not user in list_user:
      print('잘못입력하셨습니다. 가위,바위,보 중 입력해주세요')
      continue

   if (user == '가위' and com == '보') or \
        (user == '보' and com == '바위') or \
           (user == '바위' and com == '가위'):
       cont_win += 1
       print(f'이겼습니다! 컴퓨터:{com} 사용자:{user}')
       break
   elif user == com:
       cont_win += 1
       print(f'비겼습니다!컴퓨터:{com} 사용자:{user}')
       cont += 1
       break
   else:
       print(f'졌습니다.컴퓨터:{com} 사용자:{user}.')
       cont_lose += 1
       break
       if min_cont == 0 or cont < min_cont:
          min_cont = cont
          print(f'{cont_win}승 {cont_lose}패 {cont} 무 입니다 ')


 restart_game = input('게임을 다시 시작하시겠습니까?(y/n): ').lower()

print(f'{cont_win}승 {cont_lose}패 {cont} 무 입니다.')