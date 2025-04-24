# Airport Simulation

This project simulates the air traffic control system of a small airport using Python.  
It handles landing, takeoff, and emergency landing requests from flights and processes them based on priority.

## Features

- Separate queues for:
  - Regular landings (FIFO)
  - Takeoffs (FIFO)
  - Emergency landings (highest priority)
- Random generation of flight requests
- Real-time simulation with print outputs that reflect the control tower decisions

## Technologies Used

- `collections.deque` for queue implementation
- `random` and `time` modules for simulation purposes

## How to Run

1. Open terminal or command prompt.
2. Navigate to the project directory.
3. Run the script:

```bash
python airport_simulation.py
