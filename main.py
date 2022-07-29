import os
from colorama import init
from colorama import Fore, Back, Style
init()
#os.system(f'mode con: cols={60} lines={26}') sets window size

def main():
  print("ﾋﾟﾋﾟﾋﾟ...ハロー")
  print("資金：利率：回数 を入力ちてもらう")
  roop = True
  
  while roop:
    money = float(input('資金: '))
    rate =  float(input('利率%: '))
    n =     int(input('回数: '))
    money_start = money
    money_before = 0

    for i in range(n):
      money_before = money
      money += round(money * (rate / 100))
      
      print(Fore.YELLOW+"{}".format(i+1), end='')
      print(Fore.RESET+':' ,end='')
      print(Fore.CYAN+"{:,}".format(round(money)) ,end='')
      print(Fore.GREEN+' + '+"{:,}".format(round(money-money_before)))
    print(Fore.LIGHTMAGENTA_EX + "{}%".format(round( (money / money_start -1) * 100,1)))
    print(Fore.RESET)

if __name__ == '__main__':main()