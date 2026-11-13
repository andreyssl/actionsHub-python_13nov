from greet import greet_user


def test_greet_user(capsys):
    greet_user("Alice")
    captured = capsys.readouterr()
    assert captured.out == "Hello Alice\n"

def test_greet_user_different_name(capsys):
    greet_user("Bob")
    captured = capsys.readouterr()
    assert captured.out == "Hello Bob\n"
