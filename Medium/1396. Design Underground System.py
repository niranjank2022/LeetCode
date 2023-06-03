from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.table = defaultdict(dict)
        self.checkin_data = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_data[id] = stationName, t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        final_data = self.checkin_data[id]
        values = self.table[final_data[0]].get(stationName, (0, 0))
        self.table[final_data[0]][stationName] = (values[0] + t - final_data[1], values[1] + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.table[startStation][endStation][0] / self.table[startStation][endStation][1]
