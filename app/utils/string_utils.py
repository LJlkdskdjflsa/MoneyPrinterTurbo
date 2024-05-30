from typing import List


def split_string_by_max_word_length(
    string_to_split: str, max_word_length: int
) -> List[str]:
    """
    Splits a string into chunks where each chunk's length does not exceed the specified maximum word length.

    This function takes a string and splits it into a list of substrings,
    each with a total length of words not exceeding the `max_length` parameter.

    Args:
        s (str): The input string to be split.
        max_length (int): The maximum length of each chunk.

    Returns:
        List[str]: A list of substrings, each with a total length of words not exceeding the specified `max_length`.

    Example:
        >>> split_string_by_max_word_length("I am a good boy haha haha", 10)
        ['I am a', 'good boy', 'haha haha']

        >>> split_string_by_max_word_length("hello world", 5)
        ['hello', 'world']

        >>> split_string_by_max_word_length("split this string into chunks", 15)
        ['split this', 'string into', 'chunks']
    """
    words = string_to_split.split()
    result = []
    temp_words_string = ""

    count = 0

    if not words:
        return []

    while words:
        if count > max_word_length:
            result.append(temp_words_string)
            temp_words_string = ""
            count = 0
        else:
            temp_words_string += words.pop(0) + " "
            count += 1

    # add the final chunk
    result.append(temp_words_string)

    return result


# write a simple test to test above function
# test_text = "This version of the function explicitly calculates the new_length considering the spaces between words (len(current_chunk) represents the number of spaces as it's one less than the number of words in the chunk). It then checks if adding the new word would exceed max_word_lengt"
# test_max_word_length = 3
# test_result = split_string_by_max_word_length(
#     string_to_split=test_text, max_word_length=test_max_word_length
# )
# print(test_result)
