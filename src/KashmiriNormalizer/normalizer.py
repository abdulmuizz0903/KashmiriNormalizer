from typing import List, Dict
from .constants import (
    KASHMIRI_CHARACTER_MAPPING,
    KASHMIRI_PUNCTUATIONS, PUNCTUATION_MAP,
    KASHMIRI_ENG_DIGITS_MAP, ENG_KASHMIRI_DIGITS_MAP, 
    KASHMIRI_DIACRITICS)
import regex as re

class KashmiriNormalizer:
    def __init__(self):
        """Initialize the normalizer."""
        pass

    def _replace(self, text: str, charMap: Dict[str, List[str]]) -> str:
        """Replaces the letters in the list in map's values with its key"""
        flattenMap: Dict = {}
        for key, value in charMap.items():
            for letter in value:
                flattenMap[letter] = key
                
        if flattenMap:
            # Sort by length (descending) to prevent substring issues
            sorted_bad_chars = sorted(flattenMap.keys(), key=len, reverse=True)
            
            pattern_string = "|".join(map(re.escape, sorted_bad_chars))
            
            regex_pattern = re.compile(pattern_string)
        else:
            regex_pattern = None
            
        if not regex_pattern:
            return text
            
        # The lambda finds the match in the inverted map and returns the correct key
        return regex_pattern.sub(
            lambda match: flattenMap[match.group(0)], 
            text
        )
        
    def _punctuation_spaces(self, text: str) -> str:
        """Removes spaces before punctuations and add spaces after them"""
        
        # Add spaces after punctuations, numbers and some special characters
        _SPACE_AFTER_PUNCTUATIONS_RE = re.compile(
            r"(?<=[" + "".join(KASHMIRI_PUNCTUATIONS) + "])(?=[^" + "".join(KASHMIRI_PUNCTUATIONS) + "0-9 \n])",
            flags=re.U | re.M | re.I)
        
        # Remove whitespaces before punctuations
        _REMOVE_SPACE_BEFORE_PUNCTUATIONS_RE = re.compile(r'\s+([' + "".join(KASHMIRI_PUNCTUATIONS) + '])',
                                                        flags=re.U | re.M | re.I)
        
        text = _SPACE_AFTER_PUNCTUATIONS_RE.sub(' ', text)
        text = _REMOVE_SPACE_BEFORE_PUNCTUATIONS_RE.sub(r'\1', text)
        return text
        
    def _canonicalize(self, text: str) -> str:
        """Canonicalize text using Kashmiri Character maps."""
        
        text = self._replace(text, KASHMIRI_CHARACTER_MAPPING)
        text = self._replace(text, PUNCTUATION_MAP)
        return text

    def _replace_digits(self, text: str, toEnglish: bool = True) -> str:
        """Replaces Kashmiri (Persio-Arabic) Digits with English (Latin) Digits and vice versa"""
        if not toEnglish:
            return self._replace(text, KASHMIRI_ENG_DIGITS_MAP)
        return self._replace(text, ENG_KASHMIRI_DIGITS_MAP)
    def _handlePlatYe(self, text: str) -> str:
        """Replaces ؠ with ۍ when it occurs at the final position of words to align with Kashmiri writing rules"""
        
        t = re.escape('ؠ')
        pattern = fr"\b{t}|{t}\b"
        return re.sub(pattern, "ۍ", text)
    
    def _removeDiacritics(self, text: str) -> str:
        """Removes all the diacritics from the input text"""
        REP_MAP = {"": list(KASHMIRI_DIACRITICS)}
        return self._replace(text, REP_MAP)
    
    def normalize(self, text: str, removeDiacritics: bool = False) -> str:
        """
        1. Canonicalizes the text
        2. Replaces Kashmiri digits with English 
        3. Handles spaces before and after punctuations
        
        Ideal for Pre-Processing of ML models.
        NOTE: For post processing use PostNormalize method
        Args:
            text (str): The input text to normalize.
            removeDiacritics (bool): Do you want to remove Diacritics or not?
            
        Returns:
            str: The normalized text.
        """
        text = self._canonicalize(text)
        text = self._replace_digits(text)
        text = self._punctuation_spaces(text)
        if removeDiacritics:
            text = self._removeDiacritics(text)
        
        return text

    def PostNormalize(self, text: str) -> str:
        """
        1. Canonicalizes the text
        2. Replaces Kashmiri digits with English 
        3. Handles spaces before and after punctuations
        4. Modifies the text to follow Kashmiri writing rules
        
        Ideal for Post-Processing of ML models.
        Args:
            text (str): The input text

        Returns:
            str: The normalized text
        """
        text = self.normalize(text)
        text = self._handlePlatYe(text)
        return text
        