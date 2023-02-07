import requests


class sonnenbatterie_v2:
    def __init__(self, ipaddress, auth_token):
        self.ipaddress = ipaddress
        self.auth_token = auth_token
        self.baseurl = 'http://' + self.ipaddress + '/api/v2/'

    def _get(self, what):
        response = requests.get(self.baseurl + what,
                                headers={'Auth-Token': self.auth_token},
                                )
        if response.status_code != 200:
            response.raise_for_status()

        return response.json()

    def get_powermeter(self):
        return self._get("powermeter")

    def get_status(self):
        return self._get("status")

    def get_battery(self):
        return self._get("battery")

    def get_inverter(self):
        return self._get("inverter")

    def get_latestdata(self):
        return self._get("latestdata")
