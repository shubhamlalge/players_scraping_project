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
    # These are the global variables which we use in try except block
    text_img_url, player_name, player_pos, player_height, player_weight, player_high_school, player_city, \
        player_state, player_class, li_lists_of_teams = None, None, None, None, None, None, None, None, None, None

    try:
        # here get function is used to go player url
        browser.get(player_url)
        # sleep method used to stop execution for 3 sec
        time.sleep(3)
        # To scrap -> player name <- we use find element method and scrap BY using XPATH and get text of player name
        player_name = browser.find_element(By.XPATH, "//h1[@class='name']").text
        # Here to scrap ->player_img_url<- we scrap url using tag name and get there src link using get_attribute method
        player_img = browser.find_element(By.TAG_NAME, 'img')
        player_img_url = player_img.get_attribute('src')
        # Here we use f string to convert url to string
        text_img_url = f"{player_img_url}"
        # To scrap pos , height , weight , high school name , city, state we find ul list using class name
        ul_first_list_info = browser.find_element(By.CLASS_NAME, 'metrics-list')
        # Then we find span tags which are present in ul list using tag name and save list of elements
        span_tags_info = ul_first_list_info.find_elements(By.TAG_NAME, 'span')

        # here we use indexing to scrap elements if not found elements then make it None
        try:
            player_pos = span_tags_info[1].text
        except Exception as e:
            player_pos = None
            print(e)
        try:
            player_height = span_tags_info[3].text
        except Exception as e:
            player_height = None
            print(e)
        try:
            player_weight = span_tags_info[5].text
        except Exception as e:
            player_weight = None
            print(e)

        # Here same we want to scrap high school , city ,state ,class then we find ul and span tags
        ul_second_info = browser.find_element(By.CLASS_NAME, 'details ')
        span_info = ul_second_info.find_elements(By.TAG_NAME, 'span')

        try:
            # here we use indexing to scrap elements if not found elements then make it None

            player_high_school = span_info[1].text
            player_city_first = span_info[3].text
        except Exception as e:
            print(e)
            # here we add one more condition if city is not found at index 3 then go to index 1
            try:
                player_city_first = span_info[1].text
            except Exception as e:
                player_city_first = None
                print(e)
        # in player_city_first we have to elements, so we split it and save in different variables
        player_city_state = player_city_first.split(',')
        try:
            # then scrap using indexing
            player_city = player_city_state[0]
            player_state = player_city_state[1]
        except Exception as e:
            print(e)
            player_city = None
            player_state = None
        try:
            player_classes = span_info[5].text
            player_class = player_classes[:4]
        except Exception as e:
            player_class = None
            print(e)
    except Exception as e:
        # if you can't found browser I throw an exception
        print(e)

    try:
        # here we globally declare dictionary for commitments
        commitments_list = {}
        try:
            # in below variable we find view profile link using class name
            view_recruting_profile = browser.find_element(By.CLASS_NAME, 'view-profile-link')

            recruited_list = []

            # This if condition used for check in web page we have view_recruiting_profile link or not
            try:
                if view_recruting_profile:
                    view_recruting_profile.click()
                    time.sleep(2)
            except Exception as e:
                print(e)
            # here we find ul list then find li list using class name
            try:
                ul_lists_of_teams = browser.find_element(By.CLASS_NAME, 'college-comp__body-list')
                li_lists_of_teams = ul_lists_of_teams.find_elements(By.CLASS_NAME, 'college-comp__body-list-item')
            except Exception as e:
                print(e)
            commitment_recruited_div = None
            commitment_team_img_url_src = None
            commitment_team_name = None
            try:
                for teams_list in li_lists_of_teams:
                    # This for loop is used for iterate all lists of commitments
                    if teams_list.find_element(By.TAG_NAME, 'span').text == 'Enrolled' or 'Committed':
                        # This if condition used for verify the player is Enrolled or Committed for particular team
                        # Here we find commitment team info using class name
                        try:
                            commitment_team_name = teams_list.find_element(By.CLASS_NAME,
                                                                           'college-comp__team-name-link').text
                            commitment_team_img_url = teams_list.find_element(By.CLASS_NAME,
                                                                              'college-comp__college-team-image')
                            commitment_team_img_url_src = commitment_team_img_url.get_attribute('src')
                            commitment_recruited_div = teams_list.find_element(By.CLASS_NAME,
                                                                               'college-comp__recruit-coach-block')
                        except Exception as e:
                            print(e)
                        # Here we find recruiters text using tag name
                        try:
                            recruited_by_text = commitment_recruited_div.find_elements(By.TAG_NAME, 'a')
                            for recruits in recruited_by_text:
                                # This for loop used for iterate all recruiters names
                                recruited_names = recruits.text
                                recruited_list.append(recruited_names)

                            commitments_list = {'committed_team_name': commitment_team_name,
                                                'committed_img_url': commitment_team_img_url_src,
                                                'recruited_list': recruited_list}
                        except Exception as e:
                            print(e)
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
        offer_dict = {}
        try:
            view_complete_team_list = browser.find_element(By.CLASS_NAME, 'college-comp__view-all')
            # Here we find view complete list link and click if we found
            if view_complete_team_list:
                view_complete_team_list.click()
                time.sleep(2)
        except Exception as e:
            print(e)
        try:
            offer_school_names_list = browser.find_elements(By.CLASS_NAME, 'recruit-interest-index_lst')
            # Here we find list of offers list and iterate one by one
            for offer_school_names in offer_school_names_list:

                offer_school_img_url = offer_school_names.find_elements(By.XPATH, "//img[@class='jsonly']")
                # Here we find img urls with the help of this urls we scrap src and title name
                for offer_img_url_list in offer_school_img_url:
                    offer_img_url_list_src = offer_img_url_list.get_attribute('src')
                    offer_img_url_list_name = offer_img_url_list.get_attribute('title')
                    offer_dict.update({offer_img_url_list_name: offer_img_url_list_src})
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
        # here we declare None for offers and commitments
        offer_dict = None
        commitments_list = None
    # Here we store all elements in list
    player_info = [text_img_url, player_name, player_pos, player_height, player_weight, player_high_school,
                   player_city, player_state, player_class, offer_dict, commitments_list]
    browser.close()
    with open(file_name, 'a') as file:
        # Add our players info in csv file which already created
        writer = csv.writer(file)
        writer.writerow(player_info)

    return player_info


