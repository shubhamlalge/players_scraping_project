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
    with open('players/player_info_20230619143136(copy).csv', 'r') as csvfile:
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

            try:
                # create class object with name field
                class_, _ = Class.objects.get_or_create(name=player[8])
            except Exception as error:
                print(error)

            try:
                # create state object with name field
                state, _ = State.objects.get_or_create(name=player[7])
            except Exception as error:
                print(error)

            try:
                # create city object with name field
                city, _ = City.objects.get_or_create(name=player[6])
            except Exception as error:
                print(error)

            try:

                # create or get player object using model fields
                player_obj = Player.objects.create(image_url=player[0], full_name=player[1],
                                                   height=player[3],
                                                   weight=player[4], city=city, position=position,
                                                   state=state, clas=class_)
            except Exception as error:
                print(error)

            try:
                # Create an offer object and associate it with the player
                offer = Offer.objects.create(player=player_obj)
                # take offers from csv and evaluate data
                offers_elements = eval(player[9])

                # loop over offer teams
                for team_name, team_url in offers_elements.items():
                    # Create or get a school object with the name field
                    school, _ = School.objects.get_or_create(name=team_name)
                    school.url = team_url
                    school.save()
                    player_obj.school =school
                    player_obj.save()
                    # Add the school to the offer
                    offer.schools.add(school)
                    # Evaluate commitment elements from the CSV
                    commitments = eval(player[10])
                    # Get the recruiters list
                    recruiters = commitments.get('recruited_list')
                    commited_offer = commitments.get('committed_team_name')
                    if school.name == commited_offer:
                        # Create a commitment object with recruiters field
                        commitment, _ = Committment.objects.get_or_create(
                            recruiters=recruiters,
                            school=school
                        )
                        player_obj.commitment = commitment
                        # Save the player object
                        player_obj.save()
                        print("data inserted")
            except Exception as error:
                print(error)


if __name__ == '__main__':
    # main function call from here
    import_csv_to_models()
