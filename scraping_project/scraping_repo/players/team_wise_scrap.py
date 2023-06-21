import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import csv


def get_player_info(player_url, file_name):
    '''
    This function is used for scrap all player information from team
    '''
    browser = webdriver.Firefox()
    text_img_url, player_name, player_pos, player_height, player_weight, player_high_school, player_city, \
        player_state, player_class = None, None, None, None, None, None, None, None, None

    try:

        browser.get(player_url)
        time.sleep(3)
        player_name = browser.find_element(By.XPATH, "//h1[@class='name']").text
        player_img = browser.find_element(By.TAG_NAME, 'img')
        player_img_url = player_img.get_attribute('src')
        text_img_url = f"{player_img_url}"
        ul_first_list_info = browser.find_element(By.CLASS_NAME, 'metrics-list')
        span_tags_info = ul_first_list_info.find_elements(By.TAG_NAME, 'span')
        try:
            player_pos = span_tags_info[1].text
        except:
            player_pos = None
        try:
            player_height = span_tags_info[3].text
        except:
            player_height =None
        try:
            player_weight = span_tags_info[5].text
        except:
            player_weight=None

        ul_second_info = browser.find_element(By.CLASS_NAME, 'details ')
        span_info = ul_second_info.find_elements(By.TAG_NAME, 'span')
        try:
            player_high_school = span_info[1].text
            player_city = span_info[3].text
        except:
            player_city = span_info[1].text

        player_city_state = player_city.split(',')
        try:
            player_city = player_city_state[0]
            player_state = player_city_state[1]
        except:
            player_city =None
            player_state =None
        try:
            player_classes = span_info[5].text
            player_class = player_classes[:4]
        except:
            player_class = None
    except:
        raise Exception("Browser not found")

    try:
        commitments_list = {}
        try:
            view_recruting_profile = browser.find_element(By.CLASS_NAME, 'view-profile-link')

            recruited_list = []

            '''This if condition used for check in web page we have view_recruiting_profile link or not '''

            if view_recruting_profile:
                view_recruting_profile.click()
                time.sleep(2)
            ul_lists_of_teams = browser.find_element(By.CLASS_NAME, 'college-comp__body-list')
            li_lists_of_teams = ul_lists_of_teams.find_elements(By.CLASS_NAME, 'college-comp__body-list-item')
            for teams_list in li_lists_of_teams:
                '''This for loop is used for iterate all lists of commitments'''
                if teams_list.find_element(By.TAG_NAME, 'span').text == 'Enrolled' or 'Committed':
                    commitment_team_name = teams_list.find_element(By.CLASS_NAME, 'college-comp__team-name-link').text
                    commitment_team_img_url = teams_list.find_element(By.CLASS_NAME, 'college-comp__college-team-image')
                    commitment_team_img_url_src = commitment_team_img_url.get_attribute('src')
                    commitment_recruited_div = teams_list.find_element(By.CLASS_NAME,
                                                                       'college-comp__recruit-coach-block')

                    recruited_by_text = commitment_recruited_div.find_elements(By.TAG_NAME, 'a')
                    for recruits in recruited_by_text:
                        '''This for loop used for iterate all recruiters names'''
                        recruited_names = recruits.text
                        recruited_list.append(recruited_names)

                    commitments_list = {'committed_team_name': commitment_team_name,
                                        'committed_img_url': commitment_team_img_url_src,
                                        'recruited_list': recruited_list}

        except:

            recruited_list = []
            ul_lists_of_teams = browser.find_element(By.CLASS_NAME, 'college-comp__body-list')
            li_lists_of_teams = ul_lists_of_teams.find_elements(By.CLASS_NAME, 'college-comp__body-list-item')
            for teams_list in li_lists_of_teams:
                '''This for loop is used for iterate all lists of commitments'''
                if teams_list.find_element(By.TAG_NAME, 'span').text == 'Enrolled' or 'Committed':
                    commitment_team_name = teams_list.find_element(By.CLASS_NAME, 'college-comp__team-name-link').text
                    commitment_team_img_url = teams_list.find_element(By.CLASS_NAME, 'college-comp__college-team-image')
                    commitment_team_img_url_src = commitment_team_img_url.get_attribute('src')
                    commitment_recruited_div = teams_list.find_element(By.CLASS_NAME,
                                                                       'college-comp__recruit-coach-block')

                    recruited_by_text = commitment_recruited_div.find_elements(By.TAG_NAME, 'a')
                    for recruits in recruited_by_text:
                        '''This for loop used for iterate all recruiters names'''
                        recruited_names = recruits.text
                        recruited_list.append(recruited_names)

                    commitments_list = {'committed_team_name': commitment_team_name,
                                        'committed_img_url': commitment_team_img_url_src,
                                        'recruited_list': recruited_list}

        try:
            offer_dict = {}

            view_complete_team_list = browser.find_element(By.CLASS_NAME, 'college-comp__view-all')
            if view_complete_team_list:
                view_complete_team_list.click()
                time.sleep(2)
            offer_school_names_list = browser.find_elements(By.CLASS_NAME, 'recruit-interest-index_lst')

            for offer_school_names in offer_school_names_list:

                offer_school_img_url = offer_school_names.find_elements(By.XPATH, "//img[@class='jsonly']")

                for offer_img_url_list in offer_school_img_url:
                    offer_img_url_list_src = offer_img_url_list.get_attribute('src')
                    offer_img_url_list_name = offer_img_url_list.get_attribute('title')
                    offer_dict.update({offer_img_url_list_name: offer_img_url_list_src})


        except:

            '''This except block is used for if there is not found view_complete_list button'''

            offer_dict = {}

            offer_school_names_list = browser.find_elements(By.CLASS_NAME, 'recruit-interest-index_lst')

            for offer_school_names in offer_school_names_list:

                offer_school_img_url = offer_school_names.find_elements(By.XPATH, "//img[@class='jsonly']")

                for offer_img_url_list in offer_school_img_url:
                    offer_img_url_list_src = offer_img_url_list.get_attribute('src')
                    offer_img_url_list_name = offer_img_url_list.get_attribute('title')
                    offer_dict.update({offer_img_url_list_name: offer_img_url_list_src})
    except:
        offer_dict = None
        commitments_list = None

    player_info = [text_img_url, player_name, player_pos, player_height, player_weight, player_high_school,
                   player_city, player_state, player_class, offer_dict, commitments_list]

    browser.close()
    with open(file_name, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(player_info)

    return


def get_prospect_url(team_name):
    '''This function is used for create url for go prospect teams player page'''
    name = team_name
    rename = name.replace("&", "")
    name_without = rename.replace(" ", "-")

    url = f'https://247sports.com/college/{name_without}/Season/2023-Football/Targets/'
    return url


def create_csv_file():
    '''This function is used for create csv file by considering datetime'''
    try:
        current_time_span = datetime.datetime.now().strftime("%f")
        file_name = f"player_info_{current_time_span}.csv"
        header = ['Player Image Url', 'Player Name', 'Player Position', 'Player Height', 'Player Weight',
                  'Player High School Name', 'Player City Name', 'Player state', 'Player Class', 'Offers Dictionary',
                  'Commitments Dictionary']
        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(header)
        return file_name
    except:
        raise Exception("Csv file not created")


def main():
    '''This is main function , execution starts from this function'''
    try:
        browser = webdriver.Firefox()
        file_name = create_csv_file()
        browser.get('https://247sports.com/college/football/recruiting/')
        browser.implicitly_wait(3)
        team_ranking_button = browser.find_element(By.LINK_TEXT, 'TEAM RANKINGS')
        team_ranking_button.click()
        headers = {
            'User-Agent': 'Mozilla/5.0 (windows NT 10.0; win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        browser.get('https://247sports.com/Season/2023-Football/CompositeTeamRankings/')

        url = "https://247sports.com/Season/2023-Football/CompositeTeamRankings/"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        team_container = soup.find('ul', class_='rankings-page__list')
        team_elements = team_container.find_all('li', class_='rankings-page__list-item')

        for team_element in team_elements:
            '''This for loop used to iterate teams'''
            team_name = team_element.find('a', class_='rankings-page__name-link').text.strip()
            team_url = team_element.find(class_='rankings-page__name-link')['href']

            browser.get(team_url)
            time.sleep(2)
            print(f'{team_name}->>')
            prospect_url = get_prospect_url(team_name)
            print(prospect_url)
            browser.get(prospect_url)
            browser.implicitly_wait(3)
            player_count = 1
            player_container = browser.find_elements(By.CLASS_NAME, 'ri-page__name-link')

            for player_element in player_container:

                '''This for loop is used to iterate players'''
                player_name = player_element.text
                player_url = browser.find_element(By.LINK_TEXT, player_name)
                player_info_url = player_url.get_attribute('href')

                get_player_info(player_info_url, file_name)
                player_count += 1
                if player_count == 51:
                    break

            browser.back()
            browser.back()


    except:
        raise Exception("web driver exception occur")


main()
