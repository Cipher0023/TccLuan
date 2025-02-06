from app import main
from plotter import plot_results
import os
import pandas as pd

def generate_sh_values(min_value, max_value, num_values):
    """Generate SH values within the specified range."""
    sh_values=[(min_value + i * (max_value - min_value) / (num_values - 1)) for i in range(num_values)]
    print(sh_values,"\n")
    return sh_values


def run_generated_sh_values(sh_values):

    i = 0
    for sh in sh_values:
        main(float(sh)) #the program should iterate trough the values from the sh_values 
        i += 1
        print(f"Run case {i} with sh={sh}")

def list_created_files():
    output_folder = "outputs"
    created_files = [f for f in os.listdir(output_folder) if os.path.isfile(os.path.join(output_folder, f))]
    
    if created_files:
        print("Created files in the 'outputs' folder:")
        for file_name in created_files:
            print(f"- {file_name}")
    else:
        print("No files found in the 'outputs' folder.")
def choose_file_to_plot():
    while True:
        # List the created files
        created_files = list_created_files()

        filechoice = input("Enter the file you want to plot (or 'exit' to stop): ")

        if filechoice.lower() == 'exit':
            break

        if filechoice in created_files:
            df = pd.read_csv(os.path.join("outputs", filechoice))
            plot_results(df)
        else:
            print("Invalid file. Please choose a valid file.")

# Add the return statement to list_created_files to return created_files
def list_created_files():
    output_folder = "outputs"
    created_files = [f for f in os.listdir(output_folder) if os.path.isfile(os.path.join(output_folder, f))]
    
    if created_files:
        print("Created files in the 'outputs' folder:")
        for file_name in created_files:
            print(f"- {file_name}")
    else:
        print("No files found in the 'outputs' folder.")

    return created_files  # Return the created_files list

# Rest of your code...


if __name__ == "__main__":
    # Specify the range and number of SH values to generate
    min_sh_value = float(input("Write the minimum sh value: "))
    max_sh_value = float(input("Write the maximum sh value: "))
    num_sh_values = int(input("Write the number of sh values to be calculated: "))

    # Run cases with dynamically generated SH values
    run_generated_sh_values(generate_sh_values(min_sh_value, max_sh_value, num_sh_values))

    choose_file_to_plot()


