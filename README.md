# COVID-19 Project
### Short Description 
GUI which has two key features:
  1. 'GIVE ME GRAPHS' - Takes a city's name in Israel and returns the COVID-19 data in 3 pie charts as described later.
  2. 'Update Data' - Updating the database by scraping the official website of Ministry Of Health. 

### Motivation 
The Coronavirus is **by far** the most talked-about subject in the globe, and especially in Israel.
furthermore, the information is often dispropotionately represented, so my passion for data and solving problems produce this idea.

### Build Status
There some extra features to come:
  - [x] The data will be represented **on the GUI itselfs**.
  - [ ] The input absorption will be **more forgiving**.
  - [ ] The user will be able to plot graphs **several times in one run**.

### Screenshots

- #### The GUI (Opening Window)
<img src="/Screenshots/Main.png" width="60%" height="60%">


- #### The Pie Charts (for Tel Aviv - Yafo)
<img src="/Screenshots/Graphs.png" width="60%" height="60%">


- #### The GUI after successful update
<img src="/Screenshots/Update Succeeded.png" width="60%" height="60%">



### Tech & Framework 
 - **Editor:** VSCode 
 - **Libraries:** Selenium, Tkinter, Pandas and Matplotlib.
 
### Data Sources References:
- [**COVID-19 Data (Ministry of Health)**](https://datadashboard.health.gov.il/COVID-19/general)

  Scraping from this website the Covid-19 data.
- [**City Population (Data Gov)**](https://data.gov.il/dataset/residents_in_israel_by_communities_and_age_groups/resource/64edd0ee-3d5d-43ce-8562-c336c24dbc1f)ֿ

  Used for adding the total population amount to the Covid-19 table (With simple pandas' operations).
- [**List of cities Israel for translation) (Data Gov)**](https://data.gov.il/dataset/citiesandsettelments/resource/5c78e9fa-c2e2-4771-93ff-7f400a12f7ba)

  User for retrieving Hebrew-English dictionary for translation.




