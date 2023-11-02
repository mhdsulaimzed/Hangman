from hangman import get_random_words
import os





def test_for_lowercase():
    exfile = "/tmp/sample_words"
    with open(exfile, 'w') as f:
        f.writelines( ["Apple","apple","Banana"] )

    for i in exfile:


        assert get_random_words(exfile) == "apple"
    os.unlink(sample_words)



