import random
class Coin_flip:
    def flip_coin(self):
        coin = ["Head", "Tail"]
        n = int(input("How many coins? are you fliping.."))
        for i in range(n):
            print(random.choice(coin))

obj = Coin_flip()
obj.flip_coin()
