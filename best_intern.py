import pandas as pd

# Load the cleaned dataset
cleaned_dataset_path = r"C:\Users\PC\Desktop\Best_Intern\Cleaned_Dataset.xlsx"
df = pd.read_excel(cleaned_dataset_path)

# Define the scoring mechanism
# You can customize this based on your criteria and requirements
def calculate_score(row):
    score = 0
    # Add weights to different criteria based on importance
    score += row['Python (out of 3)'] * 0.3
    score += row['Machine Learning (out of 3)'] * 0.4
    score += row['Natural Language Processing (NLP) (out of 3)'] * 0.2
    score += row['Deep Learning (out of 3)'] * 0.1
    return score

# Calculate scores for each candidate
df['Score'] = df.apply(calculate_score, axis=1)

# Sort the candidates based on their scores in descending order
df_sorted = df.sort_values('Score', ascending=False)

# Select the top candidate
best_intern = df_sorted.iloc[0]

# Print the details of the best intern
print("Best Intern:")
print(best_intern)
