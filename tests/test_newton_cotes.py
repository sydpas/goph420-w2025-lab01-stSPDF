import numpy as np

from src.goph420_lab01.integration import (
    integrate_newton
)

def test_newton_trap():
    x = np.linspace(-2, 5, 50)

    # constant func
    f0 = 5.0 * np.ones_like(x)
    # linear func
    f1 = -2.5 + 0.6 * x

    # exp integral
    I0_exp = f0[0] * (x[-1] - x[0])
    # test with 2 points
    I0_act_2 = integrate_newton([x[0], x[-1]],[f0[0], f0[-1]],'trap')
    # test with all points
    I0_act_all = integrate_newton(x, f0, 'trap')

    print("Testing trapezoid rule...")
    print(f'f(x) = {f0[0]} from x = {x[0]} to x = {x[-1]}...')
    print(f'Expected: {I0_exp}')
    print(f'Actual (2 data points): {I0_act_2}')
    print(f'Actual ({len(x)} data points): {I0_act_all}')


def test_newton_simp():
    x = np.linspace(-3, 5, 101)

    # constant func
    f0 = 5.0 * np.ones_like(x)
    # linear func
    f1 = -2.5 + 0.6 * x

    # exp integral
    I0_exp = f0[0] * (x[-1] - x[0])
    # test with 3 points
    I0_act_3 = integrate_newton([x[0], x[len(x) // 2], x[-1]], [f0[0], f0[len(f0) // 2], f0[-1]], 'simp')
    # test with all points
    I0_act_all = integrate_newton(x, f0, 'simp')

    print("Testing Simpson's 1/3 rule...")
    print(f'f(x) = {f0[0]} from x = {x[0]} to x = {x[-1]}...')
    print(f'Expected: {I0_exp}')
    print(f'Actual (3 data points): {I0_act_3}')
    print(f'Actual ({len(x)} data points): {I0_act_all}')

if __name__ == "__main__":
    test_newton_trap()
    test_newton_simp()