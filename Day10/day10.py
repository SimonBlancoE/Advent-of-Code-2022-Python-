with open('input') as f:
    inp = f.read().strip().split('\n')


def check_cycle():
    global cycle_check
    global sig_str_sum
    if len(cycle) == cycle_check:
        sig_str_sum += cycle[-1] * cycle_check
        cycle_check += 40


cycle = []
cycle_check = 20
x_reg = 1
sig_str_sum = 0
for index, row in enumerate(inp):
    check_cycle()
    try:
        op, n = row.split()
        for _ in range(2):
            cycle.append(x_reg)
            check_cycle()
        x_reg += int(n)
    except ValueError:
        op = 'noop'
        n = '0'
        cycle.append(x_reg)

print("Signal strength sum = ", sig_str_sum)