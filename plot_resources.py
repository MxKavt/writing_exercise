import random
from data import genre_list, ending_choice, character_quantity, mc_age, mc_type, mc_occupation


class Plot:

    def working_genre(self):
        chosen_genre = random.sample(genre_list, k=3)
        return ', '.join(chosen_genre)

    def working_ending(self):
        chosen_ending = random.choice(ending_choice)
        return chosen_ending

    def working_characters(self):
        chosen_characters = random.choice(character_quantity)
        return chosen_characters

    def __repr__(self):
        return f'You will be working with the genres: {self.working_genre()}, with a {self.working_ending()} ending, ' \
               f'{self.working_characters()} characters!'


class MainCharacter:

    def mc_age(self):
        chosen_age = random.choice(mc_age)
        return chosen_age

    def mc_type(self):
        chosen_type = random.choice(mc_type)
        return chosen_type

    def mc_occupation(self):
        chosen_occupation = random.choice(mc_occupation)
        return chosen_occupation

    def __repr__(self):
        return f'Your main character stats: {self.mc_age()} years old, ' \
               f'{self.mc_type()} of the story, {self.mc_occupation()}.'








