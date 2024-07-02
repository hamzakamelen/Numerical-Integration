import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Importing the methods
from Trapezoidal import trapezoidal_rule, trapezoidal_rule_discrete, trapezoidal_rule_interactive
from simpson_1_3 import simpson_1_3, simpson_1_3_func
from simpson_3_8 import simpson_3_8
from midpoint import midpoint_rule

def plot_integration(f, a, b, n, method):
    x = np.linspace(a, b, 200)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'b-', label='f(x)')

    dx = (b - a) / n
    x_points = np.linspace(a, b, n + 1)
    y_points = f(x_points)

    if method == "Midpoint":
        for i in range(n):
            x_mid = (x_points[i] + x_points[i + 1]) / 2
            y_mid = f(x_mid)
            ax.add_patch(plt.Rectangle((x_points[i], 0), dx, y_mid, fill=False, edgecolor='r'))
    elif method in ["Simpson's 1/3", "Simpson's 3/8", "Trapezoidal"]:
        ax.fill_between(x, y, alpha=0.3)
        ax.plot(x_points, y_points, 'ro-', linewidth=2, markersize=4)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.set_title(f'{method} Rule Visualization')

    return fig

def main():
    st.title("Numerical Integration Methods")

    method = st.sidebar.selectbox(
        "Select Integration Method",
        ["Midpoint Rule", "Simpson's 1/3 Rule", "Simpson's 3/8 Rule", "Trapezoidal Rule"]
    )

    st.header(method)

    # Common inputs
    function_str = st.text_input("Enter function (use 'x' as variable)", value="x**2")
    a = st.number_input("Lower bound (a)", value=0.0)
    b = st.number_input("Upper bound (b)", value=1.0)
    n = st.number_input("Number of subintervals", min_value=1, value=4)

    try:
        f = lambda x: eval(function_str)
    except:
        st.error("Invalid function. Please enter a valid Python expression.")
        return

    if method == "Midpoint Rule":
        result = midpoint_rule(f, a, b, n)

    #------------------
    elif method == "Simpson's 1/3 Rule":
        simpson_option = st.radio(
            "Choose Simpson's 1/3 Rule type",
            ["Continuous function", "Discrete data points"]
        )

        if simpson_option == "Continuous function":
            if n % 2 != 0:
                st.warning(
                    "Number of subintervals must be even for Simpson's 1/3 Rule. Adjusting to the next even number.")
                n += 1
            result = simpson_1_3_func(f, a, b, n)
        else:
            x_values = st.text_input("Enter x values (comma-separated)")
            fx_values = st.text_input("Enter f(x) values (comma-separated)")

            if x_values and fx_values:
                x = [float(x.strip()) for x in x_values.split(",")]
                fx = [float(fx.strip()) for fx in fx_values.split(",")]
                if len(x) % 2 == 0:
                    st.warning("Number of points must be odd for Simpson's 1/3 Rule. Removing the last point.")
                    x = x[:-1]
                    fx = fx[:-1]
                result = simpson_1_3(x, fx)
            else:
                st.warning("Please enter both x and f(x) values.")
                return

        #-------
    elif method == "Simpson's 3/8 Rule":
        if n % 3 != 0:
            st.warning("Number of subintervals must be a multiple of 3 for Simpson's 3/8 Rule. Adjusting to the next multiple of 3.")
            n += (3 - n % 3)
        result = simpson_3_8(f, a, b, n)
    elif method == "Trapezoidal Rule":
        trapezoidal_option = st.radio(
            "Choose Trapezoidal Rule type",
            ["Continuous function", "Discrete data points"]
        )

        if trapezoidal_option == "Continuous function":
            result = trapezoidal_rule(f, a, b, n)
        else:
            x_values = st.text_input("Enter x values (comma-separated)")
            fx_values = st.text_input("Enter f(x) values (comma-separated)")

            if x_values and fx_values:
                x = [float(x.strip()) for x in x_values.split(",")]
                fx = [float(fx.strip()) for fx in fx_values.split(",")]
                result = trapezoidal_rule_discrete(x, fx)
            else:
                st.warning("Please enter both x and f(x) values.")
                return

    # For demonstration purposes, actual value for x^2 integration
    actual = (b ** 3 - a ** 3) / 3  # Actual value for x^2 if that's the function
    st.write(f"Estimated value: {result}")
    st.write(f"Actual value: {actual}")
    st.write(f"Error: {abs(actual - result)}")

    # Visualization
    fig = plot_integration(f, a, b, n, method.split()[0])
    st.pyplot(fig)

if __name__ == "__main__":
    main()