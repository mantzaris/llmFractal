import subprocess
import logging
import pandas as pd
import matplotlib.pyplot as plt
import select
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Start the Julia process
julia_process = subprocess.Popen(
    ["julia"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1
)

def run_julia_code(code):
    # Send the code to the Julia process
    julia_process.stdin.write(code + "\n")
    julia_process.stdin.flush()

    output = []
    while True:
        # Use select to check if there's data to read, with a timeout
        ready, _, _ = select.select([julia_process.stdout], [], [], 2)
        if ready:
            line = julia_process.stdout.readline().strip()
            if line:
                output.append(line)
                logging.info(f"Julia Output: {line}")
            else:
                break
        else:
            break  # Exit if there's nothing to read (timeout reached)

    return "\n".join(output)

def visualize_data(file_name):
    data = pd.read_csv(file_name)
    plt.scatter(data['x'], data['y'])
    plt.title(f"Scatter Plot from {file_name}")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.savefig(f"{file_name.replace('.csv', '.png')}")
    logging.info(f"Plot saved as {file_name.replace('.csv', '.png')}")
    plt.clf()  # Clear the current figure

def main():
    logging.info("Python: Orchestrator started")

    # Manually call Julia to generate and save data
    run_julia_code('include("simple_fractal.jl")')

    run_julia_code('generate_simple_data("data1.csv")')
    visualize_data("data1.csv")

    # Call Julia again to generate and save different data
    run_julia_code('generate_simple_data("data2.csv")')
    visualize_data("data2.csv")

    run_julia_code('generate_simple_data("data3.csv")')
    visualize_data("data3.csv")

    run_julia_code('generate_simple_data("data4.csv")')
    visualize_data("data4.csv")

    # Close the Julia process
    julia_process.terminate()
    logging.info("Python: Orchestrator finished")

if __name__ == "__main__":
    main()
