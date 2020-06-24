first_number_sign = list()
first_number_mantis = list()
second_number_sign = list()
second_number_mantis = list()
sumator_answer_sign = list()
sumator_answer_mantis = list()
sumator_answer = list()
needed_length = 0
transposition = 0


def bit_equalization(first_number, second_number):
    """It takes sign and equalize mantises."""
    global needed_length
    global first_number_sign
    global second_number_sign
    global first_number_mantis
    global second_number_mantis
    first_work_mantis = list()
    second_work_mantis = list()
    first_number_sign = list()
    second_number_sign = list()
    first_number_sign.append(first_number[0])
    first_work_mantis.extend(first_number[1:])
    second_number_sign.append(second_number[0])
    second_work_mantis.extend(second_number[1:])
    needed_length = max(len(first_work_mantis), len(second_work_mantis))
    first_work_mantis.reverse()
    second_work_mantis.reverse()
    while len(first_work_mantis) != needed_length:
        first_work_mantis.append(0)
    while len(second_work_mantis) != needed_length:
        second_work_mantis.append(0)
    first_work_mantis.reverse()
    second_work_mantis.reverse()
    first_number_mantis = first_work_mantis
    second_number_mantis = second_work_mantis


def mok_transform(sign, mantis):
    """It makes double sign and reverse mantis."""
    sign_digit = sign[0]
    sign.append(sign_digit)
    if sign_digit:
        for digit_index in range(len(mantis)):
            mantis[digit_index] = int(not bool(mantis[digit_index]))


def sumator_core(first_adder, second_adder):
    """It is find sum and make MDK, if this needed."""
    global transposition
    result_of_sum = [0 for digit in range(needed_length)]
    add_to_next_digit = first_number_sign[0] + second_number_sign[0]
    for index in range(needed_length - 1, -1, -1):
        suma = first_adder[index] + second_adder[index] + add_to_next_digit
        if suma == 0:
            result_of_sum[index] = 0
            add_to_next_digit = 0
        elif suma == 1:
            result_of_sum[index] = 1
            add_to_next_digit = 0
        elif suma == 2:
            result_of_sum[index] = 0
            add_to_next_digit = 1
        elif suma == 3:
            result_of_sum[index] = 1
            add_to_next_digit = 1
        elif suma == 4:
            result_of_sum[index] = 0
            add_to_next_digit = 2
    transposition = add_to_next_digit
    return result_of_sum


def answer_transform(answer):
    """It is transform mantis from MDK to PK."""
    global needed_length
    global sumator_answer_sign
    global sumator_answer_mantis
    global sumator_answer
    if answer[0] == answer[1]:
        answer.reverse()
        answer.pop()
        answer.reverse()
        needed_length -= 1
    sumator_answer_sign = answer[0]
    sumator_answer_mantis = list()
    sumator_answer_mantis.extend(answer[1:])
    if sumator_answer_sign:
        index_for_minus = len(sumator_answer_mantis) - 1
        while index_for_minus > -1 and sumator_answer_mantis[index_for_minus] != 1:
            index_for_minus -= 1
        if index_for_minus == -1:
            sumator_answer_sign = 0
        else:
            sumator_answer_mantis[index_for_minus] = 0
            for digit in range(index_for_minus + 1, needed_length - 1):
                sumator_answer_mantis[digit] = 1
            mok_transform([1], sumator_answer_mantis)
    sumator_answer = list()
    sumator_answer.append(sumator_answer_sign)
    sumator_answer.extend(sumator_answer_mantis)


def full_addition_procedure(first_number, second_number, minus=False):
    """It is main function."""
    if minus:
        second_number[0] = int(not bool(second_number[0]))
    bit_equalization(first_number, second_number)
    mok_transform(first_number_sign, first_number_mantis)
    mok_transform(second_number_sign, second_number_mantis)
    first_adder = list()
    first_adder.extend(first_number_sign)
    first_adder.extend(first_number_mantis)
    second_adder = list()
    second_adder.extend(second_number_sign)
    second_adder.extend(second_number_mantis)
    global needed_length
    needed_length += 2
    answer_transform(sumator_core(first_adder, second_adder))


def use_only_sumator_core(length, first_adder, second_adder):
    """It is function for registers."""
    global needed_length
    global first_number_sign
    global second_number_sign
    needed_length = length
    first_number_sign = [0]
    second_number_sign = [0]
    return sumator_core(first_adder, second_adder)