def get_prospect_url(team_name):
    '''This function is used for create url for go prospect teams player page'''
    name = team_name
    # Here we replace & with none and  blank space with - and return it
    rename = name.replace("&", "")
    name_without = rename.replace(" ", "-")

    url = f'https://247sports.com/college/{name_without}/Season/2023-Football/Targets/'
    return url


def create_csv_file():
    '''This function is used for create csv file by considering datetime'''
    try:
        # Here we use datetime module which used to found unique number for our csv file name
        current_time_span = datetime.datetime.now().strftime("%f")
        # we store in file name variable and use f string to use datetime microseconds
        file_name = f"player_info{current_time_span}.csv"
        # This header list used to display in csv heading for column head name
        header = ['Player Image Url', 'Player Name', 'Player Position', 'Player Height', 'Player Weight',
                  'Player High School Name', 'Player City Name', 'Player state', 'Player Class', 'Offers Dictionary',
                  'Commitments Dictionary']
        with open(file_name, 'w') as file:
            # here we use open function to open and write our file
            writer = csv.writer(file)
            # here we write our csv file
            writer.writerow(header)
            # here we add header first row
        return file_name
    except:
        print("Csv file not created")


def main():
    '''This is main function , execution starts from this function'''
    try:

        browser = webdriver.Firefox()
        # Here we call function for create csv file
        file_name = create_csv_file()
        # here we go to 247sports website
        browser.get('https://247sports.com/college/football/recruiting/')
        # here we wait for 3 sec
        browser.implicitly_wait(3)
        # here we find team ranking button and click it
        team_ranking_button = browser.find_element(By.LINK_TEXT, 'TEAM RANKINGS')
        team_ranking_button.click()
        # this header used in beautiful soup
        headers = {
            'User-Agent': 'Mozilla/5.0 (windows NT 10.0; win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        # This url is used to go 2023 team list
        url = "https://247sports.com/Season/2023-Football/CompositeTeamRankings/"
        soup = None
        team_elements = None
        team_name = None
        player_element = None
        try:
            response = requests.get(url, headers=headers)
            # using beautiful soup we found html data
            soup = BeautifulSoup(response.content, 'html.parser')
        except:
            print("url not found")
        # here we find ul and li list for teams
        try:
            team_container = soup.find('ul', class_='rankings-page__list')
            team_elements = team_container.find_all('li', class_='rankings-page__list-item')
        except:
            print("ul list not found")
        try:
            for team_element in team_elements:
                # This for loop used to iterate teams
                # Here we find team name and url using class name
                try:
                    team_name = team_element.find('a', class_='rankings-page__name-link').text.strip()
                    team_url = team_element.find(class_='rankings-page__name-link')['href']
                    # Then we go team url using webdriver get function
                    browser.get(team_url)
                    time.sleep(2)
                except Exception as e:
                    print(e)
                # Here we call function for create prospect url using team name
                try:
                    prospect_url = get_prospect_url(team_name)
                    # here we go prospect teams
                    browser.get(prospect_url)
                    browser.implicitly_wait(3)
                except Exception as e:
                    print(e)
                player_count = 1
                # here we find player elements
                try:
                    player_container = browser.find_elements(By.CLASS_NAME, 'ri-page__name-link')

                    for player_element in player_container:
                        # This for loop is used to iterate players
                        player_name = player_element.text
                        # here we find player url using link text of player name
                        player_url = browser.find_element(By.LINK_TEXT, player_name)
                        player_info_url = player_url.get_attribute('href')
                        try:
                            # Here we call function for scrap player information
                            get_player_info(player_info_url, file_name)
                        except Exception as e:
                            print(e)
                        player_count += 1
                        # Here we apply if condition for we scrap only 50 players then break the loop
                        if player_count == 51:
                            break
                except Exception as e:
                    print(e)
                # Here we double back our page to go teams
                browser.back()
                browser.back()
        except Exception as e:
            print(e)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
