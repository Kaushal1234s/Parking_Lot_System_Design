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
- Key Methods:
       - park_vehicle(vehicle_number, vehicle_type): Assigns a vehicle to an available spot.
       - leave_vehicle(vehicle_number): Removes a vehicle from the parking lot.
       - query_parking_lot(): Checks the current parking status.
       - is_full(): Determines if the parking lot is full.
       - find_vehicle(vehicle_number): Locates a parked vehicle.
