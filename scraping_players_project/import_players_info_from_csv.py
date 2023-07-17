import csv
import os
import django

# it is mapping object
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraping_repo.settings')
# to configure a settings because we use ORM
django.setup()
from players.models import Player, Position, Class, State, School, City, Commitment, Offer


def import_csv_to_models():
    '''This function used for convert csv data into models  '''
    # open csv file and read
    with open('players/player_info_20230619143136(copy).csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        # skip first row from csv because it contains header
        next(reader)

        # loop over csv
        for players in reader:
            try:
                # create position object with name field
                position, _ = Position.objects.get_or_create(name=players[2])
            except Exception as error:
                print(error)

            try:
                # create class object with name field
                class_, _ = Class.objects.get_or_create(name=players[8])
            except Exception as error:
                print(error)

            try:
                # create state object with name field
                state, _ = State.objects.get_or_create(name=players[7])
            except Exception as error:
                print(error)

            try:
                # create city object with name field
                city, _ = City.objects.get_or_create(name=players[6])
            except Exception as error:
                print(error)

            try:

                # create or get player object using model fields
                player_obj = Player.objects.create(image_url=players[0], full_name=players[1],
                                                   height=players[3],
                                                   weight=players[4], city=city, position=position,
                                                   state=state, clas=class_)
            except Exception as error:
                print(error)

            try:

                # take offers from csv and evaluate data
                offers_elements = eval(players[9])
                # loop over offer teams
                for teams_data in offers_elements.items():
                    # store team name
                    team_name = teams_data[0]
                    # store team url
                    team_url = teams_data[1]
                    # create school object with name field
                    school = School.objects.create(name=team_name)
                    # give urls to school url
                    school.url = team_url
                    school.save()
                    # save school object in player object
                    player_obj.school = school
                    player_obj.save()
                    # create offer object with player field
                    offer = Offer.objects.create(player=player_obj)
                    # add school object in offer
                    offer.schools.add(school)

            except Exception as error:
                print(error)
            try:
                # evaluate commitment elements from csv
                commitments = eval(players[10])
                # get recruiters list
                recruiters = commitments.get('recruited_list')
                # create commitment object with recruiters and school field
                commitment = Commitment.objects.create(recruiters=recruiters, school=school)
                player_obj.commitment = commitment
                player_obj.save()
                print("data inserted")
            except Exception as error:
                print(error)


if __name__ == '__main__':
    # main function call from here
    import_csv_to_models()
