import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def plot_function_and_revolution(function_str, variable, lower_bound, upper_bound, axis='x'):
    x = sp.symbols(variable)
    function_expr = sp.sympify(function_str.replace('np.', ''))

    f = sp.lambdify(x, function_expr, 'numpy')

    x_vals = np.linspace(lower_bound, upper_bound, 400)
    y_vals = f(x_vals)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x_vals, y_vals, label=f"f({variable}) = {function_str}")

    if axis == 'x':
        ax.fill_between(x_vals, y_vals, alpha=0.2)
        volume = sp.integrate(sp.pi * function_expr ** 2, (x, lower_bound, upper_bound))
        ax.set_title(f'Volume of Revolution around X-axis: {volume.evalf():.2f}')
    elif axis == 'y':
        ax.fill_betweenx(y_vals, x_vals, alpha=0.2)
        volume = sp.integrate(sp.pi * function_expr ** 2, (x, lower_bound, upper_bound))
        ax.set_title(f'Volume of Revolution around Y-axis: {volume.evalf():.2f}')
    else:
        raise ValueError("Axis must be 'x' or 'y'.")

    ax.set_xlabel(variable)
    ax.set_ylabel('f(x)')
    ax.legend()
    ax.grid(True)
    plt.show()
