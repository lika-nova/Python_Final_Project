# Import necessary modules
import visualization as vz
import result_part as rp
import welcome_part as wp

# Call the welcome menu function to start the program and get filtered data
filtered_df = wp.welcome_menu()
filtered_result_df = filtered_df
# Initialize variables for selected filters
selected_neighbourhood = None
selected_room_type = None
selected_accommodates = None
selected_price = None
selected_rating = None

# Filter data based on user-selected Neighbourhood
def neighbourhood():
    global filtered_result_df, selected_neighbourhood
    # Display a plot of Neighbourhood distribution
    vz.create_plot(filtered_result_df, 'Neighbourhood')
    # Define valid Neighbourhood options
    valid_neighbourhoods = ['Dublin City', 'Fingal', 'Dn Laoghaire-Rathdown', 'South Dublin']
    while True:
        selected_neighbourhood = input("Select the Neighbourhood from Dublin City, Fingal, Dn Laoghaire-Rathdown, or South Dublin: ").title()
        if selected_neighbourhood in valid_neighbourhoods:
            filtered_result_df = filtered_result_df[filtered_result_df['Neighbourhood'] == selected_neighbourhood]
            return filtered_result_df, selected_neighbourhood 
        else:
            print("Invalid input. Please choose a valid Neighbourhood.")

# Filter data based on user-selected Room type
def room():
    global filtered_result_df, selected_room_type
    # Display a plot of Room type distribution
    vz.create_plot(filtered_result_df, 'Room type')
    # Define valid Room type options
    valid_room_type = ['Private room', 'Entire home/apt', 'Shared room', 'Hotel room']
    while True:
        selected_room_type = input("Select the Room type from Private room, Entire home/apt, Shared room, Hotel room: ").capitalize()
        if selected_room_type in valid_room_type:
            filtered_result_df = filtered_result_df[filtered_result_df['Room type'] == selected_room_type]
            return filtered_result_df, selected_room_type
        else:
            print("Invalid input. Please choose a valid Room type.")

# Filter data based on user-selected Capacity
def capacity():
    global filtered_result_df, selected_accommodates
    # Display a plot of Capacity distribution
    vz.create_plot(filtered_result_df, 'Capacity (number of people)')
    # Define valid Capacity options
    valid_accommodates = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
    while True:
        selected_accommodates = input("Select the Capacity from 1 to 16: ")
        if selected_accommodates in valid_accommodates:
            filtered_result_df = filtered_result_df[filtered_result_df['Capacity (number of people)'] == int(selected_accommodates)]
            return filtered_result_df, selected_accommodates
        else:
            print("Invalid input. Please choose a valid Capacuty.")

# Filter data based on user-selected Price Range
def price():
    global filtered_result_df, selected_price
    # Display a plot of Price Range distribution
    vz.create_plot(filtered_result_df, 'Price Range, $')
    # Define valid Price Range options
    valid_price_range = ['10-40','41-60','61-80','81-100','101-130','131-160','161-200','201-300','300+']
    while True:
        selected_price = input("Select Your budget (per night) 10-40, 41-60, 61-80, 81-100, 101-130, 131-160, 161-200, 201-300, 300+: ")
        if selected_price in valid_price_range:
            filtered_result_df = filtered_result_df[filtered_result_df['Price Range, $'] == selected_price]
            return filtered_result_df, selected_price
        else:
            print("Invalid input. Please choose a valid Price Range.")

# Filter data based on user-selected Review Scores Rating
def rating():
    global filtered_result_df, selected_rating
    # Display a bar plot of Review Scores Rating distribution
    vz.create_barplot(filtered_result_df, 'review_scores_rating')
    # Define valid Review Scores Rating options
    valid_rating_range = ['3.5','4','4.5','4.7']
    while True:
        selected_rating = input("Select the review scores rating 3.5, 4, 4.5, 4.7: ")
        if selected_rating in valid_rating_range:
            filtered_result_df = filtered_result_df[filtered_result_df['review_scores_rating'] >= float(selected_rating)]
            return filtered_result_df, selected_rating
        else:
            print("Invalid input. Please choose a valid Review Scores Rating.")

# Display filtered results based on user-selected filters and provide options for further interaction
def result():
    global selected_neighbourhood, selected_room_type, selected_accommodates, selected_price, selected_rating, filtered_df, filtered_result_df
    # Check if no filters are selected
    if selected_neighbourhood is None and selected_room_type is None and selected_accommodates is None and selected_price is None and selected_rating is None:
        print("No filters selected.")
    # Check if no listings match the criteria
    if len(filtered_result_df) == 0:
        print("No listings match your criteria.")
    # Display the number of listings based on selected filters
    print(f"Number of listings based on your choice (Neighbourhood - {selected_neighbourhood}, Room type - {selected_room_type}, Capacity - {selected_accommodates}, Price Range, $ - {selected_price}, Review Scores Rating - {selected_rating}): {len(filtered_result_df)}")
    while True:
        print("1. Show result on the map")
        print("2. Show information about the result")
        print("3. Return and add filters")
        print("4. Return and change your filters")
        print("5. Return to the beginning of the program. Reset all your selections.")
        print("6. Exit the program")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            rp.result_map(filtered_result_df)
        elif choice == '2':
            rp.result(filtered_result_df)
        elif choice == '3':
            break
        elif choice == '4':
            selected_neighbourhood = None
            selected_room_type = None
            selected_accommodates = None
            selected_price = None
            selected_rating = None
            filtered_result_df = filtered_df
            break
        elif choice == '5':
            selected_neighbourhood = None
            selected_room_type = None
            selected_accommodates = None
            selected_price = None
            selected_rating = None
            filtered_df = wp.welcome_menu()
            filtered_result_df = filtered_df
            break
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")