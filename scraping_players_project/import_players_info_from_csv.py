import csv
import os
import django

# it is mapping object
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraping_repo.settings')
# to configure a settings because we use ORM
django.setup()
from players.models import Player, Position, Class, State, School, City, Committment, Offer


def import_csv_to_models():
    '''This function used for convert csv data into models  '''
    # open csv file and read
    with open('players/player_info_20230619143136.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        # skip first row from csv because it contains header
        next(reader)

        # loop over csv
        for player in reader:
            try:
                # create position object with name field
                position, _ = Position.objects.get_or_create(name=player[2])
            except Exception as error:
                print(error)
                position = None

            try:
                # create class object with name field
                player_class, _ = Class.objects.get_or_create(name=player[8])
            except Exception as error:
                print(error)
                player_class = None

            try:
                # create state object with name field
                state, _ = State.objects.get_or_create(name=player[7])
            except Exception as error:
                print(error)
                state = None

            try:
                # create city object with name field
                city, _ = City.objects.get_or_create(name=player[6])
            except Exception as error:
                print(error)
                city = None
            try:
                school, _ = School.objects.get_or_create(name=player[5])
            except Exception as error:
                print(error)
                school = None

            try:

                # create or get player object using model fields
                player_obj, _ = Player.objects.get_or_create(image_url=player[0], full_name=player[1],
                                                             height=player[3],
                                                             weight=player[4], city=city, position=position,
                                                             state=state, clas=player_class, school=school)
            except Exception as error:
                print(error)

            try:
                # Create an Offer object and associate it with the player
                offer = Offer.objects.create(player=player_obj)
                # Take offers from the CSV and evaluate the data
                offers_elements = eval(player[9])

                # Loop over offer teams
                for team_name, team_url in offers_elements.items():
                    # Create or get a School object with the name field
                    school, _ = School.objects.get_or_create(name=team_name)
                    # set offer urls in school
                    school.url = team_url
                    school.save()
                    # Add the school to the offer
                    offer.schools.add(school)
                # Evaluate commitment elements from the CSV
                commitments = eval(player[10])
                # Get the recruiters list
                recruiters = commitments.get('recruited_list')
                committed_team_name = commitments.get('committed_team_name')

                # Check if the player has committed to a school
                if committed_team_name:
                    try:
                        # Find the school for the committed_team_name
                        committed_school = School.objects.get(name=committed_team_name)

                        # Create a commitment object with recruiters field
                        commitment, _ = Committment.objects.get_or_create(
                            recruiters=recruiters,
                            school=committed_school
                        )

                        # Set the commitment for the player
                        player_obj.commitment = commitment

                    except Exception as error:
                        print(error)

                # Save the player object after setting the commitment and school
                player_obj.save()

                print("Data inserted successfully for player:", player[1])
            except Exception as error:
                print(error)


if __name__ == '__main__':
    # main function call from here
    import_csv_to_models()
