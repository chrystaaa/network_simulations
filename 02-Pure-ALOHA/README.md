# Pure ALOHA Simulation

This project implements a Python-based simulation of the **Pure ALOHA** Medium Access Control (MAC) protocol to analyze the relationship between **network load** and **throughput**.

The objective is to experimentally validate the theoretical Poisson model using simulation results.

---

# Background

Pure ALOHA is a random access protocol in which nodes transmit **whenever they have data to send**, without waiting for time slots.

Because transmissions can begin at **any moment**, packets may overlap in time and cause collisions.

Each transmission attempt can result in:

• **Success** → No other packet overlaps  
• **Collision** → Two or more packets overlap  

A packet transmission will fail if another node begins transmitting within the **vulnerable period**.

---

# Offered Load Model

The offered load is defined as:

$$
G = Np
$$

where:

- **N** = number of nodes  
- **p** = transmission probability per node  
- **G** = average number of attempted transmissions per packet time  

The probability that exactly **k** nodes transmit is modeled using the **Poisson distribution**:

$$
P(k) = \frac{G^k e^{-G}}{k!}
$$

---

# Maximum Throughput

For the network to successfully deliver a packet, **exactly one node must transmit** $(k = 1)$.

- If $k = 0$ → The channel is **Idle**
- If $k > 1$ → A **Collision** occurs

However, in **Pure ALOHA**, collisions can occur if another transmission starts **before or after** the packet within the vulnerable period.

The vulnerable period is:

$$
2T
$$

Therefore, the throughput becomes:

$$
S = G e^{-2G}
$$

---

# Key Result

The maximum throughput occurs when:

$$
G = 0.5
$$

At this point:

$$
S = \frac{1}{2e} \approx 0.184
$$

This means **Pure ALOHA can only utilize about 18.4% of the channel capacity**.

---

# Simulation Model

The simulation:

- Uses **N = 30 nodes**
- Sweeps multiple offered load values **G**
- Runs for **20,000 time slots per experiment**

The simulation measures:

1. Throughput  
2. Collision rate  
3. Idle rate  

---

# Results

The figure below compares the **simulated throughput** with the **theoretical throughput** of Pure ALOHA.

<img width="1266" height="957" alt="image" src="https://github.com/user-attachments/assets/e3145a80-3510-4756-b36a-34f16c6cd2de" />

The simulation closely follows the theoretical model:

- Throughput follows the theoretical curve **$S = G e^{-2G}$**
- The maximum throughput occurs near **$G \approx 0.5$**
- The maximum channel efficiency is approximately **18.4%**
- As the offered load increases, collisions become more frequent and throughput decreases

This behavior illustrates the fundamental limitation of **Pure ALOHA**, where transmissions can begin at any time and therefore experience a larger **vulnerable period**, leading to more collisions compared to **Slotted ALOHA**.

---
