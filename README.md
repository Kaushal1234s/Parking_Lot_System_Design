
# 🚗 Parking Lot Management System

## 📌 Overview
A simple and efficient **Parking Lot Management System** that allows vehicles to park, exit, and check availability in a multi-floor parking lot.  
It supports different vehicle types and ensures **concurrency safety** using threading.

---

## 📋 System Requirements

### ✅ Functional Requirements
1. **Vehicle Parking**  
   - Vehicles can enter and park in the nearest available spot.  
   - **Truck** requires **two adjacent spots**, while **Bikes** and **Cars** need **one spot** each.

2. **Vehicle Exit**  
   - The system allows vehicles to leave, freeing up their occupied spot(s).

3. **Availability Check**  
   - Users can check the number of **available spots** on each floor.

4. **Find Vehicle Location**  
   - Users can locate a **parked vehicle** by its vehicle number.

5. **Full Parking Lot Check**  
   - The system should indicate whether the parking lot is **full**.

6. **Thread Safety (Concurrency Handling)**  
   - Multiple users can interact with the system **simultaneously** without conflicts.

---

### ⚡ Non-Functional Requirements
1. **Scalability** → Supports multiple floors and a large number of vehicles.  
2. **Performance** → Efficient spot allocation and retrieval operations.  
3. **Maintainability** → Modular and extendable design for future enhancements.  
4. **User-Friendly Interface** → Simple and intuitive command-line interface (CLI).  
5. **Security & Access Control** → Prevents duplicate parking of the same vehicle.  

---

## 🚀 Class Diagram Explanation for Parking Lot System

1. **ParkingLot**:
   - The main class managing the entire parking lot.
   - Stores a list of floors and a vehicle map to track parked vehicles.
   - Uses threading lock for concurrency safety.
   - **Key Methods**:
     - `park_vehicle(vehicle_number, vehicle_type)`: Assigns a vehicle to an available spot.
     - `leave_vehicle(vehicle_number)`: Removes a vehicle from the parking lot.
     - `query_parking_lot()`: Checks the current parking status.
     - `is_full()`: Determines if the parking lot is full.
     - `find_vehicle(vehicle_number)`: Locates a parked vehicle.

2. **Floor**:
   - Represents a parking floor in the parking lot.
   - Contains a list of **parking spots** available on the floor.
   - **Key Methods**:
     - `find_available_spot(vehicle_type)`: Finds a suitable spot for the given vehicle type.
     - `park_vehicle(vehicle)`: Assigns a vehicle to an available spot.
     - `leave_vehicle(vehicle_number)`: Frees a spot when a vehicle leaves.
     - `available_spots()`: Returns the count of free spots on the floor.

3. **ParkingSpot**:
   - Represents an individual parking spot.
   - Holds information about its status (occupied or free) and the vehicle parked in it.
   - **Key Methods**:
     - `park(vehicle)`: Parks a vehicle in this spot.
     - `leave()`: Frees the parking spot when a vehicle exits.

4. **Vehicle**:
   - Represents a vehicle that will be parked.
   - Stores the **vehicle number** and **vehicle type**.
   - Types of vehicles include:
     - `Bike`
     - `Car`
     - `Truck`

5. **VehicleType (Enumeration)**:
   - Defines different types of vehicles that can be parked.
   - Supported types:
     - `Bike`
     - `Car`
     - `Truck`

6. **Main**:
   - Entry point of the application.
   - **Key Method**:
     - `main()`: Initializes the parking lot system and handles user interactions.

![Screenshot 2025-02-18 220126](https://github.com/user-attachments/assets/f3f62e24-194a-4e4d-ac11-2f31fe317237)

## Working of Code Below
<img width="958" alt="screenshot1" src="https://github.com/user-attachments/assets/af390b9e-3d57-43ec-87b1-b5f4408dbc30" />
<img width="959" alt="screenshot2" src="https://github.com/user-attachments/assets/29fa955d-e332-4c58-8eb5-0f013296ebf1" />


