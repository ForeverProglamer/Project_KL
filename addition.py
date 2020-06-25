from instruments_for_all_operations import *


def calculate(order_x, order_y, sign_x, sign_y, mantis_x, mantis_y):
    """All variables must have type string."""
    operation_number = 6
    memory_buffer.clear_operation(operation_number)
    order_of_operation = list()
    mantis_of_operation = list()
    sign_of_operation = list()
    number_of_digits = len(mantis_x) # 6
    order_x_in_list = list(order_x)
    order_y_in_list = list(order_y)
    mantis_x_in_list = list(mantis_x)
    mantis_y_in_list = list(mantis_y)
    type_converter(order_x_in_list, int)
    type_converter(order_y_in_list, int)
    type_converter(mantis_x_in_list, int)
    type_converter(mantis_y_in_list, int)
    sumator.full_addition_procedure(order_x_in_list, order_y_in_list, True)
    order_difference = sumator.sumator_answer
    order_difference.reverse()
    sign_of_order_difference = order_difference.pop()
    order_difference.reverse()
    type_converter(order_difference, str)
    order_difference_decade = int("".join(order_difference), 2)
    mantis_for_mudslide = list()
    if sign_of_order_difference:
        mantis_for_mudslide.extend(mantis_x_in_list)
        order_of_operation.extend(order_y_in_list)
    else:
        mantis_for_mudslide.extend(mantis_y_in_list)
        order_of_operation.extend(order_x_in_list)
    code_table = table_code_generator("", "", order_difference_decade + 1)
    k = 0
    microoperations = list()
    microoperations.append("RG:= {0}".format(mantis_for_mudslide))
    microoperations.append("CT:={0}".format(code_table[order_difference_decade]))
    make_records(k, mantis_for_mudslide, "", "", microoperations, code_table[order_difference_decade], operation_number)
    while order_difference_decade > 0:
        k += 1
        order_difference_decade -= 1
        microoperations = list()
        mantis_for_mudslide.pop()
        mantis_for_mudslide.insert(0, 0)
        microoperations.append("RG:= 0.r(RG)")
        microoperations.append("CT:= CT – 1")
        if order_difference_decade == 0:
            microoperations.append("CT:= 0")
        make_records(k, mantis_for_mudslide, "", "", microoperations, code_table[order_difference_decade], operation_number)
    if sign_of_order_difference:
        mantis_for_mudslide.insert(0, int(sign_x))
        mantis_y_in_list.insert(0, int(sign_y))
        sumator.full_addition_procedure(mantis_for_mudslide, mantis_y_in_list)
    else:
        mantis_for_mudslide.insert(0, int(sign_y))
        mantis_x_in_list.insert(0, int(sign_x))
        sumator.full_addition_procedure(mantis_x_in_list, mantis_for_mudslide)
    answer_before_normalization = sumator.sumator_answer
    answer_before_normalization.reverse()
    sign_of_operation.append(answer_before_normalization.pop())
    answer_before_normalization.reverse() # 7?
    if len(answer_before_normalization) == number_of_digits:
        if answer_before_normalization[0] != sign_of_operation[0] and sign_of_operation[0] == 1:
            while number_of_digits > 0:
                answer_before_normalization.reverse()
                answer_before_normalization.pop()
                answer_before_normalization.reverse()
                answer_before_normalization.append(0)
                sumator.full_addition_procedure(order_of_operation, [0, 1], True)
                order_of_operation = sumator.sumator_answer
                number_of_digits -= 1
                if answer_before_normalization[0] == sign_of_operation[0]:
                    break
        elif sign_of_operation[0] == 0 and answer_before_normalization[0] == sign_of_operation[0]:
            while number_of_digits > 0:
                answer_before_normalization.reverse()
                answer_before_normalization.pop()
                answer_before_normalization.reverse()
                answer_before_normalization.append(0)
                sumator.full_addition_procedure(order_of_operation, [0, 1], True)
                order_of_operation = sumator.sumator_answer
                number_of_digits -= 1
                if answer_before_normalization[0] != sign_of_operation[0]:
                    break
    else:
        sumator.full_addition_procedure(order_of_operation, [0, 1])
        order_of_operation = sumator.sumator_answer
    mantis_of_operation.extend(answer_before_normalization)
    mantis_of_operation = rounding(mantis_of_operation)
    memory_buffer.orders_memory[6] = record_corector(order_of_operation)
    memory_buffer.answers_memory[6][0] = record_corector(sign_of_operation)
    memory_buffer.answers_memory[6][1] = record_corector(mantis_of_operation)
