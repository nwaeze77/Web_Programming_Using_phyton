# # Initialization
# country_of_choice = input("Enter the country of interest: ")
# 

# Prompt the user to enter a country of choice

country_life_expectancies = []
country_of_choice = input('What is your country of choice: ')

# Re-read the data file to collect life expectancies for the specific country
with open('C:/Users/Hp/Downloads/life-expectancy.csv') as data:
    header = next(data)  # Skip the header row
    for line in data:
        country = line[0]
        year = line[2]
        try:
            expectancy = float(line[3])
        except ValueError:
            continue  # Skip lines where conversion to float fails

        if country == country_of_choice:
            country_life_expectancies.append(expectancy)

# Calculate and output the min, max, and average life expectancy for the specific country
if country_life_expectancies:
    average_country_expectancy = sum(country_life_expectancies) / len(country_life_expectancies)
    max_country_expectancy = max(country_life_expectancies)
    min_country_expectancy = min(country_life_expectancies)

    print(f'For {country_of_choice}:')
    print(f'The average life expectancy is {average_country_expectancy:.2f}')
    print(f'The max life expectancy is {max_country_expectancy:.2f}')
    print(f'The min life expectancy is {min_country_expectancy:.2f}')
else:
    print(f'No data available for the country {country_of_choice}')