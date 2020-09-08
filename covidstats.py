from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches




def update_data_table():

    """
    Updating the desirable data (DataFrame type).
    Takes the official website url as a parameter.
    """

    # Official Ministry Of Health's data dashboard website
    url = "https://datadashboard.health.gov.il/COVID-19/general"

    # Loading the driver
    # First try with local chromedriver, else install one.
    try:
        driver = webdriver.Chrome(executable_path="Sagi CV/Projects/chromedriver")
    except:
        driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get(url)
    driver.implicitly_wait(20)
    
    # Scraping the table as a DataFrame object
    contagion_areas = driver.find_element_by_name("contagionAreas")
    raw_table = contagion_areas.find_element_by_tag_name('table')

    covid_areas = pd.read_html(raw_table.get_attribute('outerHTML'))[0]

    # Closing driver
    driver.quit() 

    # Setting the Index as the City's name
    covid_areas.set_index('יישוב', inplace=True)

    # Loading Government's data files
    population = pd.read_csv('population_final.csv')
    population.set_index('Unnamed: 0', inplace=True)

    city_dict = pd.read_csv('city_dict.csv')
    city_dict.set_index('Unnamed: 0', inplace=True)


    # Appending the 'Population' column, keeping the errors in a list.
    unsuccessful = []
    for key in covid_areas.index:
        try:
            covid_areas.loc[key, 'Population'] = population.loc[key, 'סהכ']
        except:
            unsuccessful.append(key)

    # Changing the table from Hebrew to English
    covid_areas.index = [city_dict.loc[key].values[0] for key in covid_areas.index]

    covid_areas.columns = ['Total Cases', 'Active Cases', 'New Cases In The Past Week',
                    'Total Tests In The Past Week', 'Active Cases Per 10,000 Residents', 'Population']

    covid_areas.loc[covid_areas['Total Cases'] == 'קטן מ-15', 'Total Cases'] = 'smaller than 15'

    # Update the CSV file
    covid_areas.to_csv('covid_data.csv')
    


def pie_plot(labels, values):
    """
    Plotting pie graph by labels and values.
    """
    ax1 = plt.subplots()[1]
    ax1.pie(values, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.



def plot_city_data(city):
    """
    Ploting 3 graphs which presenting proportions:
        1. Total Cases / Population
        2. Active Cases / Total Cases
        3. New Cases / Tests  - (in the past week)
    """
        

    # Read Data
    covid_data = pd.read_csv('covid_data.csv')
    covid_data.set_index('Unnamed: 0', inplace=True)

    city_data = covid_data.loc[city.upper()]

    # Assigning variables
    population = int(city_data['Population'])
    total_cases = int(city_data['Total Cases'])
    active_cases = int(city_data['Active Cases'])
    cases_week = int(city_data['New Cases In The Past Week'])
    tests_week = int(city_data['Total Tests In The Past Week'])

    # Assigning figures' values and labels
    fig1_labels, fig1_values = ['Population', 'Total Cases'], [population, total_cases]
    fig2_labels, fig2_values = ['Total Cases', 'Active Cases'], [total_cases, active_cases]
    fig3_labels, fig3_values = ['Total Tests (per week)', 'New Cases (per week)'], [tests_week, cases_week]

    # Ploting with written function.
    pie_plot(fig1_labels, fig1_values)
    pie_plot(fig2_labels, fig2_values)
    pie_plot(fig3_labels, fig3_values)

    plt.show()