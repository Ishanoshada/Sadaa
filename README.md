# Sadaa - Python Story Generation Package

Unleash Your Imagination with Sadaa!


![img1](https://github.com/Ishanoshada/Ishanoshada/blob/main/ss/6c9ec14e076ac4663afea598867a367b.png?raw=true)


The Sadaa package is not just a Python library; it's a portal to infinite worlds of imagination. Dive into the universe of science fiction and embark on epic journeys with the power of words.

![img2](https://github.com/Ishanoshada/Ishanoshada/blob/main/ss/ecaa76685cd799e2445aab18638d7dd4.png?raw=true)


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Importing the Module](#importing-the-module)
  - [Generating Stories](#generating-stories)
- [Examples](#examples)
  - [Example 1 : MoonStoryGenerator - Moonlit Tales](#example-1-moonstorygenerator---moonlit-tales)
  - [Example 2: Quantum Stories - Beyond Reality](#example-2-generating-quantum-stories)
  - [Example 3: Math-based Adventures - Equations Unleashed](#example-3-generating-math-based-stories)
  - [Example 4: Prediction Stories - Glimpses of Tomorrow](#example-4-generating-prediction-stories)
  - [Example 5: Akikiki Stories - Mysteries of Akikiki](#example-5-generating-akikiki-stories)
  - [Example 6: Quantum Stories with Different Lengths - Size Doesn't Matter](#example-6-generating-quantum-stories-with-different-lengths)
  - [Example 7: Math-based Stories with Multiple Tales - Math Marvels](#example-7-generating-math-based-stories-with-multiple-stories)
  
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

## Installation

Embark on your storytelling journey by installing the package with a simple command:

```bash
pip install sadaa
```

## Usage

### Importing the Module

Your gateway to imagination is just an import away:

```python
from sadaa import GenerateStoryWords, AkikikiStoryGenerator 
```

### Generating Stories

Ready to craft your tales? You have the power to control the narrative. Choose the number of words, stories, and themes, from quantum to math, or delve into predictions. If you seek the mystical Akikiki stories, they're just a generator away:

```python
story_generator = GenerateStoryWords(num_words=80, num_stories=1, type="quantum")
stories = story_generator.generate_stories()

akikiki_story_generator = AkikikiStoryGenerator(num_stories=3)  # Unlock the secrets of Akikiki with 3 captivating stories
akikiki_stories = akikiki_story_generator.generate_stories()
```

![img2](https://github.com/Ishanoshada/Ishanoshada/blob/main/ss/d6f73659b9c5f09d019c8b0c8bd6f9fc.png?raw=true)

## Examples

### Example 1: MoonStoryGenerator - Moonlit Tales

Illuminate your night with stories inspired by the serene Moon:

```python
from sadaa import MoonStoryGenerator

moon_story_generator = MoonStoryGenerator(5)

print("Moon-themed Story:")
print(moon_story_generator.generate_stories())
```

### Example 2: Quantum Stories - Beyond Reality

Enter the quantum realm and explore the limitless possibilities of science:

```python
from sadaa import GenerateStoryWords

story_generator = GenerateStoryWords(num_words=70, num_stories=2, type="quantum")
stories = story_generator.generate_stories()

for i, story in enumerate(stories, start=1):
    print(f"Quantum Story {i}:\n{story}\n")
```

### Example 3: Math-based Adventures - Equations Unleashed

Let math take you on a thrilling journey through the world of numbers and equations:

```python
from sadaa import GenerateStoryWords

story_generator = GenerateStoryWords(num_words=90, num_stories=2, type="math")
stories = story_generator.generate_stories()

for i, story in enumerate(stories, start=1):
    print(f"Math Story {i}:\n{story}\n")
```

### Example 4: Prediction Stories - Glimpses of Tomorrow

Peek into the future with stories that unravel the mysteries of foresight:

```python
from sadaa import GenerateStoryWords

story_generator = GenerateStoryWords(num_words=70, num_stories=2, type="prediction")
stories = story_generator.generate_stories()

for i, story in enumerate(stories, start=1):
    print(f"Prediction Story {i}:\n{story}\n")
```

### Example 5: Akikiki Stories - Mysteries of Akikiki

Discover the enigmatic world of Akikiki with 3 captivating stories:

```python
from sadaa import AkikikiStoryGenerator

akikiki_story_generator = AkikikiStoryGenerator(num_stories=3)
akikiki_stories = akikiki_story_generator.generate_stories()

for i, story in enumerate(akikiki_stories, start=1):
    print(f"Akikiki Story {i}:\n{story}\n")
```

### Example 6: Quantum Stories with Different Lengths - Size Doesn't Matter

No matter the length, quantum stories always pack a punch:

```python
from sadaa import GenerateStoryWords

story_generator = GenerateStoryWords(num_words=70, num_stories=3, type="quantum")
stories = story_generator.generate_stories()

for i, story in enumerate(stories, start=1):
    print(f"Quantum Story {i}:\n{story}\n")
```

### Example 7: Math-based Stories with Multiple Tales - Math Marvels

Multiply your storytelling prowess with multiple math-based stories:

```python
from sadaa import GenerateStoryWords

story_generator = GenerateStoryWords(num_words=80, num_stories=3, type="math")
stories = story_generator.generate_stories()

for i, story in enumerate(stories, start=1):
    print(f"Math Story {i}:\n{story}\n")
```

## Example Output

### Quantum Story (200 Words)

Ready for an epic quantum journey? Generate a quantum-inspired story:

```python
quantum_story = GenerateStoryWords(200,type="quantum").generate_story()

print(quantum_story)
```

**Output**:

> Within the shimmering boundaries of a quantum chaos simulation, Quantum Quester, an interdimensional traveler exploring realms beyond the quantum veil, conducted a successful experiment in quantum teleportation. An ancient artifact revealed the quantum echoes of their past lives. Their mastery of quantum manipulation brought about an era of unbounded creativity and innovation. Amidst the swirling vortices of a quantum fluid experiment, Professor Paradox, a time theorist navigating the intricacies of quantum causality, conducted a successful experiment in quantum teleportation of matter. An ancient prophecy foretold of a quantum savior who would reshape the cosmos. The quantum truths they brought to light would challenge the very core of reality and being. Within the crystalline structure of a quantum lattice system, Professor Samuel Quark, an eccentric inventor known for pushing the boundaries of quantum mechanics, opened a gateway to a realm governed by quantum chaos. They discovered they were living in a simulated quantum universe. The quantum enlightenment they attained would permeate the collective consciousness of their species.

## Contributing

Ready to add your own twist to the tales? Check out our [contributing guidelines](

CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

**Repository Views** ![Views](https://profile-counter.glitch.me/Sadaa/count.svg)

Dive into the world of Sadaa and let your imagination run wild! 🚀📚
