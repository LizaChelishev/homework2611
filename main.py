
from db_config import create_all_entities
from db_repo import DbRepo
from Tourist import Tourist
from Attraction import Attraction
from Visit import Visit

local_session = create_all_entities()
repo = DbRepo(local_session)


repo.reset_auto_inc(Tourist)
repo.reset_auto_inc(Attraction)
repo.reset_auto_inc(Visit)

tourists_list = [Tourist(name='Liza', origin_country='Israel'), Tourist(name='Victoria',
                                                                              origin_country='Germany')]
repo.add_all(tourists_list)
attractions_list = [Attraction(name='Museum', price=60), Attraction(name='National Park', price=120),
                    Attraction(name='Restaurant', price=500)]
repo.add_all(attractions_list)

visits_list = [Visit(tourist_id=1, attraction_id=2, year_of_visit=2009),
               Visit(tourist_id=1, attraction_id=3, year_of_visit=2003),
               Visit(tourist_id=2, attraction_id=1, year_of_visit=2020),
               Visit(tourist_id=2, attraction_id=2, year_of_visit=2017),
               Visit(tourist_id=1, attraction_id=1, year_of_visit=2021)]

repo.add_all(visits_list)

repo.get_visit_by_tourist_id()