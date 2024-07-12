from collections import deque


deq = deque([1, 2, 3, 4, 5])
empty_deq = deque()

deq_extended = deq
deq_insert = deq
deq_remove = deq


if __name__ == '__main__':
    try:
        value = empty_deq.popleft()
        print(value)
    except IndexError as err:
        print(f'Error text: {err}')
        print(f'{"*"*30}')

    deq_extended.extend([6, 7, 8])
    deq_extended.extendleft([0, -1, -2])
    print(deq_extended)
    print(f'{"*"*30}')

    deq_insert.insert(1, 200)
    print(deq_insert)
    print(f'{"*" * 30}')

    try:
        deq_remove.remove(4)
        print(deq_remove)
        print(f'{"*" * 30}')
    except ValueError as err:
        print(f'Error text: {err}')
        print(f'{"*" * 30}')