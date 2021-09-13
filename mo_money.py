from datetime import datetime
import time


def main():
  money = input("What's you're total yearly gross income\n:~> ")
  money = float(money.replace(',', ''))
  money_per_millisecond = money / (365.25 * 24 * 60 * 60 * 1000)
  
  now = datetime.now()

  elapsed_time = 0
  total_made = 0

  while True:
    elapsed_time = (datetime.now().timestamp() - now.timestamp()) * 1000
    total = elapsed_time * money_per_millisecond
    print(f"You made ${total:.02f}!            ", end="\r")


if __name__ == '__main__':
  main()
