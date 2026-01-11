import random
import time

omikuji = ["大吉", "吉", "凶", "中吉"]  # 結果リストをまとめて定義

again = "y"

while again == "y":
    result = random.choice(omikuji)
    print("今日の運勢は", end="", flush=True)
    count = 0
    while count <= 2:
        time.sleep(1)
        print(".", end="", flush=True)
        count += 1

time.sleep(1)

print(f"{result}")

again = input("もう一度引く(y/s)>")
