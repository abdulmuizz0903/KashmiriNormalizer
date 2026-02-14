# KashmiriNormalizer

A Python library designed for normalizing Kashmiri text (Persio-Arabic script). This tool standardizes text by handling character variations, consistent punctuation spacing, and digit conversion. It is optimized for Natural Language Processing (NLP) pipelines and Machine Learning data preprocessing.

## Features

- **Character Canonicalization**: Maps multiple Unicode variants of Kashmiri characters to a single standard form using extensive character maps.
- **Code standardization**: Handles common inconsistencies in Kashmiri typing.
- **Punctuation & Spacing**: Automatically removes spaces before punctuation marks and ensures a single space follows them.
- **Digit Normalization**: Converts Kashmiri (Persio-Arabic) digits to standard English (Latin) digits for consistency.

## Installation

Ensure you have Python 3.8 or higher installed.

You can install the package directly from GitHub:

```bash
pip install git+https://github.com/abdulmuizz0903/KashmiriNormalizer.git
```

<!-- ### For Development

1. Clone the repository:
   ```bash
   git clone https://github.com/abdulmuizz0903/KashmiriNormalizer.git
   cd KashmiriNormalizer
   ```

2. Install the package locally:
   ```bash
   pip install .
   ``` -->

## Usage

### Normalization

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

### Digit Handling

The library automatically converts Kashmiri digits to English digits during normalization.

```python
digit_text = "١٢٣٤٥"
print(kn.normalize(digit_text)) 
# Output will have standardized English digits
```

### Text-to-Speech (TTS) Normalization

The library includes a specialized `TTSNormalizer` class tailored for Text-to-Speech tasks. This class extends the base normalization set with:

- **Preserves Diacritics**: Does not remove diacritics, which are crucial for correct pronunciation in Kashmiri.
- **Digit Expansion**: Converts digits (both Kashmiri and English) into their Kashmiri word forms (e.g., "1" -> "اکھ").
  - *Note: Requires populating the `WORD_TO_DIGIT_MAP` in `constants.py`.*
- **Plat Ye Handling**: Converts `ؠ` to `ۍ` at the end of words to align with standard writing rules.
- **Character Filtering**: Removes any characters not present in the allowed Kashmiri character set (`ALL_CHARACTERS`), ensuring clean input for TTS models.

```python
from KashmiriNormalizer import TTSNormalizer

# Initialize the TTS normalizer
tts_norm = TTSNormalizer()

text = "مےٚ چُھ 1 لۄکچارٕ پٮ۪ٹھٕ یہٕ عادت۔" 

# Normalize for TTS
tts_text = tts_norm.normalize(text)
print(tts_text)
# Output will have diacritics preserved, digits expanded to words, and non-Kashmiri chars removed.
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

