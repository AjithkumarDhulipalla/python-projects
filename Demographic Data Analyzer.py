import pandas as pd

def calculate_demographic_data(print_output=True):
    # Load the dataset
    df = pd.read_csv('your_dataset.csv')  # Replace 'your_dataset.csv' with the actual file path

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'] == 'Bachelors').sum() / len(df) * 100

    # 4. What percentage of people with advanced education make more than 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_higher_education = (higher_education['salary'] == '>50K').sum() / len(higher_education) * 100

    # 5. What percentage of people without advanced education make more than 50K?
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_lower_education = (lower_education['salary'] == '>50K').sum() / len(lower_education) * 100

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = len(df[df['hours-per-week'] == min_work_hours])
    rich_percentage = (df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0] / num_min_workers) * 100

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
    highest_earning_country_percentage = (df[df['native-country'] == highest_earning_country]['salary'] == '>50K').sum() / len(df[df['native-country'] == highest_earning_country]) * 100

    # 9. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    if print_output:
        print("1. People of each race: \n", race_count)
        print("\n2. Average age of men: ", round(average_age_men, 1))
        print("\n3. Percentage with Bachelor's degree: ", round(percentage_bachelors, 1))
        print("\n4. Percentage with advanced education earning >50K: ", round(percentage_higher_education, 1))
        print("\n5. Percentage without advanced education earning >50K: ", round(percentage_lower_education, 1))
        print("\n6. Minimum number of hours a person works per week: ", min_work_hours)
        print("\n7. Percentage of people working the minimum hours earning >50K: ", round(rich_percentage, 1))
        print("\n8. Country with the highest percentage earning >50K: ", highest_earning_country)
        print("   Percentage: ", round(highest_earning_country_percentage, 1))
        print("\n9. Most popular occupation for those earning >50K in India: ", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'percentage_higher_education': round(percentage_higher_education, 1),
        'percentage_lower_education': round(percentage_lower_education, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }

# Uncomment the line below to test your function
# calculate_demographic_data()
