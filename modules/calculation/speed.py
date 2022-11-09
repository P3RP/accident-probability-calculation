from geopy import distance


class SpeedCalc:
    prev = None

    def calc(self, lat, lng, timestamp):
        if not self.prev:
            speed = 0.0
        else:
            dis = distance.distance((self.prev[0], self.prev[1]), (lat, lng)).kilometers * (1000 * 60 * 60)
            hour = timestamp - self.prev[2]
            speed = dis / hour
        self.prev = (lat, lng, timestamp)
        return speed
