"""
https://adventofcode.com/2022/day/1
--- Day 1: Calorie Counting ---
--PART ONE--
This list represents the Calories of the food carried by five Elves:
    The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
    The second Elf is carrying one food item with 4000 Calories.
    The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
    The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
    The fifth Elf is carrying one food item with 10000 Calories.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: 
    they'd like to know how many Calories are being carried by the Elf carrying the most Calories. 
    In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
--PART TWO--
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most
Calories of food might eventually run out of snacks.
To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three
Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""

import csv


class ElvesCalories:

    def __init__(self, elves_calories_list):
        self.elves_with_calories_summed = {"Elf n°1": 0}
        elves_count = 1
        for calorie in elves_calories_list:

            if not calorie:
                elves_count += 1
                self.elves_with_calories_summed["Elf n°{}".format(elves_count)] = 0
                continue
            self.elves_with_calories_summed["Elf n°{}".format(elves_count)] += int(calorie[0])

    def elfWithMostCalories(self):
        # x[0] is key, x[1] is value from ".items()"
        sorted_elves_by_calories = sorted(self.elves_with_calories_summed.items(), key=lambda x: x[1], reverse=True)
        return sorted_elves_by_calories[0]

    def top3ElvesWithMostCalories(self):
        sorted_elves_by_calories = sorted(self.elves_with_calories_summed.items(), key=lambda x: x[1], reverse=True)
        return sorted_elves_by_calories[0:3]


if __name__ == "__main__":
    with open("input.csv", "r+") as csv_file:
        input_list = csv.reader(csv_file)
        elvesCalories = ElvesCalories(input_list)
        print("Part 1:")
        fat_elf = elvesCalories.elfWithMostCalories()
        print("It's {0} and he carries {1} food calories".format(fat_elf[0], fat_elf[1]))
        print("\nPart 2:")
        top3ElvesCalories = elvesCalories.top3ElvesWithMostCalories()
        print("Top 1 is {0}, he carries {1} food calories".format(top3ElvesCalories[0][0],
                                                                  top3ElvesCalories[0][1]))
        print("Top 2 is {0}, he carries {1} food calories".format(top3ElvesCalories[1][0],
                                                                  top3ElvesCalories[1][1]))
        print("Top 3 is {0}, he carries {1} food calories".format(top3ElvesCalories[2][0],
                                                                  top3ElvesCalories[2][1]))
        print("Total is {0} calories".format(top3ElvesCalories[0][1] + top3ElvesCalories[1][1] + top3ElvesCalories[2][1]))
