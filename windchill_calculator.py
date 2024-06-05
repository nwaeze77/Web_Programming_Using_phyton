import math

tempreture = float(input('What is the temperature? '))

given_temp_type = str(input('Fahrenheit or Celsius (F/C)?')).upper()

# Writing the various Functions
# Function for converting Celsius to Fahrenheit

def celsius_fahrenheit(tempreture):
    if given_temp_type == 'C':
        return tempreture * (9/5) + 32
    
    elif given_temp_type == 'F':
        return tempreture
    
new_temp  = celsius_fahrenheit(tempreture) 

# Function that calculates the Wind Chill given Tempreture and Wind speed

def wind_chill(tempreture, wind_speed):
    wind_chill = 35.74 + 0.6215 * new_temp - 35.75 * (wind_speed ** 0.16) + 0.4275 * new_temp * (wind_speed ** 0.16)
    return wind_chill

# Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5, and calculate wind chill

for wind_speed in range(5, 61, 5):
    #print(wind_speed)
    wind_chill_new = wind_chill(tempreture, wind_speed)
    new_temp = celsius_fahrenheit(tempreture)
    print(f'At temperature {new_temp:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill_new:.2f}F')