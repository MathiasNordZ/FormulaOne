import httpx
from fastapi import FastAPI
from models.models import Driver, RacePosition

app = FastAPI()

base_url = "https://api.openf1.org/v1/"

"""
Method that creates a route '/drivers'.
Returns an array of driver objects.
"""
@app.get("/drivers")
async def get_drivers():
  # Will get all drivers from API.
  async with httpx.AsyncClient() as client:
    driver_url = f"{base_url}drivers?session_key=latest"
    response = await client.get(driver_url)
    data = response.json()

  return [
    Driver(
        driver_name = driver["full_name"],
        team_name = driver["team_name"],
        driver_number = driver["driver_number"],
        name_acronym= driver["name_acronym"]
    )
    for driver in data
  ]

"""
Method that creates a route '/positions'
Returns an array of position objects.
"""
@app.get("/positions")
async def get_positions():
  # Will get all positions from API.
  async with httpx.AsyncClient() as client:
    position_url = f"{base_url}position?session_key=latest"
    response = await client.get(position_url)
    data = response.json()

  return [
    RacePosition (
        date = pos_data["date"],
        driver_number = pos_data["driver_number"],
        position = pos_data["position"]
    )
    for pos_data in data
  ]
