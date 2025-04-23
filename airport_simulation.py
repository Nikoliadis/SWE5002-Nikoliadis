import random
import time
from collections import deque

class FlightRequest:
    def __init__(self, flight_number, action_type):
        self.flight_number = flight_number
        self.action_type = action_type  # "landing", "takeoff" or "emergency"

    def __str__(self):
        return f"Flight {self.flight_number} is requesting {self.action_type}"

class AirportManager:
    def __init__(self):
        self.queue_landing = deque()
        self.queue_takeoff = deque()
        self.queue_emergency = deque()

    def register_request(self, request: FlightRequest):
        if request.action_type == "emergency":
            self.queue_emergency.appendleft(request)
        elif request.action_type == "landing":
            self.queue_landing.append(request)
        elif request.action_type == "takeoff":
            self.queue_takeoff.append(request)
        print(request)

    def handle_next_action(self):
        if self.queue_emergency:
            current = self.queue_emergency.popleft()
            print(f"CONTROL: {current.flight_number} is cleared for **EMERGENCY LANDING**")
        elif self.queue_landing:
            current = self.queue_landing.popleft()
            print(f"CONTROL: {current.flight_number} is cleared to land")
        elif self.queue_takeoff:
            current = self.queue_takeoff.popleft()
            print(f"CONTROL: {current.flight_number} is cleared for takeoff")

    def has_pending_requests(self):
        return any([self.queue_emergency, self.queue_landing, self.queue_takeoff])

def run_simulation():
    airport = AirportManager()
    next_flight_id = 200

    for _ in range(15):
        request_kind = random.choices(
            ["landing", "takeoff", "emergency"],
            weights=[0.4, 0.4, 0.2],
            k=1
        )[0]
        request = FlightRequest(next_flight_id, request_kind)
        airport.register_request(request)
        next_flight_id += 1
        time.sleep(0.2)

        airport.handle_next_action()

    while airport.has_pending_requests():
        time.sleep(0.2)
        airport.handle_next_action()

if __name__ == "__main__":
    run_simulation()
