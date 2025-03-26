class Driver(object):
  def __init__(self, driver_name: str, team_name: str,
      driver_number: int, name_acronym:str):
    self.driver_name = driver_name
    self.team_name = team_name
    self.driver_number = driver_number
    self.name_acronym = name_acronym

class RacePosition(object):
  def __init__(self, date:str, driver_number:int, position:int):
    self.date = date
    self.driver_number = driver_number
    self.position = position