class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        people_num = len(groupSizes)
        groups_temp = [[] for i in range(people_num + 1)]
        # groups[1].append(5)
        # print(groups)
        # print(people_num)
        for person in range(people_num):
            person_in_size = groupSizes[person]
            # print(person_in_size)
            groups_temp[person_in_size].append(person)
        print(groups_temp)
        groups = []
        for size in range(people_num + 1):
            if groups_temp[size]:
                self.regroup(groups, size, groups_temp[size])
        print(groups)
        return groups
        
                
    def regroup(self, groups, size, tempList):
        group = []
        count = 0
        for person in tempList:
            group.append(person)
            count += 1
            if count == size:
                groups.append(group)
                group = []
                count = 0
                