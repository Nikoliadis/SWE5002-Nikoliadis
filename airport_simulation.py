import random
import time
from collections import deque

class FlightRequest:
    def __init__(self, flight_number, action_type, emergency_reason=None):
        self.flight_number = flight_number
        self.action_type = action_type  # "landing", "takeoff", or "emergency"
        self.emergency_reason = emergency_reason

    def __str__(self):
        if self.emergency_reason:
            return f"Flight {self.flight_number} requests {self.action_type} (EMERGENCY: {self.emergency_reason})"
        return f"Flight {self.flight_number} is requesting {self.action_type}"

class AirportManager:
    def __init__(self, airport_name):
        self.airport_name = airport_name
        self.queue_landing = deque()
        self.queue_takeoff = deque()
        self.queue_emergency = deque()

        # Stats
        self.landing_count = 0
        self.takeoff_count = 0
        self.emergency_count = 0

    def register_request(self, request: FlightRequest):
        if request.emergency_reason:
            self.queue_emergency.appendleft(request)
        elif request.action_type == "landing":
            self.queue_landing.append(request)
        elif request.action_type == "takeoff":
            self.queue_takeoff.append(request)
        print(request)

    def handle_next_action(self):
        if self.queue_emergency:
            current = self.queue_emergency.popleft()
            print(f"CONTROL: {current.flight_number} is cleared for EMERGENCY LANDING due to: {current.emergency_reason}")
            self.emergency_count += 1
        elif self.queue_landing:
            current = self.queue_landing.popleft()
            print(f"CONTROL: {current.flight_number} is cleared to land")
            self.landing_count += 1
        elif self.queue_takeoff:
            current = self.queue_takeoff.popleft()
            print(f"CONTROL: {current.flight_number} is cleared for takeoff")
            self.takeoff_count += 1

    def has_pending_requests(self):
        return any([self.queue_emergency, self.queue_landing, self.queue_takeoff])

    def print_summary(self):
        print("\n--- Simulation Summary ---")
        print(f"🛬 Normal landings: {self.landing_count}")
        print(f"⚠️ Emergency landings: {self.emergency_count}")
        print(f"🛫 Takeoffs: {self.takeoff_count}")
        print("--------------------------")

def run_simulation():
    airport = AirportManager("Athens International Airport")
    print(f"--- {airport.airport_name} Simulation Started ---\n")
    next_flight_id = 200

    for _ in range(15):
        request_kind = random.choices(
            ["landing", "takeoff", "landing_with_issue"],
            weights=[0.4, 0.4, 0.2],
            k=1
        )[0]

        emergency_reason = None
        if request_kind == "landing_with_issue":
            emergency_reason = random.choice(["low fuel", "technical malfunction"])
            action_type = "emergency"
        else:
            action_type = request_kind

        request = FlightRequest(next_flight_id, action_type, emergency_reason)
        airport.register_request(request)
        next_flight_id += 1
        time.sleep(0.2)

        airport.handle_next_action()

    while airport.has_pending_requests():
        time.sleep(0.2)
        airport.handle_next_action()

    airport.print_summary()

if __name__ == "__main__":
    run_simulation()
