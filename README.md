# One-to-One Secure Chat Application (Python)

## 📌 Overview
This project is a **one-to-one chat application** built using **Python socket programming** with a **client–server architecture**.  
It enables **real-time communication** between two users, where each client runs independently and connects to a central server for message routing.

The project focuses on demonstrating **core backend engineering fundamentals** such as networking, concurrency, stateful connection handling, and system design.

---

## 🏗️ System Architecture

Client A ──►
Server ──► Client B
Client A ◄── ◄── Client B


- Each user runs a separate client process
- The server manages active client connections
- Messages are routed through the server using TCP sockets

---

## 🔑 Key Features
- One-to-one real-time messaging
- Client–server based communication model
- Concurrent handling of multiple clients using multithreading
- Username-based message routing
- Graceful handling of client disconnections
- Modular design preparing the system for secure communication

---

## 🛠️ Technologies Used
- Python 3
- TCP Socket Programming
- Multithreading
- Command Line Interface (CLI)

---

## 📂 Project Structure

one-on-one-chat-application/
│
├── server.py # Server-side connection and routing logic
├── client.py # Client-side messaging logic
└── README.md


---

## ⚙️ How the Application Works
1. The server starts and listens for incoming client connections.
2. Each client connects to the server and registers with a unique username.
3. The server maintains a mapping of active users and their socket connections.
4. Messages sent by a client are forwarded only to the intended recipient.
5. The recipient receives and displays the message in real time.

---

## ▶️ How to Run the Application

### Step 1: Start the Server
```bash
python server.py

Server started. Waiting for clients...
