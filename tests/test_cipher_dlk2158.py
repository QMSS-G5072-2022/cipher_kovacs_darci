from cipher_dlk2158 import cipher_dlk2158
def test_single_word():
    example = 'Hello'
    expected = 'Ifmmp'
    actual = cipher(example,1)
    assert actual == expected