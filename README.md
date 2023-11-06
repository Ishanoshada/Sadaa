# Sadaa - Python Story Generation Package

The Sadaa package is a Python library designed to generate random science-fiction-style stories based on different themes. It provides a flexible and customizable way to create imaginative narratives for various settings.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Importing the Module](#importing-the-module)
  - [Generating Stories](#generating-stories)
- [Examples](#examples)
  - [Example 1 : MoonStoryGenerator - Generating Moon-themed Stories](#example-1-moonstorygenerator---generating-moon-themed-stories)
  - [Example 2: Generating Quantum Stories](#example-2-generating-quantum-stories)
  - [Example 3: Generating Math-based Stories](#example-3-generating-math-based-stories)
  - [Example 4: Generating Prediction Stories](#example-4-generating-prediction-stories)
  - [Example 5: Generating Akikiki Stories](#example-5-generating-akikiki-stories)
  - [Example 6: Generating Quantum Stories with Different Lengths](#example-6-generating-quantum-stories-with-different-lengths)
  - [Example 7: Generating Math-based Stories with Multiple Stories](#example-7-generating-math-based-stories-with-multiple-stories)
  
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

## Installation

You can install the package using pip:

```bash
pip install sadaa
```

## Usage

### Importing the Module

```python
from sadaa import GenerateStoryWords, AkikikiStoryGenerator 
```

### Generating Stories

To generate stories, you can create an instance of `GenerateStoryWords` and specify the number of words and stories you want. Optionally, you can choose a specific theme (`type`) from the available options: "quantum", "math", or "prediction".

For Akikiki stories, you can use the `AkikikiStoryGenerator` class:

```python
story_generator = GenerateStoryWords(num_words=80, num_stories=1, type="quantum")
stories = story_generator.generate_stories()

akikiki_story_generator = AkikikiStoryGenerator(num_stories=3)  # Generate 3 Akikiki stories
akikiki_stories = akikiki_story_generator.generate_stories()
```

## Examples

### Example 1: MoonStoryGenerator - Generating Moon-themed Stories

```python
from sadaa import MoonStoryGenerator

moon_story_generator = MoonStoryGenerator(5)

print("Moon-themed Story:")
print(moon_story_generator.generate_stories())
```

### Example 2: Generating Quantum Stories

```python
from sadaa import GenerateStoryWords

story_generator = GenerateStoryWords(num_words=70, num_stories=2, type="quantum")
stories = story_generator.generate_stories()

for i, story in enumerate(stories, start=1):
    print(f"Quantum Story {i}:\n{story}\n")
```

### Example 3: Generating Math-based Stories

```python
from sadaa import GenerateStoryWords

story_generator = GenerateStoryWords(num_words=90, num_stories=2, type="math")
stories = story_generator.generate_stories()

for i, story in enumerate(stories, start=1):
    print(f"Math Story {i}:\n{story}\n")
```

### Example 4: Generating Prediction Stories

```python
from sadaa import GenerateStoryWords

story_generator = GenerateStoryWords(num_words=70, num_stories=2, type="prediction")
stories = story_generator.generate_stories()

for i, story in enumerate(stories, start=1):
    print(f"Prediction Story {i}:\n{story}\n")
```

### Example 5: Generating Akikiki Stories

```python
from sadaa import AkikikiStoryGenerator

akikiki_story_generator = AkikikiStoryGenerator(num_stories=3)  # Generate 3 Akikiki stories
akikiki_stories = akikiki_story_generator.generate_stories()

for i, story in enumerate(akikiki_stories, start=1):
    print(f"Akikiki Story {i}:\n{story}\n")
```

### Example 6: Generating Quantum Stories with Different Lengths

```python
from sadaa import GenerateStoryWords

story_generator = GenerateStoryWords(num_words=70, num_stories=3, type="quantum")
stories = story_generator.generate_stories()

for i, story in enumerate(stories, start=1):
    print(f"Quantum Story {i}:\n{story}\n")
```

### Example 7: Generating Math-based Stories with Multiple Stories

```python
from sadaa import GenerateStoryWords

story_generator = GenerateStoryWords(num_words=80, num_stories=3, type="math")
stories = story_generator.generate_stories()

for i, story in enumerate(stories, start=1):
    print(f"Math Story {i}:\n{story}\n")
```

## Example Output

### Quantum Story (200 Words)

```python
# Generating a quantum-inspired story
quantum_story = story_generator.generate_story()

print(quantum_story)
```

**Output**:

> Within the shimmering boundaries of a quantum chaos simulation, Quantum Quester, an interdimensional traveler exploring realms beyond the quantum veil, conducted a successful experiment in quantum teleportation. An ancient artifact revealed the quantum echoes of their past lives. Their mastery of quantum manipulation brought about an era of unbounded creativity and innovation. Amidst the swirling vortices of a quantum fluid experiment, Professor Paradox, a time theorist navigating the intricacies of quantum causality, conducted a successful experiment in quantum teleportation of matter. An ancient prophecy foretold of a quantum savior who would reshape the cosmos. The quantum truths they brought to light would challenge the very core of reality and being. Within the crystalline structure of a quantum lattice system, Professor Samuel Quark, an eccentric inventor known for pushing the boundaries of quantum mechanics, opened a gateway to a realm governed by quantum chaos. They discovered they were living in a simulated quantum universe. The quantum enlightenment they attained would permeate the collective consciousness of their species.

## Contributing

If you'd like to contribute to this project, please read our [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).


**Repository Views** ![Views](https://profile-counter.glitch.me/Sadaa/count.svg)

