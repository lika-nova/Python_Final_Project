# Import necessary libraries
import folium  # Library for creating interactive maps
import webbrowser  # Library for opening web browser
import requests  # Library for making HTTP requests
from PIL import Image  # Library for image processing
from io import BytesIO  # Library for handling byte streams

# Generate a map displaying Airbnb listings in Dublin
def result_map(data):
    # Create a folium map centered around Dublin
    dublin_map = folium.Map(location=[53.349805, -6.26031], zoom_start=14)
    # Group the data by latitude and longitude
    grouped_data = data.groupby(['latitude', 'longitude'])
    # Add markers for each group in the DataFrame
    for (lat, lon), group in grouped_data:
        # Create a string representation with information for all objects at the same location
        popup_content = ""
        for index, row in group.iterrows():
            popup_content += f"ID: {row['id']}, Name: {row['name']}<br>"
        # Add a marker with the string representation as the popup
        folium.Marker([lat, lon], popup=popup_content).add_to(dublin_map)
    
    # Save the map to an HTML file
    dublin_map.save("result_map.html")
    # Open the HTML file in the default web browser
    webbrowser.open("result_map.html")

# Display result (filtered Airbnb listing data) and provide options to interact with the result
def result(data):
    data_result = data[['id','name']]
    # Displaying the filtered rows as a Markdown table
    print(data_result.to_markdown(index=False),'\n')
    while True:
        print("1. Show Airbnb listing details by ID")
        print("2. Open Airbnb listing image by ID")
        print("3. Open Airbnb listing URL by ID")
        print("4. Return")
        print("5. Exit the program")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            result_id(data)
        elif choice == '2':
            open_image(data)
        elif choice == '3':
            open_url(data)
        elif choice == '4':
            break
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Display details of an Airbnb listing based on user-provided ID
def result_id(data):
    # The ID value to filter rows
    target_id = input("Please enter the Airbnb listing ID: ")

    try:
        # Validate if the ID is an integer
        target_id = int(target_id)  
    except ValueError:
        print("Invalid ID. Please enter a valid numeric ID.")
        return

    # Filtering rows based on the ID value
    if 'id' in data.columns and (data['id'] == target_id).any():
        id_data = data[data['id'] == target_id]

        if not id_data.empty:
            row = id_data.iloc[0]
            print(f"\nID: {row['id']}\n"
                  f"Airbnb name: {row['name']}\n"
                  f"Description: {row['description']}\n"
                  f"Amenities: {row['amenities']}\n")
        else:
            print("No listings found for the provided ID.")
    else:
        print(f"The ID {target_id} does not exist. Please provide valid ID.")

# Open the image associated with an Airbnb listing based on user-provided ID
def open_image(data):
    # The ID value to filter rows
    target_id = input("Please enter the Airbnb listing ID: ")

    try:
        # Validate if the ID is an integer
        target_id = int(target_id)  
    except ValueError:
        print("Invalid ID. Please enter a valid numeric ID.")
        return

    # Filtering rows based on the ID value
    if 'id' in data.columns and (data['id'] == target_id).any():
        id_data = data[data['id'] == target_id]
        
        if not id_data.empty:
            image_url = id_data['picture_url'].iloc[0]
            # Downloading the image from the URL
            response = requests.get(image_url)
            # Checking the success of the request
            if response.status_code == 200:
                # Creating an image object from the byte stream
                try:
                    image = Image.open(BytesIO(response.content))
                    # Opening the image
                    image.show()
                except Exception as e:
                    print(f"Failed to open the image. Error: {e}")
            else:
                print(f"Failed to download the image. Status code: {response.status_code}")
        else:
            print("No listings found for the provided ID.")
    else:
        print(f"The ID {target_id} does not exist. Please provide valid ID.")

# Open the URL associated with an Airbnb listing based on user-provided ID
def open_url(data):
    # The ID value to filter rows
    target_id = input("Please enter the Airbnb listing ID: ")

    try:
        # Validate if the ID is an integer
        target_id = int(target_id)  
    except ValueError:
        print("Invalid ID. Please enter a valid numeric ID.")
        return

    # Filtering rows based on the ID value
    if 'id' in data.columns and (data['id'] == target_id).any():
        id_data = data[data['id'] == target_id]
    
        if not id_data.empty:
            url = id_data['listing_url'].iloc[0]
            webbrowser.open(url)
        else:
            print("No listings found for the provided ID.")
    else:
        print(f"The ID {target_id} does not exist. Please provide valid ID.")
