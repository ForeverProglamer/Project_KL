import sumator
from instruments_for_all_operations import *


def calculate(operation_number, order_x, order_y, sign_x, sign_y, mantis_x, mantis_y):
    """All variables must have type string."""
    operation_number = int(operation_number)
    memory_buffer.clear_operation(operation_number)
    order_of_operation = list()
    mantis_of_operation = list()
    code_table = table_code_generator(mantis_x, mantis_y, 1)
    number_of_digits = len(mantis_x)
    order_x_in_list = list(order_x)
    order_y_in_list = list(order_y)
    mantis_x_in_list = list(mantis_x)
    mantis_y_in_list = list(mantis_y)
    type_converter(order_x_in_list, int)
    type_converter(order_y_in_list, int)
    type_converter(mantis_x_in_list, int)
    type_converter(mantis_y_in_list, int)
    sumator.full_addition_procedure(order_x_in_list, order_y_in_list)
    order_of_operation.extend(sumator.sumator_answer)
    sign_x_in_list = list(sign_x)
    sign_y_in_list = list(sign_y)
    type_converter(sign_x_in_list, int)
    type_converter(sign_y_in_list, int)
    sign_of_operation = sumator.use_only_sumator_core(1, sign_x_in_list, sign_y_in_list)

    if operation_number == 0:
        RG1 = [0 for i in range(number_of_digits + 1)]
        RG2 = list()
        RG3 = [0]
        RG2.extend(mantis_x_in_list)
        RG3.extend(mantis_y_in_list)
        CT = code_table[number_of_digits]
        CT_count = number_of_digits
        k = 0
        microoperations = list()
        microoperations.append("RG1:= {0}".format(RG1))
        microoperations.append("RG2:= {0}".format(RG2))
        microoperations.append("RG3:= {0}".format(RG3))
        microoperations.append("CT:= {0}".format(CT))
        make_records(k, RG1, RG2, RG3, microoperations, code_table[CT_count])
        while CT_count != 0:
            k += 1
            microoperations = list()
            if RG2[number_of_digits - 1] == 1:
                make_records(k, "", "", RG3, "", "")
                RG1 = sumator.use_only_sumator_core(number_of_digits + 1, RG1, RG3)
                make_records("", RG1, "", "", "", "")
                microoperations.append("RG1: = RG1 + RG3")
            RG2.insert(0, RG1[number_of_digits])
            RG2.pop()
            RG1.insert(0, 0)
            RG1.pop()
            CT_count -= 1
            microoperations.append("RG2: = RG1[" + str(number_of_digits + 1) + "].r(RG2)")
            microoperations.append("RG1: = 0.r(RG1)")
            microoperations.append("CT = CT-1")
            if CT_count == 0:
                microoperations.append("CT = 0")
            make_records(k, RG1, RG2, RG3, microoperations, code_table[CT_count])
        RG1.extend(RG2)
        mantis_of_operation = RG1[1:2 * number_of_digits + 1]

    elif operation_number == 1:
        RG1 = [0 for i in range(2 * number_of_digits)]
        RG2 = list()
        RG3 = [0 for i in range(number_of_digits)]
        RG2.extend(mantis_x_in_list)
        RG3.extend(mantis_y_in_list)
        k = 0
        microoperations = list()
        microoperations.append("RG1:= {0}".format(RG1))
        microoperations.append("RG2:= {0}".format(RG2))
        microoperations.append("RG3:= {0}".format(RG3))
        make_records(k, RG1, RG2, RG3, microoperations, on=operation_number)
        while sum(RG2) != 0:
            k += 1
            microoperations = list()
            if RG2[number_of_digits - 1] == 1:
                make_records(k, "", "", RG3, "", on=operation_number)
                RG1 = sumator.use_only_sumator_core(2 * number_of_digits, RG1, RG3)
                make_records("", RG1, "", "", "", on=operation_number)
                microoperations.append("RG1: = RG1 + RG3")
            RG3.reverse()
            RG3.pop()
            RG3.reverse()
            RG3.insert(len(RG3), 0)
            RG2.pop()
            RG2.insert(0, 0)
            microoperations.append("RG3: = l(RG3).0")
            microoperations.append("RG2: = 0.r(RG2)")
            make_records(k, RG1, RG2, RG3, microoperations, on=operation_number)
        mantis_of_operation.extend(RG1)

    elif operation_number == 2:
        RG1 = [0 for i in range(number_of_digits)]
        RG2 = list()
        RG2.extend(mantis_x_in_list)
        RG2.append(0)
        RG3 = list()
        RG3.extend(mantis_y_in_list)
        CT = number_of_digits
        second_number = list()
        second_number.extend([0 for i in range(number_of_digits + 1)])
        second_number.extend(RG3)
        k = 0
        microoperations = list()
        microoperations.append("RG1: ={0}".format(RG1))
        microoperations.append("RG2: ={0}".format(RG2))
        microoperations.append("RG3: ={0}".format(RG3))
        microoperations.append("CT: ={0}".format(code_table[CT]))
        make_records(k, RG1, RG2, RG3, microoperations, code_table[CT], operation_number)
        while CT != 0:
            k += 1
            microoperations = list()
            first_number = list()
            first_number.extend(RG2)
            first_number.extend(RG1)
            suma_list = list()
            suma_list.extend([0 for i in range(2 * number_of_digits + 1)])
            if RG2[0] == 1:
                suma_list = sumator.use_only_sumator_core((2 * number_of_digits + 1), first_number, second_number)
                make_records(k, "", "", RG3, "", "", operation_number)
                RG2 = suma_list[0:number_of_digits + 1]
                RG1 = suma_list[number_of_digits + 1:2 * number_of_digits + 1]
                make_records("", RG1, RG2, "", "", "", operation_number)
                microoperations.append("RG1: = RG1 + RG3")
                microoperations.append("RG2: = RG2 + 0 + CI")
            RG1.reverse()
            CI = RG1.pop()
            RG1.reverse()
            RG1.insert(len(RG1), 0)
            RG2.reverse()
            RG2.pop()
            RG2.reverse()
            RG2.insert(len(RG2), CI)
            CT -= 1
            microoperations.append("RG1: = l(RG1).0")
            microoperations.append("RG2: = l(RG2).RG1[1]")
            microoperations.append("CT: = CT - 1")
            if CT == 0:
                microoperations.append("CT = 0")
            make_records(k, RG1, RG2, RG3, microoperations, code_table[CT], operation_number)
        RG2.extend(RG1)
        mantis_of_operation.extend(RG2[0:2 * number_of_digits])

    elif operation_number == 3:
        RG1 = [0 for i in range(2 * number_of_digits)]
        RG2 = list()
        RG2.extend(mantis_y_in_list)
        RG3 = list()
        RG3.append(0)
        RG3.extend(mantis_x_in_list)
        RG3.extend([0 for i in range(number_of_digits - 1)])
        k = 0
        microoperations = list()
        microoperations.append("RG1: ={0}".format(RG1))
        microoperations.append("RG2: ={0}".format(RG2))
        microoperations.append("RG3: ={0}".format(RG3))
        make_records(k, RG1, RG2, RG3, microoperations, on=operation_number)
        while sum(RG2) != 0:
            k += 1
            microoperations = list()
            if RG2[0] == 1:
                make_records("", "", "", RG3, "", on=operation_number)
                RG1 = sumator.use_only_sumator_core(2 * number_of_digits, RG1, RG3)
                make_records("", RG1, "", "", "", on=operation_number)
                microoperations.append("RG1: = RG1 + RG3")
            RG3.insert(0, 0)
            RG3.pop()
            RG2.reverse()
            RG2.pop()
            RG2.reverse()
            RG2.insert(len(RG2), 0)
            microoperations.append("RG3: = 0.r(RG3)")
            microoperations.append("RG2: = l(RG2).0")
            make_records(k, RG1, RG2, RG3, microoperations, on=operation_number)
        mantis_of_operation.extend(RG1)
    save_results_in_buffer(operation_number, order_of_operation, sign_of_operation, mantis_of_operation)
