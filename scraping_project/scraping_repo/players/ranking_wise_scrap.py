import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from team_wise_scrap import get_player_info, create_csv_file


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


if __name__ == '__main__':
    main()
