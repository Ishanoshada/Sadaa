import random
from .datalist import *

datasets = {
    "quantum": [quantum_settings, quantum_characters, quantum_events, quantum_plot_twists, quantum_resolutions],
    "math": [math_settings, math_characters, math_events, math_plot_twists, math_resolutions],
    "prediction": [prediction_settings, prediction_characters, prediction_events, prediction_plot_twists, prediction_resolutions]
}

class GenerateStoryWords:
    def __init__(self, num_words=30, num_stories=1, type=None):
        self.num_words = num_words
        self.num_stories = num_stories
        self.generated_stories = set()
        self.type = type
        types = list(datasets.keys())

        if not self.type:
            self.type = random.choice(types)

        self.settings = datasets[self.type][0]
        self.characters = datasets[self.type][1]
        self.events = datasets[self.type][2]
        self.plot_twists = datasets[self.type][3]
        self.resolutions = datasets[self.type][4]

        if self.num_words < 65:
            raise ValueError("The minimum allowed number of words is 65.")
        
    def generate_story(self):
        
        story = ""
        current_word_count = 0

        # Generate the story
        while current_word_count < self.num_words:
            # Randomly select elements from the lists
            setting = random.choice(self.settings)
            character = random.choice(self.characters)
            event = random.choice(self.events)
            twist = random.choice(self.plot_twists)
            resolution = random.choice(self.resolutions)

            # Construct the sentence
            sentence = f"{setting} {character} {event}. {twist} {resolution} "

            # Calculate the number of words in the sentence and update the count
            sentence_word_count = len(sentence.split())
            if current_word_count + sentence_word_count <= self.num_words:
                story += sentence
                current_word_count += sentence_word_count
            else:
                break

        return story
    
    def generate_stories(self):
        stories = []

        while len(stories) < self.num_stories:
            new_story = self.generate_story()
            if new_story not in self.generated_stories:
                self.generated_stories.add(new_story)
                stories.append(new_story)

        return stories



