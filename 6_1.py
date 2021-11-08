import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        while True:
            print(TrafficLight.__color[0])
            time.sleep(7)
            print(TrafficLight.__color[1])
            time.sleep(2)
            print(TrafficLight.__color[2])
            time.sleep(7)
            print(TrafficLight.__color[1])
            time.sleep(2)


traffic_light = TrafficLight()
traffic_light.running()
