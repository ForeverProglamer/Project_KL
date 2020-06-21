memory = [[], [], [], [], [], [], [], []]
orders_memory = [0, 0, 0, 0, 0, 0, 0, 0]
answers_memory = [[0, 0], [0, 0], [0, 0], [0, 0],
                  [0, 0], [0, 0], [0, 0], [0, 0]]


def write_one_line(operation_number, data):
    memory[operation_number].append(data)


def get_the_lines_one_by_one(operation_number):
    for line in memory[operation_number]:
        yield line


def write_order(operation_number, data):
    orders_memory[operation_number] = data


def get_order(operation_number):
    return orders_memory[operation_number]


def write_answer(operation_number, sign, mantis):
    answers_memory[operation_number][0] = sign
    answers_memory[operation_number][1] = mantis


def get_answer(operation_number):
    return answers_memory[operation_number]


def clear_operation(operation_number=None):
    if operation_number is not None:
        global memory
        global orders_memory
        global answers_memory
        memory[operation_number] = []
        orders_memory[operation_number] = 0
        answers_memory[operation_number] = [0, 0]

# @todo check if wrong
def clear_all_operations():
    global memory
    global orders_memory
    global answers_memory
    memory = [[], [], [], [], [], [], [], []]
    orders_memory = [0, 0, 0, 0, 0, 0, 0, 0]
    answers_memory = [[0, 0], [0, 0], [0, 0], [0, 0],
                      [0, 0], [0, 0], [0, 0], [0, 0]]
