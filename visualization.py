# Visualization libraries
import seaborn as sns
import matplotlib.pyplot as plt
# Define a custom color palette
custom_palette = ['#86A7FC','#FFDD95']

# Create a bar plot showing the count of each category in the specified column
def create_plot(data, column):
    # Seaborn bar plot with the specified order
    plt.figure(figsize=(10, 3))
    ax=sns.countplot(x=column, data=data, color='#FFDD95')
    # Annotate each bar with its height
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha='center', va='bottom')
    # Set plot labels and title    
    plt.ylabel("Properties found, count")
    plt.xlabel(column)
    plt.title("Number of Listings by " + column, fontsize=10)
    # Display the plot
    plt.show()

# Create a pie chart showing the distribution of categories in the specified column
def create_pie(data, column):
    counts = data[column].value_counts()
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(counts, labels=counts.index, colors=custom_palette, autopct='%1.1f%%', startangle=90)
    # Set plot title 
    ax.set_title(f'{column} options')
    # Display the plot
    plt.show()

# Create a bar plot showing the count of properties based on rating ranges
def create_barplot(data, column):
    # Data filtering
    data_3_5 = data[data[column] >= 3.5]
    data_4 = data[data[column] >= 4]
    data_4_5 = data[data[column] >= 4.5]
    data_4_7 = data[data[column] >= 4.7]
    
    # Counting occurrences in each range
    counts = [len(data_3_5), len(data_4), len(data_4_5), len(data_4_7)]
    # Rating ranges
    categories = ['Pleasant: 3.5+', 'Good: 4+', 'Very good: 4.5+', 'Superb: 4.7+']
    
    # Using Seaborn for visualization
    plt.figure(figsize=(10, 3))
    ax=sns.barplot(x=categories, y=counts, color='#FFDD95')
    # Adding value annotations to each bar
    for i, count in enumerate(counts):
        ax.text(i, count + 0.1, str(count), ha='center', va='bottom', fontsize=10)
    # Set plot labels and title 
    plt.xlabel('Review Score Rating')
    plt.ylabel('Properties found, count')
    plt.title('Number of Listings by Rating', fontsize=10)
    # Display the plot
    plt.show()