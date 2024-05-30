import pytest
from app.utils.string_utils import split_string_by_max_word_length

def test_split_string_by_max_word_length_basic():
    s = "I am a good boy haha haha"
    max_length = 10
    expected = ["I am a", "good boy", "haha haha"]
    assert split_string_by_max_word_length(s, max_length) == expected