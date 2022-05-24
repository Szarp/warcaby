from names import names
import heapq
import random


class Elo:
    def __init__(self, k: int = 10, g: int = 1):
        self.ratingDict = {}
        self.k = k
        self.g = g

    def addPlayer(
        self,
        name,
        rating=1500,
        depth=2,
        params: list = [1, 5, 0.7, 0.2, 1, 0.5, 0.5, 0.5, 0.2, 0.2],
    ):
        # depth params
        self.ratingDict[name] = [rating, depth, params]

    def gameOver(self, winner: str, loser: str):
        result = self.expectResult(self.ratingDict[winner][0], self.ratingDict[loser][0])
        self.ratingDict[winner][0] = self.ratingDict[winner][0] + (self.k * self.g) * (1 - result)
        self.ratingDict[loser][0] = self.ratingDict[loser][0] + (self.k * self.g) * (
            0 - (1 - result)
        )

    def expectResult(self, p1, p2):
        exp = (p2 - p1) / 400.0
        return 1 / ((10.0 ** (exp)) + 1)

    def create_players(self, choosen_players: list = []):
        if len(choosen_players) > 0:
            pass
        else:
            for player in names:
                name, depth, params = player
                params = [int(p) / 10 for p in params.split(",")]
                self.addPlayer(name=name, depth=depth, params=params)

    def get_random_player(self, name: str = ""):
        if name == "":
            name = random.choice(list(self.ratingDict.keys()))
        return (name, self.ratingDict[name])

    def get_best_players(self, limit: int = 50):
        return heapq.nlargest(limit, self.ratingDict.items(), key=lambda i: i[0])
        pass


# test = Elo(k = 20)
# test.addPlayer("Daniel", rating = 1600)
# test.addPlayer("Mike")
if __name__ == "__main__":
    test = Elo(k=20)
    # test.addPlayer("Daniel", rating=1600)
    # test.addPlayer("Mike")
    # name, depth, params = names[0]
    # params = [int(p) / 10 for p in params.split(",")]
    # test.addPlayer(name=name, depth=depth, params=params)
    # test.gameOver("Daniel", name)
    # print(name, depth, params)
    test.create_players()
    print(test.get_best_players())
    # print(test.ratingDict)
