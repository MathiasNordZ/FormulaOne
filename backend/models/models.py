"""
Model for the driver info.
"""
class Driver(object):
  def __init__(self, driver_name: str, team_name: str,
      driver_number: int, name_acronym:str):
    self.driver_name = driver_name
    self.team_name = team_name
    self.driver_number = driver_number
    self.name_acronym = name_acronym

"""
Model for the position in the leaderboard.
"""
class RacePosition(object):
  def __init__(self, date:str, driver_number:int, position:int):
    self.date = date
    self.driver_number = driver_number
    self.position = position

"""
Model for the session info.
"""
class SessionInfo(object):
  def __init__(self, circuit_name:str, country:str, session_name:str,
      session_type:str, date_end:str, date_start:str):
    self.circuit_name = circuit_name
    self.country = country
    self.session_name = session_name
    self.session_type = session_type
    self.date_end = date_end
    self.date_start = date_start