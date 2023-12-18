from sortedcontainers import SortedSet
from functools import cmp_to_key

# This solution come from Accepted Solutions Runtime Distribution
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):

        def compare(a, b):
            if a[0] > b[0]:
                return 1
            elif b[0] > a[0]:
                return -1
            if a[1] < b[1]:
                return 1
            elif b[1] < a[1]:
                return -1
            return 0
            
        self.food_ratings = {f: r for r, f in zip(ratings, foods)}
        self.food_cuisines = {f: c for c, f in zip(cuisines, foods)}
        self.cuisines = {}
        for c, (f, r) in zip(cuisines, self.food_ratings.items()):
            if c not in self.cuisines:
                self.cuisines[c] = SortedSet(key=cmp_to_key(compare))
            self.cuisines[c].add((r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        old_rating = self.food_ratings[food]
        self.food_ratings[food] = newRating
        self.cuisines[self.food_cuisines[food]].remove((old_rating, food))
        self.cuisines[self.food_cuisines[food]].add((newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines[cuisine][-1][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)