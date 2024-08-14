import sympy as sp
import numpy as np


def get_volume_of_revolution(function_str, variable, lower_bound, upper_bound, axis='x'):
    x = sp.symbols(variable)

    # Convert the function string to a sympy expression
    try:
        # Handle numpy functions
        function_expr = sp.sympify(function_str.replace('np.', ''), evaluate=False)
    except Exception as e:
        raise ValueError(f"Failed to parse the function: {e}")

    if axis == 'x':
        volume = sp.integrate(sp.pi * function_expr ** 2, (x, lower_bound, upper_bound))
    elif axis == 'y':
        volume = sp.integrate(sp.pi * function_expr ** 2, (x, lower_bound, upper_bound))
    else:
        raise ValueError("Axis must be 'x' or 'y'.")

    return volume.evalf()
