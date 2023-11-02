from hangman import get_random_words
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
        f.writelines( ["Apple's\n","pIneapple\n","B#anana\n"] )

    for _ in range(100):


        assert get_random_words(fname) == "pIneapple"
    os.unlink(fname)



