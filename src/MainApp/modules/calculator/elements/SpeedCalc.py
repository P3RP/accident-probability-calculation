from geopy import distance

from .base import BaseCalc


class SpeedCalc(BaseCalc):
    prev_coord = None
    prev_speed = 0.0

    def calc(self, **kwargs):
        lat = kwargs['lat']
        lng = kwargs['lng']
        timestamp = kwargs['timestamp']

        if not self.prev_coord:
            speed = 0.0
        else:
            dis = distance.distance((self.prev_coord[0], self.prev_coord[1]), (lat, lng)).kilometers * (1000 * 60 * 60)
            hour = timestamp - self.prev_coord[2]
            speed = dis / hour

        chg = speed - self.prev_speed
        if chg > 40:
            prob = 20.0
        else:
            prob = 0.0

        self.prev_coord = (lat, lng, timestamp)
        self.prev_speed = speed
        return {
            'prob': prob,
            'info': {
                'speed': speed,
                'chg': chg
            }
        }
