import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# We'll import the specific functions later when they're needed

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
        from midpoint import midpoint_rule
        result = midpoint_rule(f, a, b, n)
    elif method == "Simpson's 1/3 Rule":
        from simpson_1_3 import simpson_1_3
        if n % 2 != 0:
            st.warning("Number of subintervals must be even for Simpson's 1/3 Rule. Adjusting to the next even number.")
            n += 1
        x = np.linspace(a, b, n+1)
        Fx = f(x)
        result = simpson_1_3(x, Fx, (b-a)/n)
    elif method == "Simpson's 3/8 Rule":
        from simpson_3_8 import simpsom_3_8
        if n % 3 != 0:
            st.warning("Number of subintervals must be a multiple of 3 for Simpson's 3/8 Rule. Adjusting to the next multiple of 3.")
            n += (3 - n % 3)
        x = np.linspace(a, b, n+1)
        Fx = f(x)
        result = simpsom_3_8(x, Fx, (b-a)/n)
    elif method == "Trapezoidal Rule":
        from trapezoidal import trapezoidal_rule
        result = trapezoidal_rule(f, a, b, n)

    st.write(f"Estimated value: {result}")

    # Visualization
    fig = plot_integration(f, a, b, n, method.split()[0])
    st.pyplot(fig)

if __name__ == "__main__":
    main()