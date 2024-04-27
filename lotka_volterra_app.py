import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from fmpy import simulate_fmu

# Function to simulate the Lotka-Volterra model FMU
def simulate_lotka_volterra(alpha, beta, gamma, delta, x0, y0, duration):
    # Load the FMU
    fmu = 'Lotka_Volterra.fmu'

    # Set the input parameters
    parameters = {
        'alpha': alpha,
        'beta': beta,
        'gamma': gamma,
        'delta': delta,
        'x0': x0,
        'y0': y0
    }

    # Simulate the FMU
    result = simulate_fmu(fmu, start_time=0, stop_time=duration, start_values=parameters)

    # Extract simulation results
    time = result['time']
    x = result['x']
    y = result['y']

    return time, x, y

# Streamlit app
st.title('Lotka-Volterra Model Simulation')
st.markdown("""
The Lotka–Volterra equations, also known as the Lotka–Volterra predator–prey model, are a pair of first-order nonlinear differential equations, frequently used to describe the dynamics of biological systems in which two species interact, one as a predator and the other as prey. The populations change through time according to the pair of equations:

""")

# Define equations in LaTeX format
equation1 = r'\frac{dx}{dt} = \alpha x - \beta xy'
equation2 = r'\frac{dy}{dt} = \delta xy - \gamma y'

# Display equations using st.latex()
st.latex(equation1)
st.latex(equation2)

st.markdown("""
where:
- the variable $x$ is the population density of prey (for example, the number of rabbits per square kilometre).
- the variable $y$ is the population density of some predator (for example, the number of foxes per square kilometre).

Set the parameters on the left panel and click on Start Simulation to simulate and plot the results.
""")

st.link_button("Wikipedia page", "https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations")


# Input parameters
alpha = st.sidebar.number_input('Reproduction rate of prey (alpha)', value=0.1)
beta = st.sidebar.number_input('Mortality rate of prey per predator (beta)', value=0.02)
gamma = st.sidebar.number_input('Mortality rate of predator (gamma)', value=0.4)
delta = st.sidebar.number_input('Reproduction rate of predator per prey (delta)', value=0.02)
x0 = st.sidebar.number_input('Initial prey population density', value=10, step=1)
y0 = st.sidebar.number_input('Initial predator population density', value=10, step=1)
duration = st.sidebar.number_input('Simulation duration', value=100, step=1)

# Start Simulation button
if st.sidebar.button('Start Simulation'):
    time, x, y = simulate_lotka_volterra(alpha, beta, gamma, delta, x0, y0, duration)

    # Plot results
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(time, x, label='Prey')
    ax.plot(time, y, label='Predator')
    ax.set_xlabel('Time')
    ax.set_ylabel('Population')
    ax.set_title('Lotka-Volterra Model Simulation')
    ax.legend()
    st.pyplot(fig)
