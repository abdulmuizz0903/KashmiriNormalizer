# KashmiriNormalizer

A Python library designed for normalizing Kashmiri text (Persio-Arabic script). This tool standardizes text by handling character variations, consistent punctuation spacing, and digit conversion. It is optimized for Natural Language Processing (NLP) pipelines and Machine Learning data preprocessing.

## Features

- **Character Canonicalization**: Maps multiple Unicode variants of Kashmiri characters to a single standard form using extensive character maps.
- **Code standardization**: Handles common inconsistencies in Kashmiri typing.
- **Punctuation & Spacing**: Automatically removes spaces before punctuation marks and ensures a single space follows them.
- **Digit Normalization**: Converts Kashmiri (Persio-Arabic) digits to standard English (Latin) digits for consistency.
- **Post-Processing Rules**: specific rules for writing conventions, such as handling final forms of specific characters (e.g., 'ؠ' to 'ۍ' at word boundaries).

## Installation

### From Source

Ensure you have Python 3.8 or higher installed.

1. Clone the repository:
   ```bash
   git clone https://github.com/abdulmuizz0903/KashmiriNormalizer.git
   cd KashmiriNormalizer
   ```

2. Install the package locally:
   ```bash
   pip install .
   ```

## Usage

### 1. Pre-processing (Normalization)

The `normalize` method is intended for cleaning text data. It performs canonicalization, digit conversion, and punctuation fixing.

```python
from KashmiriNormalizer import KashmiriNormalizer

# Initialize the normalizer
kn = KashmiriNormalizer()

text = "مےٚ چُھ لۄکچارٕ پٮ۪ٹھٕ یہٕ عادت" # Example text

# Normalize the text
cleaned_text = kn.normalize(text)
print(cleaned_text)
```

### 2. Post-processing

The `PostNormalize` method applies all normalization rules plus additional linguistic corrections specific to Kashmiri writing conventions (e.g., specific rules for the letter 'Ye'). This is useful for final text output or display.

```python
# Post-process the text
final_text = kn.PostNormalize(text)
print(final_text)
```

### 3. Digit Handling

The library automatically converts Kashmiri digits to English digits during normalization.

```python
digit_text = "١٢٣٤٥"
print(kn.normalize(digit_text)) 
# Output will have standardized English digits
```

## Dependencies

- [regex](https://pypi.org/project/regex/): Used for advanced Unicode string handling.

## Development

The project structure is as follows:

```
KashmiriNormalizer/
├── src/
│   └── KashmiriNormalizer/
│       ├── __init__.py
│       ├── constants.py     # Character maps and regex constants
│       └── normalizer.py    # Main Normalizer class
└── pyproject.toml           # Build configuration and dependencies
```

