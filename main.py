# Доработать класс FlatIterator в коде ниже.
# Должен получиться итератор, который принимает список списков и возвращает их плоское представление,
# т.е последовательность состоящую из вложенных элементов.
# Функция test в коде ниже также должна отработать без ошибок.

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list


    def __iter__(self):
        self.ln_main = len(self.list_of_list)
        self.cursor = 0
        self.templist = []

        return self

    def __next__(self):

        if self.cursor == self.ln_main:
            raise StopIteration

        if type(self.list_of_list[self.cursor]) == list:
            if len(self.list_of_list[self.cursor]) > 1:
                element = self.list_of_list[self.cursor].pop(0)
                if type(element) == list:
                    item = FlatIterator(element)
                else:
                    item = element

        else:
            item = self.list_of_list[self.cursor]
            self.cursor += 1
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()