import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# Importing the methods
from Trapezoidal import trapezoidal_rule, trapezoidal_rule_discrete
from simpson_1_3 import simpson_1_3, simpson_1_3_func
from simpson_3_8 import simpson_3_8, simpson_3_8_discrete
from midpoint import midpoint_rule, midpoint_rule_discrete

# MATPLOT FOR GRAPHS
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

# Main function
def main():
    st.title("Numerical Integration Methods")

    method = st.sidebar.selectbox(
        "Select Integration Method",
        ["Midpoint Rule","Trapezoidal Rule", "Simpson's 1/3 Rule", "Simpson's 3/8 Rule"]
    )
    st.sidebar.title("""
    Prepared By:\n
    Hamza Kamelen 22F-BSAI-09\n
    Muzamil Khalid 22F-BSAI-29\n
    Moiz Mansoori 22F-BSAI-32\n
    Wajahat Tariq 22F-BSAI-17\n
    Rayyan Ahmed 22F-BSAI-11\n
    Muhammad Sami 22F-BSAI-43             
    """)
    st.header(method)

    # Common inputs
    function_str = st.text_input("Enter function (use 'x' as variable)", value="x**2")
    a = st.number_input("Lower bound (a)", value=0)
    b = st.number_input("Upper bound (b)", value=1)
    n = st.number_input("Number of subintervals", min_value=1, value=4)

    try:
        f = lambda x: eval(function_str)
        # Test the function
        f(1)
    except Exception as e:
        st.error(f"Invalid function. Please enter a valid Python expression. Error: {str(e)}")
        return

    integration_option = st.radio(
        "Choose integration type",
        ["Continuous function", "Discrete data points"]
    )

    if integration_option == "Continuous function":
        if method == "Midpoint Rule":
            st.write("""Formula:
                    ∫[a to b] f(x) dx ≈ h * Σ[i=1 to n] f(x_i)
                     """)
            result = midpoint_rule(f, a, b, n)
        elif method == "Simpson's 1/3 Rule":
            if n % 2 != 0:
                st.warning("Number of subintervals must be even for Simpson's 1/3 Rule. Adjusting to the next even number.")
                n += 1
            st.write("""Formula:
                    ∫ydx= (h/3) (y0+4(y1+y3+...+yn-1)+2(y2+y4+...+yn-2)+yn)
                     """)
            result = simpson_1_3_func(f, a, b, n)
        elif method == "Simpson's 3/8 Rule":
            if n % 3 != 0:
                st.warning("Number of subintervals must be a multiple of 3 for Simpson's 3/8 Rule. Adjusting to the next multiple of 3.")
                n += (3 - n % 3)
            st.write("""Formula:
                    ∫ydx = 3h/8 (y0 + 2(y3+y6+...+yn-3) + 3(y1+y2+y4+y5+...+yn-2+yn-1) + yn)
                     """)
            result = simpson_3_8(f, a, b, n)
        elif method == "Trapezoidal Rule":
            st.write("""Formula:
            ∫ydx = h/2 (y0 + 2(y1 + y2 + ... + yn-1) + yn)""")
            result = trapezoidal_rule(f, a, b, n)

        # Calculate actual value
        actual, _ = integrate.quad(f, a, b)

        st.write(f"Estimated value: {result}")
        st.write(f"Actual value: {actual}")
        st.write(f"Error: {abs(actual - result)}")

        # Visualization
        fig = plot_integration(f, a, b, n, method.split()[0])
        st.pyplot(fig)

    else:  # Discrete data points
        x_values = st.text_input("Enter x values (comma-separated)")
        y_values = st.text_input("Enter y values (comma-separated)")

        if x_values and y_values:
            try:
                x = [float(x.strip()) for x in x_values.split(",")]
                y = [float(y.strip()) for y in y_values.split(",")]

                if len(x) != len(y):
                    st.error("The number of x values must be equal to the number of y values.")
                    return

                if len(x) < 2:
                    st.error("At least two data points are required for integration.")
                    return

                if method == "Midpoint Rule":
                    result = midpoint_rule_discrete(x, y)
                elif method == "Simpson's 1/3 Rule":
                    if len(x) % 2 == 0:
                        st.warning("Number of points must be odd for Simpson's 1/3 Rule. Removing the last point.")
                        x = x[:-1]
                        y = y[:-1]
                    if len(x) < 3:
                        st.error("At least three points are required for Simpson's 1/3 Rule.")
                        return
                    result = simpson_1_3(x, y)
                elif method == "Simpson's 3/8 Rule":
                    if len(x) % 3 != 1:
                        st.warning("Number of points must be of the form 3n + 1 for Simpson's 3/8 Rule. Removing extra points.")
                        x = x[:-(len(x) % 3) + 1]
                        y = y[:-(len(y) % 3) + 1]
                    if len(x) < 4:
                        st.error("At least four points are required for Simpson's 3/8 Rule.")
                        return
                    result = simpson_3_8_discrete(x, y)
                elif method == "Trapezoidal Rule":
                    result = trapezoidal_rule_discrete(x, y)

                st.write(f"Estimated value: {result}")

                # Plot discrete data points
                fig, ax = plt.subplots()
                ax.plot(x, y, 'ro-', linewidth=2, markersize=4)
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.set_title(f'{method} - Discrete Data Points')
                st.pyplot(fig)

            except Exception as e:
                st.error(f"Error processing discrete data: {str(e)}")
        else:
            st.warning("Please enter both x and y values for discrete data points.")

if __name__ == "__main__":
    main()