import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from team_wise_scrap import get_player_info, create_csv_file


def start():
    '''Execution starts from here '''

    browser = webdriver.Firefox()
    file_name = None
    li_list_of_players = None
    # here we directly use link to go 2022 and junior college player list
    url = 'https://247sports.com/Season/2022-Football/RecruitRankings/?InstitutionGroup=JuniorCollege'
    try:
        # call function to create csv file with different name
        file_name = create_csv_file()
    except Exception as e:
        print(e)

    browser.get(url)
    browser.implicitly_wait(3)
    try:
        # find ul and li list for players data scrap
        ul_list_of_players = browser.find_element(By.CLASS_NAME, 'rankings-page__list')
        li_list_of_players = ul_list_of_players.find_elements(By.CLASS_NAME, 'rankings-page__list-item')
    except Exception as e:
        print(e)
    try:
        for player_list in li_list_of_players:
            # This for loop used to iterate player lists
            players_url = player_list.find_element(By.CLASS_NAME, 'rankings-page__name-link')
            players_url_link = players_url.get_attribute('href')
            try:
                # Here we call function to scrap player info
                player_info = get_player_info(players_url_link)
                with open(file_name, 'a') as file:
                    # Add our players info in csv file which already created
                    writer = csv.writer(file)
                    writer.writerow(player_info)
            except Exception as e:
                print(e)
            # apply back for go again players list
            browser.back()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    start()
