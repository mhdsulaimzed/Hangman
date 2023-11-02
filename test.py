from hangman import get_random_words,masking_random_word
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


def test_for_mask_random_words():
    assert masking_random_word("dimple") == "______"




