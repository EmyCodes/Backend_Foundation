#!/usr/bin/python3
""" program that prints all the names defined
by the compiled module hidden_4.pyc """


if __name__ == "__main__":
    import hidden_4

    results = dir(hidden_4)
    for result in results:
        if result[:2] != "__":
            print(result)
