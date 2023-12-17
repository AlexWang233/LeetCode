from sortedcontainers import SortedSet

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.rating_map = {}
        self.cuisine_map = {}
        self.food_map = defaultdict(SortedSet)

        for i in range(len(foods)):
            self.rating_map[foods[i]] = ratings[i]
            self.cuisine_map[foods[i]] = cuisines[i]
            self.food_map[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:

        cuisine = self.cuisine_map[food]
        old_element = (-self.rating_map[food], food)

        self.food_map[cuisine].remove(old_element)
        self.rating_map[food] = newRating
        self.food_map[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        highest_rated = self.food_map[cuisine][0]
        return highest_rated[1]