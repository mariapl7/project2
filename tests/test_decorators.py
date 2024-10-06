from src.decorators import log


def test_log(capsys):
    @log
    def my_function(x, y):
        return x + y

    result = my_function(1,2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok"
    assert result == 3


def test_log_exception(filename="mylog.txt"):
    @log(filename)
    def my_function(x, y):
        return x / y

    my_function(1, 2)
    with open(filename, "r") as file:
        message = file.read()
    assert message == "my_function error: Inputs: (1, 0), {}\n"


# def test_log_exception():
#     with pytest.raises(Exception, match="my_function error: Inputs: (1, 2), {}"):
#         my_function()
