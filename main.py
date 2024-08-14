from math_functions import get_volume_of_revolution
from plotter import plot_function_and_revolution


def get_user_input():
    function = input("Enter the function f(x) (use 'np.' for numpy functions, e.g., 'np.exp(x)'): ")
    lower_bound = float(input("Enter the lower bound for x: "))
    upper_bound = float(input("Enter the upper bound for x: "))
    axis = input("Enter the axis of rotation (x/y): ").lower()
    return function, lower_bound, upper_bound, axis


def main():
    function, lower_bound, upper_bound,axis = get_user_input()

    try:
        # Calculate volume
        volume = get_volume_of_revolution(function, 'x', lower_bound, upper_bound, axis)
        print(
            f"\nThe volume of the solid of revolution around the {axis}-axis is approximately {volume:.2f} cubic units.")

        # Plot the function and solid
        plot_function_and_revolution(function, 'x', lower_bound, upper_bound, axis)
    except Exception as e:
        print(f"An error occurred: {e}")

main()