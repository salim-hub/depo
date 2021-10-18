import requests

# parameters = {"lat": 37.78, "lon": -122.41}

# response = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)

# # This gets the same data as the command above
# # response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")

# # print(response.status_code)

# print(response.content)

# # Get the response data as a Python object.  Verify that it's a dictionary.
# json_data = response.json()
# print(type(json_data))
# print(json_data)

# # Get the duration value of the ISS's first pass over San Francisco------------>çalışmıyor
# # first_pass_duration = json_data["response"][0]["duration"]


# Call the API here.
response = requests.get("http://api.open-notify.org/astros.json")
json_data = response.json()

in_space_count = json_data["number"]
print(in_space_count)