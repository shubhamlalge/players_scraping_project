import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraping_repo.settings')
# to load settings
django.setup()

from players.models import Player, Position, Class, State, School, City, Commitment, Offer


def import_csv_to_models():
    '''This function used for convert csv data into models  '''
    # open csv file and read
    with open('player_info_20230619143136(copy).csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        # skip first row from csv because it contains header
        next(reader)
        recruiter =[]
        # loop over csv
        for row in reader:
            try:
                # create or get position object
                position, _ = Position.objects.get_or_create(position=row[2])
                # create or get class object
                class_, _ = Class.objects.get_or_create(classes=row[8])
                # create or get state object
                state, _ = State.objects.get_or_create(state=row[7])
                # create or get city object
                city, _ = City.objects.get_or_create(name=row[6])
            except Exception as error:
                print(error)
                # player_object, _ = Player.objects.get_or_create(image_url=row[0], full_name=row[1], height=row[3],
                #                                                 weight=row[4], city=city, position=position,
                #                                                 state=state, clas=class_,
                #                                                 school_name=school,commitment=commitment)
            try:
                # take offers from csv and evaluate data
                offers_elements = eval(row[9])
                # loop over offer teams
                for teams_data in offers_elements.items():
                    # store team name
                    team_name = teams_data[0]
                    # store team logo
                    team_logo_url =teams_data[1]
                    # create or get school name object
                    school, _ = School.objects.get_or_create(name=row[5],url =team_logo_url)
                    # create or get team object
                    offer, _ = Offer.objects.get_or_create(name=team_name,school= school)
                    player_object.offer.add(offer)

            except Exception as error:
                print(error)

            try:
                # evaluate commitments
                commitments = eval(row[10])
                # take recruiter list and loop over them
                commited_team_name = commitments.get('committed_team_name')
                commited_team_url = commitments.get('committed_img_url')

                recruiters =commitments.get('recruited_list')
                print(recruiters)

                commitment, _ = Commitment.objects.get_or_create(recruiters_name=recruiters, name=commited_team_name,
                                                                 school=school)
                # player_object.commitment.add(commitment)
                # player_object.save()
            except Exception as error:
                print(error)
            try:
                # create or get player object using model fields
                player_object, _ = Player.objects.get_or_create(image_url=row[0], full_name=row[1], height=row[3],
                                                                weight=row[4], city=city, position=position,
                                                                state=state, clas=class_,
                                                                school_name=school, commitment=commitment)
                # add all offers into player

                print("data inserted")
            except Exception as error:
                print(error)


if __name__ == '__main__':
    # main function call from here
    import_csv_to_models()
