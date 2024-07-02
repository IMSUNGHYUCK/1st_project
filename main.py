import random

min_cont = 0

restart_game = 'y'

while restart_game == 'y':
 random_number = random.randint(1, 100)

 cont = 0


 while True:
  input_num = int(input('숫자를 입력하세요'))
  if not 1 <= input_num <= 100:
     print('입력한 숫자가 범위를 벗어났어요.1부터 100사이의 숫자를 입력해주세요')
     continue

  cont += 1

  if input_num < random_number:
   print('up')
  elif input_num > random_number:
   print('down')
  else:
   print(f'정답입니다.!! 시도횟수{cont}')
   if min_cont == 0 or cont < min_cont:
     min_cont = cont
     print(f'최소 시도 기록입니다: {min_cont}')
   break

 print(f'최소 시도 기록입니다: {min_cont}')
 restart_game = input('게임을 다시 시작하시겠습니까?(y/n): ').lower()

print(f'게임종료. 당신의 최소 시도 횟수는 {min_cont}입니다.')