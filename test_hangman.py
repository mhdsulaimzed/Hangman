from hangman import get_random_words,get_masked_word,get_status,play_game
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

    assert get_status(word,guesses,turns_remaining) == """Word:s----- \n Guesses so far:sx \n Turns remaining: 75  """
           
def test_for_playgame_right_guess():
    word="shastri"
    turns_remining=7
    guesses=[]
    guess="h"


    guesses,turns_remining,action = play_game(word,guesses,guess,turns_remining)

    assert guesses == ["h"]
    assert turns_remining == 7
    action == "next"

def test_for_playgame_wrong_guess_game_not_over():
    word="shastri"
    turns_remining=8
    guesses=["x"]
    guess="y"


    guesses,turns_remining,action = play_game(word,guesses,guess,turns_remining)

    assert guesses == ["x","y"]
    assert turns_remining == 7
    assert action == "next"

def test_for_playgame_wrong_guess_game_over():
    word="shastri"
    turns_remaining=1
    guesses=["q"]
    guess="x"

    guesses,turns_remaining,action = play_game(word,guesses,guess,turns_remaining)
    assert guesses == ["q","x"]
    assert turns_remaining == 0
    assert action == "game_over"

def test_for_play_game_win():
    word = "shatri"
    turns_remaining=2
    guesses=["s","h","a","t","r"]
    guess="i"
    guesses,turns_remaining,action = play_game(word,guesses,guess,turns_remaining)

    
    assert action == "game_won"

def test_for_repeated_guesses():
    word = "sulaim"
    turns_remaining=3
    guesses=["s"]
    guess="u"

    guesses,turns_remaining,action = play_game(word,guesses,guess,turns_remaining)

    assert guesses == ["s","u"]
    assert turns_remaining == 3
    assert action == "next"

