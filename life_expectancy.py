# Analyzing Life Expectancy Using data from OurWolrdInData.org

# I added the interesting anomalies in the data

lowest_value = 100 

highest_value = 50

country_min = ''

country_max = ''

year_min = ''

year_max = ''

year_expectancies = []

expectancies = []

year_of_choice = str(input('Enter the year of interest: '))

with open('C:/Users/Hp/Downloads/life-expectancy.csv') as data:
    header = next(data)
    for line in data:
        line = line.strip()
        cleaned_line = line.split(',')
        expectancy = float(cleaned_line[3])
        year = cleaned_line[2]
        

        if expectancy < lowest_value:
            lowest_value = expectancy
            country_min = cleaned_line[0]
            year_min = cleaned_line[2]
    

        if expectancy > highest_value:
            highest_value = expectancy
            country_max = cleaned_line[0]
            year_max = cleaned_line[2]

        
        expectancies.append(expectancy)
    
        if year == year_of_choice:
            year_expectancies.append(expectancy)

print(f'The overall max life expectancy is: {highest_value} from {country_max} in {year_max}')
print(f'The overall min life expectancy is: {lowest_value} from {country_min} in {year_min}') 


# Second part of the program
# To determine the average life expectancy

print(f'For the year {year_of_choice}:')

year_expectancies = []
highest_expectancy = float('-inf')
lowest_expectancy = float('inf')
country_highest = ''
country_lowest = ''


with open('C:/Users/Hp/Downloads/life-expectancy.csv') as data:
    header = next(data)
    for line in data:
        line = line.strip()
        cleaned_line = line.split(',')
        country = cleaned_line[0]
        year = cleaned_line[2]
        expectancy = float(cleaned_line[3])

        # Collect expectancies for the specified year
        if year == year_of_choice:
            year_expectancies.append((country, expectancy))

            # Find the highest and lowest expectancies for the year
            if expectancy > highest_expectancy:
                highest_expectancy = expectancy
                country_highest = country

            if expectancy < lowest_expectancy:
                lowest_expectancy = expectancy
                country_lowest = country

# Print the average life expectancy for the year

if year_expectancies:
    average_life_expectancy = sum(expectancy for _, expectancy in year_expectancies) / len(year_expectancies)
    print(f'The average life expectancy across all countries was {average_life_expectancy:.2f}')

else:
    print(f'No data available for the year {year_of_choice}')

# Print the highest and lowest life expectancy for the specified year
print(f'The max life expectancy was in {country_highest} with {highest_expectancy:.2f}')
print(f'The min life expectancy was in {country_lowest} with {lowest_expectancy:.2f}')


# Additional analysis for interesting anomalies or patterns
print("\nLook for interesting anomalies or patterns in the data:")

# Check for significant differences between neighboring years (if needed, customize this part)
anomalies = []
with open('C:/Users/Hp/Downloads/life-expectancy.csv') as data:
    header = next(data)
    previous_line = None
    for line in data:
        line = line.strip()
        cleaned_line = line.split(',')
        country = cleaned_line[0]
        year = int(cleaned_line[2])
        expectancy = float(cleaned_line[3])

        if previous_line:
            prev_country, prev_year, prev_expectancy = previous_line
            if country == prev_country and abs(year - prev_year) == 1:
                change = abs(expectancy - prev_expectancy)
                if change > 5:  # Customize the threshold for anomaly detection
                    anomalies.append((country, prev_year, year, prev_expectancy, expectancy, change))

        previous_line = (country, year, expectancy)

# Print anomalies
for anomaly in anomalies:
    print(f'Anomaly detected: {anomaly[0]} had a life expectancy change from {anomaly[3]:.2f} in {anomaly[1]} to {anomaly[4]:.2f} in {anomaly[2]} (Change: {anomaly[5]:.2f})')
