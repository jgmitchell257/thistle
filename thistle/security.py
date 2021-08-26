import random


def load_word_list() -> list:
    """Load /usr/share/dict/words file

    Returns:
        list: cleaned contents of /usr/share/dict/words
    """
    with open("/usr/share/dict/words", "r") as words:
        word_list = words.readlines()
        cleaned_list = []
        for word in word_list:
            w = word.strip("\n")
            cleaned_list.append(w)
        return cleaned_list


def create_passphrase(x: int) -> str:
    """Create a passphrase that is x words long

    Args:
        x (int): Number of words to sample from the word list

    Returns:
        str: passphrase
    """
    with open("/usr/share/dict/words", "r") as words:
        word_list = words.readlines()
        passphrase_list = random.sample(word_list, k=x)
        random.shuffle(passphrase_list)
        cleaned_list = []
        for word in passphrase_list:
            w = word.strip("\n")
            cleaned_list.append(w)
        return "-".join(cleaned_list)
