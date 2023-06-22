import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from team_wise_scrap import get_player_info


def main():
    '''Execution starts from here '''

    try:
        '''
        This try block is used for go all players and scrap player data
        '''
        browser = webdriver.Firefox()
        'here we directly use link to go 2022 and junior college player list'
        url = 'https://247sports.com/Season/2022-Football/RecruitRankings/?InstitutionGroup=JuniorCollege'
        'call function to create csv file with different name'
        file_name = create_csv_file()
        browser.get(url)
        browser.implicitly_wait(3)
        'find ul and li list for players data scrap'
        ul_list_of_players = browser.find_element(By.CLASS_NAME, 'rankings-page__list')
        li_list_of_players = ul_list_of_players.find_elements(By.CLASS_NAME, 'rankings-page__list-item')
        for player_list in li_list_of_players:
            '''This for loop used to iterate player lists'''
            players_url = player_list.find_element(By.CLASS_NAME, 'rankings-page__name-link')
            players_url_link = players_url.get_attribute('href')
            'Here we call function to scrap player info'
            get_player_info(players_url_link, file_name)
            'apply back for go again players list'
            browser.back()
    except:
        raise Exception("browser not found")
        
def create_csv_file():
    '''This function is used for create csv file by considering datetime'''
    try:
        'Here we use datetime module which used to found unique number for our csv file name'
        current_time_span = datetime.datetime.now().strftime("%f")
        'we store in file name variable and use f string to use datetime microseconds'
        file_name = f"player_ranking_wise{current_time_span}.csv"
        "This header list used to display in csv heading for column head name"
        header = ['Player Image Url', 'Player Name', 'Player Position', 'Player Height', 'Player Weight',
                  'Player High School Name', 'Player City Name', 'Player state', 'Player Class', 'Offers Dictionary',
                  'Commitments Dictionary']
        with open(file_name, 'w') as file:
            'here we use open function to open and write our file'
            writer = csv.writer(file)
            'here we write our csv file'
            writer.writerow(header)
            'here we add header first row'
        return file_name
    except:
        print("Csv file not created")



if __name__ == '__main__':
    main()
