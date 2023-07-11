from django.core.management.base import BaseCommand
from scraping_repo.players.models import Player, Position, Class, State, School, City, Commitment, Offer
import csv


class Command(BaseCommand):
    def import_csv_to_models(self):
        '''This function used for convert csv data into models  '''
        # open csv file and read
        with open('player_info_20230619143136(copy).csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            # skip first row from csv because it contains header
            next(reader)
            recruiter = []
            team_name = []
            team_logo_url = []
            # loop over csv
            for row in reader:
                try:
                    # create or get position object
                    position, _ = Position.objects.get_or_create(position=row[2])
                    # create or get class object
                    class_, _ = Class.objects.get_or_create(classes=row[8])
                    # create or get state object
                    state, _ = State.objects.get_or_create(state=row[7])
                    # create or get school name object
                    schoolname, _ = School.objects.get_or_create(name=row[5])
                    # create or get city object
                    city, _ = City.objects.get_or_create(name=row[6])
                except Exception as error:
                    print(error)
                try:
                    # take offers from csv and evaluate data
                    offers_elements = eval(row[9])
                    # loop over offer teams
                    for teams_data in offers_elements.items():
                        # store team name
                        team_name.append(teams_data[0])
                        # store team logo
                        team_logo_url.append(teams_data[1])

                        # create or get team object
                        team, _ = Team.objects.get_or_create(name=team_name, logo_url=team_logo_url)

                    try:
                        # evaluate commitments
                        commitments = eval(row[10])
                        # take recruiter list and loop over them
                        for recruiters in commitments.get('recruited_list'):
                            # create or get commitment
                            commitment, _ = Commitment.objects.get_or_create(recruiters_name=recruiters, team=team)


                    except Exception as error:
                        print(error)
                    try:
                        # create or get player object using model fields
                        player_object, _ = Player.objects.get_or_create(image_url=row[0], full_name=row[1],
                                                                        height=row[3],
                                                                        weight=row[4], city=city, position=position,
                                                                        state=state, clas=class_,
                                                                        school_name=schoolname, commitment=commitment)
                        # # add all offers into player
                        player_object.offer.add(team)

                        print("data inserted")
                    except Exception as error:
                        print(error)
                except Exception as error:
                    print(error)
        self.stdout.write("command executed successfully")