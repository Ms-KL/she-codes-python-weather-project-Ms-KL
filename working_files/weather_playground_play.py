import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# cd C:\GIT\python-assignment\she-codes-python-weather-project-Ms-KL
# python weather_playground_play.py

weather_data = ["49", "57", "56", "55", "53", "49"]
# weather_data = []

def min_max_list (weather_data):
    """creates a list for min/max calc

    Args:
        weather_data: A list of numbers.
    Returns:
        List of numbers as a float
    """
    if weather_data != []:
        weather_data_list = []
        for i in weather_data:
            weather_data_list.append(float(i))
        return weather_data_list
    else:
        return ()

def min_or_max (weather_data):
    if weather_data != []:
        calc_list = min_max_list(weather_data)
        min_temp = min(calc_list)
        max_temp = max(calc_list)
        for i in range(len(calc_list)):
            if calc_list[i] == min_temp:
                min_index = i
            if calc_list[i] == max_temp:
                max_index = i
        return [min_temp, min_index, max_temp, max_index]
    else:
        return ()

#--6 ---- DONE
def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    min_temp = min_or_max(weather_data)[0]
    min_index = min_or_max(weather_data)[1]
    return min_temp, min_index

    # if weather_data != []:
    #     calc_list = min_max_list(weather_data)
    #     min_temp = min(calc_list)
    #     for i in range(len(calc_list)):
    #         if calc_list[i] == min_temp:
    #             min_index = i
    #     return min_temp, min_index
    # else:
    #     return ()

def find_max(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    max_temp = min_or_max(weather_data)[2]
    max_index = min_or_max(weather_data)[3]
    return max_temp, max_index

print(find_max(weather_data), find_min(weather_data))
print(weather_data)
print(min_max_list(weather_data))
print(min_or_max (weather_data))


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

#--2
def convert_date(iso_string):
    """Converts an ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date_time = datetime.fromisoformat(iso_string)
    convert_date = date_time.strftime("%A %d %B %Y")
    return convert_date
    pass

#--3 ------ DONE
def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_c = (float(temp_in_farenheit) - 32) * .5556
    return round(temp_in_c,1) 
    pass

# external function:
def conversion_list(weather_data):
    if weather_data != []:
        weather_data_list = []
        for i in weather_data:
            weather_data_list.append(float(i))
    return weather_data_list

print(conversion_list(weather_data))


#--4 ------ DONE
def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    sum = 0
    for i in weather_data:
        sum = float(sum)+float(i)
    mean = sum / len(weather_data)
    return mean
    pass

#--5 -------- DONE
def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    csv_list = []
    with open(csv_file, encoding="utf-8") as csv_open:
        reader = csv.reader (csv_open)
        next(reader)
        for line in reader:
            if not (line):
                continue
            csv_list.append([line[0],int(line[1]),int(line[2])])
    return csv_list
    # pass


# #--6 ---- DONE
# def find_min(weather_data):
#     """Calculates the minimum value in a list of numbers.

#     Args:
#         weather_data: A list of numbers.
#     Returns:
#         The minium value and it's position in the list.
#     """
#     converted_weather_data = conversion_list(weather_data)
#     min_temp = min(converted_weather_data)
#     for i in range(len(converted_weather_data)):
#         if converted_weather_data[i] == min_temp:
#             min_index = i
#     return min_temp, min_index
#     # else:
#     #     return ()

#     pass


# #--7
# def find_max(weather_data):
#     """Calculates the minimum value in a list of numbers.

#     Args:
#         weather_data: A list of numbers.
#     Returns:
#         The minium value and it's position in the list.
#     """
#     converted_weather_data = conversion_list(weather_data)
#     max_temp = max(converted_weather_data)
#     for i in range(len(converted_weather_data)):
#         if converted_weather_data[i] == max_temp:
#             max_index = i
#     return max_temp, max_index
#     # else:
#     #     return ()
#     # pass

# #--8
# def generate_summary(weather_data):
#     """Outputs a summary for the given weather data.

#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """
#     # ----- GOALS ------
#     # TEMPS: min_temp + max_temp
#     # DATES: min_date + max_date
#     # MEANS: mean_low + mean_high 
#     # COUNT

#     # STEP 1 GET DATA:
#     # convert weather data into 3x lists to use for functions
    
#     dates_list = []
#     min_list = []
#     max_list = []
#     for row in weather_data:
#         dates_list.append(row[0])
#         min_list.append(convert_f_to_c(row[1]))
#         max_list.append(convert_f_to_c(row[2]))

#     # STEP 2 GET TEMPS:
#     # find min_temp and max_temp in lists using functions

#     min_temp_n_index = find_min(min_list)
#     min_temp = min_temp_n_index[0]
#     max_temp_n_index = find_max(max_list)
#     max_temp = max_temp_n_index[0]

#     # STEP 3 GET DATES:
#     # find min_date and max_date using temp_n_index[1] (index position of min or max) @ return item @ index 0
#     # need to convert these dates using function
    
#     min_date = dates_list[min_temp_n_index[1]]
#     min_date = convert_date(min_date)
#     max_date = dates_list[max_temp_n_index[1]]
#     max_date = convert_date(max_date)

#     # STEP 4 GET MEANS:
#     # find mean_low and mean_high using functions

#     mean_low = round((calculate_mean(min_list)),1)
#     mean_high = round((calculate_mean(max_list)),1)

    
#     # STEP 5 GET COUNT:
#     # find count using length of weather data
#     count = len(weather_data)

#     return f"{count} Day Overview\n  The lowest temperature will be {min_temp}{DEGREE_SYBMOL}, and will occur on {min_date}.\n  The highest temperature will be {max_temp}{DEGREE_SYBMOL}, and will occur on {max_date}.\n  The average low this week is {mean_low}{DEGREE_SYBMOL}.\n  The average high this week is {mean_high}{DEGREE_SYBMOL}.\n"

# #--9
# def generate_daily_summary(weather_data):
#     """Outputs a daily summary for the given weather data.

#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """
    

# # --- working it out

# # GOALS:
# # day_date
# # day_min_temp
# # day_max_temp

#     # STEP 1 GET DATA:
#     # convert weather data a list to allocate to required variables
    
#     weather_list = []
#     for row in weather_data:
#         weather_list.append([
#             convert_date(row[0]),
#             convert_f_to_c(row[1]),
#             convert_f_to_c(row[2])
#             ])
    
#     # STEP 2 ALLOCATE VARIABLES:
#     # index the weather_list and allocate to date_time, min and max

#     daily_summary_string = ""
#     last_string = ""
#     for row in weather_list:
#         day_date = row[0]
#         day_min_temp = row[1]
#         day_max_temp = row[2]
#         daily_summary_string = last_string + f"---- {day_date} ----\n  Minimum Temperature: {day_min_temp}{DEGREE_SYBMOL}\n  Maximum Temperature: {day_max_temp}{DEGREE_SYBMOL}\n\n"
#         last_string = daily_summary_string

#     return daily_summary_string
