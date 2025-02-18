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
5. **Data Persistence (Optional)** → Can be extended to store parking records in a database.  
6. **Security & Access Control** → Prevents duplicate parking of the same vehicle.  

---

## 🚀 Getting Started

### 🔧 Installation & Setup
1. **Clone this repository**:
   ```sh
   git clone https://github.com/your-repo/parking-lot-system.git
   cd parking-lot-system
