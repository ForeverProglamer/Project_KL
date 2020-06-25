from memory_buffer import orders_memory, answers_memory
import multiplication
import division
import addition
import square
import instruments_for_all_operations


def calculate_all(order_x, order_y, sign_x, sign_y, mantis_x, mantis_y):
    instruments_for_all_operations.set_rounding_length(mantis_x)
    multiplication.calculate(0, order_x, order_y, sign_x, sign_y, mantis_x, mantis_y)
    multiplication.calculate(1, orders_memory[0], order_y, answers_memory[0][0], sign_y, answers_memory[0][1], mantis_y)
    multiplication.calculate(2, orders_memory[1], order_y, answers_memory[1][0], sign_y, answers_memory[1][1], mantis_y)
    multiplication.calculate(3, orders_memory[2], order_y, answers_memory[2][0], sign_y, answers_memory[2][1], mantis_y)
    division.calculate(4, orders_memory[3], order_y, answers_memory[3][0], sign_y, answers_memory[3][1], mantis_y)
    division.calculate(5, orders_memory[4], order_y, answers_memory[4][0], sign_y, answers_memory[4][1], mantis_y)
    addition.calculate(orders_memory[5], order_y, answers_memory[5][0], sign_y, answers_memory[5][1], mantis_y)
    square.calculate(orders_memory[6], answers_memory[6][0], answers_memory[6][1])
