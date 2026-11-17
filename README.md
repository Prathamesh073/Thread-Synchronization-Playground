
# Thread Synchronization Playground

An Interactive Operating Systems Simulator built using Python and Streamlit.

## About the Project

This project demonstrates how multiple threads access shared data and resources, what problems occur during concurrent execution, and how synchronization mechanisms help manage them safely.

## Features

### 1. Race Condition vs Mutex
- Demonstrates race conditions using a shared counter.
- Compares execution with and without Mutex Lock.
- Displays expected counter, actual counter and lost updates.

### 2. Semaphore Playground
- Demonstrates semaphore-based resource management.
- Controls simultaneous access to shared resources.
- Displays peak active users and execution information.

### 3. Producer-Consumer Problem
- Demonstrates communication using a shared buffer.
- Uses Mutex and Semaphores.
- Displays produced items, consumed items and buffer status.

## Technologies Used
- Python
- Streamlit
- Threading
- Mutex Lock
- Semaphore
- Pandas
- Plotly

## Installation

Clone the repository:

```bash
git clone https://github.com/Prathamesh073/Thread-Synchronization-Playground.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Project Objective

To provide a practical understanding of thread synchronization concepts in Operating Systems.

## Developed By

Prathamesh Dhole

For educational purposes.
