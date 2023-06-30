from selenium import webdriver
import csv
from selenium.webdriver.common.by import By
import time
from team_wise_scrap import get_player_info


def start_update_script():
    '''This is main function execution starts from here'''
    try:
        # Here we open csv file and read it
        with open('player_info_20230619143136(copy).csv', 'r') as csvfile:

            reader = csv.reader(csvfile)
            # convert csv data into list
            row_list = list(reader)
            row_num = 2
            # iterate list of rows of data using enumerate function
            for index, player_data_csv in enumerate(row_list):
                # apply  condition for start updating from row 1
                if index == row_num - 1:

                    time.sleep(2)
                    # here we declare data from csv
                    player_name = player_data_csv[1]
                    player_wt = player_data_csv[4]
                    player_ht = player_data_csv[3]
                    player_pos = player_data_csv[2]
                    player_class = player_data_csv[8]
                    try:
                        # calling function for get url for scrap data
                        player_updation_url = update_profile_url(player_name, player_class)
                        # calling function to scrap player name , pos, ht and wt
                        player_updated_list, li_player_name, player_url_link, browser = player_updated_info(
                            player_updation_url)
                    except Exception as e:
                        print(e)

                        player_url = li_player_name

                        time.sleep(2)
                    try:
                        # here we compare player elements with csv data
                        if player_updated_list[0] == player_name and player_updated_list[1] == player_pos and \
                                player_updated_list[2] == player_ht and player_updated_list[3] == player_wt:
                            time.sleep(2)
                            # click on player profile url
                            player_url.click()
                            browser.close()
                    except Exception as e:
                        print(e)
                        try:
                            # fetch all player data
                            data = get_player_info(player_url_link)
                            # change csv data to scrap data using index
                            row_list[row_num - 1] = data
                            row_num += 1
                        except Exception as e:
                            print(e)
                        try:
                            # open csv file and overwrite row list
                            with open('player_info_20230619143136(copy).csv', 'w', newline="") as file:
                                writer = csv.writer(file)
                                writer.writerows(row_list)

                            print("Data updated")
                        except Exception as e:
                            print(e)


                        else:
                            print("player info not Matched")

    except Exception as e:
        print(e)


def update_profile_url(player_name, player_class):
    '''This function is used for get updated player page link'''
    try:
        url = f"https://247sports.com/Season/{player_class}-Football/Recruits/?&Player.FullName={player_name}"
        return url
    except Exception as e:
        print(e)


def player_updated_info(player_updation_url):
    browser = webdriver.Firefox()
    try:
        # go to player update info page
        browser.get(player_updation_url)
        time.sleep(2)
        # scrap player name , pos , ht, wt using class name and tag name
        li_player_name = browser.find_element(By.CLASS_NAME, 'name')
        player_name = li_player_name.find_element(By.TAG_NAME, 'a')
        player_url = player_name.get_attribute('href')
        li_player_pos = browser.find_element(By.CLASS_NAME, 'position')
        player_pos = li_player_pos.find_element(By.TAG_NAME, 'span').text
        li_player_ht_wt = browser.find_element(By.CLASS_NAME, 'size')
        player_ht_wt = li_player_ht_wt.find_element(By.TAG_NAME, 'span').text.strip()
        player = player_ht_wt.split('/')
        player_ht = player[0].strip()
        player_wt = player[1].strip()
        player_updated_list = [player_name.text, player_pos, player_ht, player_wt]
        time.sleep(2)

        return player_updated_list, li_player_name, player_url, browser

    except Exception as e:
        print(e)


if __name__ == '__main__':
    start_update_script()
