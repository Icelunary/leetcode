from sortedcontainers import SortedSet
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisineDataTbl = defaultdict(SortedSet) #save as {"cuisine": SortedSet(<rating, food>)}
        self.foodDataTbl = defaultdict(list) #save as {"food": [cuisine, rating]}
        # iterate init value
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foodDataTbl[food] = [cuisine, rating]
            self.cuisineDataTbl[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.cuisineDataTbl.get(self.foodDataTbl[food][0]) # get the food cuisine 
        cuisine.remove((-self.foodDataTbl[food][1], food)) # remove the food cuisine value in the set
        cuisine.add((-newRating, food)) # add new value
        self.foodDataTbl[food][1] = newRating # update rating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisineDataTbl[cuisine][0][1] # get 1st element in the sorted set