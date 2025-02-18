import threading

class Vehicle:
    """Class to represent a vehicle with a number and type."""
    
    def __init__(self, vehicle_number, vehicle_type):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type  # Can be "Bike", "Car", or "Truck"


class ParkingSpot:
    """Represents a single parking spot in the parking lot."""
    
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.is_occupied = False
        self.vehicle = None

    def park(self, vehicle):
        """Attempts to park a vehicle in this spot."""
        if self.is_occupied:
            return False
        self.vehicle = vehicle
        self.is_occupied = True
        return True

    def leave(self):
        """Removes the vehicle from the spot."""
        if not self.is_occupied:
            return False
        self.vehicle = None
        self.is_occupied = False
        return True


class Floor:
    """Represents a single floor in the parking lot, containing multiple parking spots."""
    
    def __init__(self, floor_number, spots_per_floor):
        self.floor_number = floor_number
        self.spots = [ParkingSpot(f"{floor_number}-{i}") for i in range(spots_per_floor)]

    def find_available_spot(self, vehicle_type):
        """Finds an available spot for a vehicle. Trucks require 2 spots."""
        spots_needed = 2 if vehicle_type == "Truck" else 1
        for i in range(len(self.spots) - spots_needed + 1):
            if all(not self.spots[j].is_occupied for j in range(i, i + spots_needed)):
                return i  # Found a valid parking space
        return None  # No available space found

    def park_vehicle(self, vehicle):
        """Attempts to park a vehicle on this floor."""
        spot_index = self.find_available_spot(vehicle.vehicle_type)
        if spot_index is None:
            return None
        spots_needed = 2 if vehicle.vehicle_type == "Truck" else 1

        for i in range(spot_index, spot_index + spots_needed):
            self.spots[i].park(vehicle)
        return spot_index

    def leave_vehicle(self, vehicle_number):
        """Removes a vehicle from this floor if found."""
        for spot in self.spots:
            if spot.is_occupied and spot.vehicle and spot.vehicle.vehicle_number == vehicle_number:
                spot.leave()

    def available_spots(self):
        """Returns the number of available spots on this floor."""
        return sum(1 for spot in self.spots if not spot.is_occupied)


class ParkingLot:
    """Manages the entire parking lot, including multiple floors and vehicles."""
    
    def __init__(self, num_floors, spots_per_floor):
        self.floors = [Floor(i, spots_per_floor) for i in range(num_floors)]
        self.vehicle_map = {}  # Stores vehicle_number → (floor, spot_index)
        self.lock = threading.Lock()  # Ensures thread safety for concurrent access

    def park_vehicle(self, vehicle_number, vehicle_type):
        """Handles the process of parking a vehicle in the lot."""
        with self.lock:
            if vehicle_number in self.vehicle_map:
                print(f"Warning: Vehicle {vehicle_number} is already parked!")
                return False  # Avoid duplicate parking
            
            vehicle = Vehicle(vehicle_number, vehicle_type)

            for floor in self.floors:
                spot_index = floor.park_vehicle(vehicle)
                if spot_index is not None:
                    self.vehicle_map[vehicle_number] = (floor.floor_number, spot_index)
                    print(f"Vehicle {vehicle_number} parked at Floor {floor.floor_number}, Spot {spot_index}")
                    return True

            print("Parking lot is full. No available spots.")
            return False

    def leave_vehicle(self, vehicle_number):
        """Removes a parked vehicle from the lot."""
        with self.lock:
            if vehicle_number not in self.vehicle_map:
                print("Vehicle not found in the parking lot.")
                return False

            floor_number, _ = self.vehicle_map[vehicle_number]
            self.floors[floor_number].leave_vehicle(vehicle_number)
            del self.vehicle_map[vehicle_number]
            print(f"Vehicle {vehicle_number} has exited the parking lot.")
            return True

    def query_parking_lot(self):
        """Displays the number of available parking spots on each floor."""
        print("\nCurrent Parking Lot Status:")
        for floor in self.floors:
            print(f"  Floor {floor.floor_number}: {floor.available_spots()} available spots")
        print("\n")

    def is_full(self):
        """Checks if the entire parking lot is full."""
        return all(floor.available_spots() == 0 for floor in self.floors)

    def find_vehicle(self, vehicle_number):
        """Finds a vehicle in the parking lot and returns its location."""
        if vehicle_number in self.vehicle_map:
            floor_number, spot_index = self.vehicle_map[vehicle_number]
            print(f"Vehicle {vehicle_number} is parked at Floor {floor_number}, Spot {spot_index}")
            return True
        print("Vehicle not found.")
        return False


# Main function
def main():
    """Main function that runs the parking lot system through a CLI."""
    
    num_floors = int(input("Enter number of floors: "))
    spots_per_floor = int(input("Enter spots per floor: "))

    parking_lot = ParkingLot(num_floors, spots_per_floor)

    while True:
        print("\n===== Parking Lot Menu =====")
        print("1. Park a vehicle")
        print("2. Remove a vehicle")
        print("3. Query available spots")
        print("4. Find vehicle location")
        print("5. Check if lot is full")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            vehicle_number = input("Enter vehicle number: ")
            vehicle_type = input("Enter vehicle type (Car/Bike/Truck): ")
            parking_lot.park_vehicle(vehicle_number, vehicle_type)
        elif choice == "2":
            vehicle_number = input("Enter vehicle number: ")
            parking_lot.leave_vehicle(vehicle_number)
        elif choice == "3":
            parking_lot.query_parking_lot()
        elif choice == "4":
            vehicle_number = input("Enter vehicle number: ")
            parking_lot.find_vehicle(vehicle_number)
        elif choice == "5":
            if parking_lot.is_full():
                print("Parking lot is FULL.")
            else:
                print("Parking lot has available spots.")
        elif choice == "6":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

# to run the program
if __name__ == "__main__":
    main()
 