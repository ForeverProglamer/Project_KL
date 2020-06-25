import memory_buffer
import sumator
rounding_length = 6


def table_code_generator(mantis_x, mantis_y, operation_parameter):
    maximum_number_for_counter = max(len(mantis_x), len(mantis_y)) + operation_parameter
    code_table = {}
    for number in range(maximum_number_for_counter):
        code_table[number] = str(bin(number))[2:]
    normal_length_for_counter = len(code_table[maximum_number_for_counter - 1])
    for key in code_table.keys():
        line_for_transform = code_table[key]
        while len(line_for_transform) < normal_length_for_counter:
            line_for_transform = "0" + line_for_transform
        code_table[key] = line_for_transform
    return code_table


def type_converter(arg_list, type_flag):
    for number in range(len(arg_list)):
        arg_list[number] = type_flag(arg_list[number])


def record_corector(arg_list):
    return ''.join(str(arg_list).replace('[', '').replace(']', '').replace(', ', '').replace(',', '').replace("'", ''))


def make_records(counter, rg1, rg2, rg3, mo, ct=None, on=0):
    tact_line = list()
    tact_line.append(str(counter))
    tact_line.append(record_corector(rg1))
    tact_line.append(record_corector(rg2))
    tact_line.append(record_corector(rg3))
    if ct is not None:
        tact_line.append(ct)
    tact_line.append(record_corector(mo))
    memory_buffer.write_one_line(on, tact_line)


def set_rounding_length(first_mantis):
    global rounding_length
    rounding_length = len(first_mantis)


def normalization(order, mantis):
    """All variables must be list."""
    while mantis[0] == 0:
        mantis.reverse()
        mantis.pop()
        mantis.reverse()
        mantis.append(0)
        sumator.full_addition_procedure(order, [0, 1], True)
        order = sumator.sumator_answer


def rounding(mantis):
    if len(mantis) > rounding_length:
        list_with_one = [0 for i in range(rounding_length)]
        list_with_one.append(1)
        return sumator.use_only_sumator_core(rounding_length + 1, mantis, list_with_one)[:rounding_length]
    else:
        return mantis


def save_results_in_buffer(operation_number, order_of_operation, sign_of_operation, mantis_of_operation):
    normalization(order_of_operation, mantis_of_operation)
    mantis_of_operation = rounding(mantis_of_operation)
    order_of_operation = record_corector(order_of_operation)
    sign_of_operation = record_corector(sign_of_operation)
    mantis_of_operation = record_corector(mantis_of_operation)
    memory_buffer.write_answer(operation_number, sign_of_operation, mantis_of_operation)
    memory_buffer.write_order(operation_number, order_of_operation)
