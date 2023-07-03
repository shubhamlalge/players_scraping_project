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
                    csv_player_wt = player_data_csv[4]
                    csv_player_ht = player_data_csv[3]
                    csv_player_pos = player_data_csv[2]
                    player_class = player_data_csv[8]
                    try:
                        # calling function for get url for scrap data
                        player_updation_url = update_profile_url(player_name, player_class)
                        browser = webdriver.Firefox()
                        try:

                            # go to player update info page
                            browser.get(player_updation_url)
                            time.sleep(2)

                            players = browser.find_elements(By.CLASS_NAME, 'player')
                            for i in players:
                                # scrap player name , pos , ht, wt using class name and tag name
                                li_player_name = i.find_element(By.CLASS_NAME, 'name')
                                player_name = li_player_name.find_element(By.TAG_NAME, 'a')
                                # here we get player url
                                player_url = player_name.get_attribute('href')
                                # here we get pos of player
                                li_player_pos = i.find_element(By.CLASS_NAME, 'position')
                                player_pos = li_player_pos.find_element(By.TAG_NAME, 'span').text
                                li_player_ht_wt = i.find_element(By.CLASS_NAME, 'size')
                                player_ht_wt = li_player_ht_wt.find_element(By.TAG_NAME, 'span').text.strip()
                                # here we split ht and wt
                                player = player_ht_wt.split('/')
                                player_ht = player[0].strip()
                                player_wt = player[1].strip()

                                time.sleep(2)
                                result = False
                                try:
                                    # here we compare player elements with csv data
                                    if player_pos == csv_player_pos and \
                                            player_ht== csv_player_ht and player_wt== csv_player_wt:
                                        time.sleep(2)

                                        result = True
                                        break
                                except Exception as e:
                                    print(e)
                            if result:
                                # click on player profile url
                                li_player_name.click()
                                try:
                                    # fetch all player data
                                    data = get_player_info(player_url)
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
                                        browser.close()

                                    print("Data updated")
                                except Exception as e:
                                    print(e)

                                else:
                                    print("player info not Matched")

                        except Exception as e:
                            print(e)

                    except Exception as e:
                        print(e)

    except Exception as e:
        print(e)


def update_profile_url(player_name, player_class):
    '''This function is used for get updated player page link'''
    try:
        url = f"https://247sports.com/Season/{player_class}-Football/Recruits/?&Player.FullName={player_name}"
        return url
    except Exception as e:
        print(e)


if __name__ == '__main__':
    start_update_script()
