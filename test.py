from hangman import get_random_words,get_masked_word,get_status
import os





def test_randomwords_for_lowercase():
    fname = "/tmp/sample_words"
    with open(fname, 'w') as f:
        f.writelines( ["Apple\n","apple\n","Banana\n"] )

    for _ in range(100):


        assert get_random_words(fname) == "apple"
    os.unlink(fname)


def test_randoms_for_punctuation():

    fname = "/tmp/sample_words"
    with open(fname, 'w') as f:
        f.writelines( ["Apple's\n","pineapple\n","B#anana\n"] )

    for _ in range(100):


        assert get_random_words(fname) == "pineapple"
    os.unlink(fname)



def test_randoms_of_length_of_five():

    fname = "/tmp/sample_words"
    with open(fname, 'w') as f:
        f.writelines( ["apples\n","pine\n","Bana\n"] )

    for _ in range(100):


        assert get_random_words(fname) == "apples"
    os.unlink(fname)


def test_random_words_not_reapeated():
    words={get_random_words() for i in range(10)}
    assert len(words) == 10

def test_mask_word_no_gusses():
    word="elephant"
    guesses=[]
    assert get_masked_word(word,guesses) == "--------"

def test_mask_word_single_wrong_guess():
    word="elephant"
    guesses=['x']
    assert get_masked_word(word,guesses) == "--------"

def test_mask_word_single_right_guess():
    word="elephant"
    guesses=['a']
    assert get_masked_word(word,guesses) == "-----a--"


def test_mask_word_two_right_guess():

    word="elephant"
    guesses=["a","p"]
    assert get_masked_word(word,guesses) == "---p-a--"


def test_mask_word_single_guess_multiple_occurrence():
    guesses = ['e', 'p','t']
    word = "elephant"
    masked_word = get_masked_word(word, guesses)
    assert masked_word == "e-ep---t"

def test_get_status():
    word="sulaim"
    turns_remaining=75
    guesses = ["s","x"]

    assert get_status(word,guesses,turns_remaining) == """Word:s-----
           Turns remaining:75
           Guessed so far:sx       """