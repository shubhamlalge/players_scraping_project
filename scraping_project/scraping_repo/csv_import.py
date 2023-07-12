import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraping_repo.settings')
# to load settings
django.setup()

from players.models import Player, Position, Class, State, School, City, Commitment, Offer,HighSchool


def import_csv_to_models():
    '''This function used for convert csv data into models  '''
    # open csv file and read
    with open('player_info_20230619143136(copy).csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        # skip first row from csv because it contains header
        next(reader)
        commitment = None
        # loop over csv
        for players in reader:
            try:
                # commitments = eval(row[10])
                # commited_team_url = commitments.get('committed_img_url')
                # create or get position object
                position, _ = Position.objects.get_or_create(position=players[2])
                # create or get class object
                class_, _ = Class.objects.get_or_create(classes=players[8])
                # create or get state object
                state, _ = State.objects.get_or_create(state=players[7])
                # create or get city object
                city, _ = City.objects.get_or_create(name=players[6])
                # create or get high school name object
                high_school, _ = HighSchool.objects.get_or_create(name=players[5])

            except Exception as error:
                print(error)
            try:
                # evaluate commitment elements from csv
                commitments = eval(players[10])
                # get recruiters list
                recruiters = commitments.get('recruited_list')
                # create commitment object using get or create method
                commitment, _ = Commitment.objects.get_or_create(recruiters=recruiters)


            except Exception as error:
                print(error)

            try:
                # create or get player object using model fields
                player_object, _ = Player.objects.get_or_create(image_url=players[0], full_name=players[1],
                                                                height=players[3],
                                                                weight=players[4], city=city, position=position,
                                                                state=state, clas=class_,high_school =high_school,
                                                                commitment= commitment)
                # take offers from csv and evaluate data
                offers_elements = eval(players[9])
                # loop over offer teams
                for teams_data in offers_elements.items():
                    # store team name
                    team_name = teams_data[0]
                    # store team url
                    team_url = teams_data[1]
                    # create or get school name object
                    school, _ = School.objects.get_or_create(name=team_name)
                    school.url = team_url
                    school.save()
                    # create or get offer object
                    offer, _ = Offer.objects.get_or_create(school=school)
                    # add offer object in player object
                    player_object.offer.add(offer)
                    # save school object in commitment
                commitment.school = school
                commitment.save()
                print("data inserted")
            except Exception as error:
                print(error)


if __name__ == '__main__':
    # main function call from here
    import_csv_to_models()
