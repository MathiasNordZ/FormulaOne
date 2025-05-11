from urllib.request import urlopen
import matplotlib.pyplot as plt
import json

"""
The RequestHandler class handles the request, that will respond with a JSON.
"""
class RequestHandler:
    def __init__(self, url):
        self.url = url

    def load_data(self):
        if len(self.url) == 0 or self.url is None:
            raise ValueError

        response = urlopen(self.url)
        data = json.loads(response.read().decode("utf-8"))
        pretty_data = json.dumps(data, indent=2)
        response.close()

        return data

    def filter_by_driver(self, data, driver_number):
        return [
            {"driver_number": item["driver_number"], "position": item["position"], "time": item["date"], "session key": item["session_key"]}
            for item in data if item["driver_number"] == driver_number
        ]

"""
The DriverPosition class tracks the position of the drivers.
"""
class DriverPosition:
    def __init__(self):
        self.request_handler = RequestHandler("https://api.openf1.org/v1/position?session_key=latest")

    # Method to get the request handler field.
    def get_request_handler(self):
        return self.request_handler

    # Method to get the position of a driver.
    def get_driver_position(self, driver_number):
        data = self.request_handler.load_data()
        filtered_data = self.request_handler.filter_by_driver(data, driver_number)

        return filtered_data

    def list_data(self, filtered_data):
        position_list = []
        timestamp_list = []
        for item in filtered_data:
            position_list.append(item["position"])
            timestamp_list.append(item["time"])

        return position_list, timestamp_list


position = DriverPosition()
driver_position = position.list_data(position.get_driver_position(44))


y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

plt.plot(driver_position[1], driver_position[0])
plt.gca().invert_yaxis()
plt.yticks(y)
plt.grid(axis="y")
plt.show()