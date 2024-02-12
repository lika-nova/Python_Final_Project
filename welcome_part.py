# Import necessary modules
import visualization as vz
import editing_data as ed

# Function to get user input and display information based on the selected parameter
# Get user input to enable or disable a specific option and filter the data accordingly
def get_user_input(data, column):
    selected_valid = ['yes', 'no']
    while True:
        selected = input(f"Would you like to enable {column} option? Select Yes or No: ").lower()
        if selected in selected_valid:
            break
        else:
            print("Invalid input. Please choose Yes or No.")

    if selected == 'yes':
        data = data[data[column] == 'yes']
    # Return the modified DataFrame
    return data  

# Display a welcome message and gather user preferences for accommodation options
def welcome_menu():
    # Main script
    print("Hello! Before we proceed with selecting accommodation based on specific criteria,\n"
      "please indicate any additional preferences or options you'd like to consider.")
    
    # Initialize filtered_df outside the loop
    filtered_df = ed.df.copy()

    # Iterate through the list of columns and get user input for each
    columns_to_check = ['Availability','Instant Booking', 'Superhost']
    for column in columns_to_check:
        vz.create_pie(filtered_df, column)
        filtered_df = get_user_input(filtered_df, column)
    return filtered_df