from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk



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
        driver = webdriver.Chrome(executable_path="chromedriver")
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
    

def plot_city_data(city, canvas_1, canvas_2, canvas_3, root):

    """
    Ploting 3 graphs which presenting the following proportions:
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
    fig3_labels, fig3_values = ['Total Tests (past week)', 'New Cases (past week)'], [tests_week, cases_week]

    # Ploting the pie charts on the GUI

    figure1 = plt.Figure(figsize=(10,5), dpi=100)
    ax1 = figure1.add_subplot(111)
    chart_type1 = FigureCanvasTkAgg(figure1, canvas_1)
    chart_type1.get_tk_widget().pack()
    ax1.pie(fig1_values, labels=fig1_labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    figure1.set_facecolor('#DC7963')


    figure2 = plt.Figure(figsize=(10,5), dpi=100)
    ax2 = figure2.add_subplot(111)
    chart_type2 = FigureCanvasTkAgg(figure2, canvas_2)
    chart_type2.get_tk_widget().pack()
    ax2.pie(fig2_values, labels=fig2_labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax2.axis('equal')
    figure2.set_facecolor('#DC7963')


    figure3 = plt.Figure(figsize=(10,5), dpi=100)
    ax3 = figure3.add_subplot(111)
    chart_type3 = FigureCanvasTkAgg(figure3, canvas_3)
    chart_type3.get_tk_widget().pack()
    ax3.pie(fig3_values, labels=fig3_labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax3.axis('equal')
    figure3.set_facecolor('#DC7963')    
