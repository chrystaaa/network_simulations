#  Slotted ALOHA Simulation

This project implements a Python-based simulation of the **Slotted ALOHA** Medium Access Control (MAC) protocol to analyze the relationship between network load and throughput.

The objective is to experimentally validate the theoretical Poisson model using simulation results.

---

##  Background

Slotted ALOHA is a random access protocol in which time is divided into discrete slots.  

In each slot, every node independently attempts transmission with probability $p$.

Each slot can result in:

- **Idle** → No nodes transmit  
- **Success** → Exactly one node transmits  
- **Collision** → More than one node transmits  

Throughput is defined as the fraction of slots that result in a successful transmission.

---

##  Theoretical Analysis: The Poisson Model

For a large number of nodes $N$, the number of transmission attempts per slot can be approximated using a **Poisson distribution**.

The offered load is defined as:

$$
G = Np
$$

where:
- $N$ = number of nodes  
- $p$ = transmission probability per node  
- $G$ = average number of attempted transmissions per slot  

The probability that exactly $k$ nodes transmit in a slot is:

$$
P(k) = \frac{G^k e^{-G}}{k!}
$$

---

##  Maximum Throughput

For the network to successfully deliver a packet, exactly **one** node must transmit ($k = 1$).

- If $k = 0$: The slot is **Idle**
- If $k > 1$: A **Collision** occurs

Therefore, throughput is:

$$
S = P(1) = \frac{G^1 e^{-G}}{1!} = G e^{-G}
$$

To determine the maximum throughput, we compute:

$$
\frac{dS}{dG} = 0
$$

Solving this gives:

$$
G = 1
$$

At this operating point:

$$
S_{\max} = e^{-1} \approx 0.368
$$

Thus, the maximum theoretical efficiency of Slotted ALOHA is **36.8%**.

---

##  Simulation Method

The simulation:

- Uses $N = 30$ nodes  
- Sweeps multiple transmission probabilities $p$  
- Runs for 20,000 time slots per experiment  
- Measures:
  - Throughput
  - Collision rate
  - Idle rate  

Each slot counts how many nodes attempt transmission and classifies the outcome accordingly.

---

##  Simulation Results

The simulation closely matches the theoretical curve:

- **Peak Efficiency:** ≈ 36.8% at $G \approx 1$
- **Under-utilization:** When $G < 1$, many slots remain idle
- **Congestion Collapse:** When $G > 1$, collisions dominate and throughput decreases

The close alignment between simulation and theory validates both the implementation and the Poisson approximation.

---

##  Throughput: Simulation vs Theory

The plot below compares simulated throughput against the theoretical curve $S = G e^{-G}$:

---

<img width="1251" height="942" alt="image" src="https://github.com/user-attachments/assets/9d938be0-27a0-4fd3-9ad6-11fa332d4796" />


##  Future Improvements

Possible extensions:

- Implement Pure ALOHA ($S = G e^{-2G}$)
- Add exponential backoff
- Compare with CSMA or CDMA
- Increase $N$ to observe stronger Poisson convergence

---

##  Key Takeaways

- Slotted ALOHA has a strict theoretical efficiency limit of 36.8%
- Maximum performance occurs at $G = 1$
- Increasing load beyond this point reduces throughput due to collisions
- Simulation experimentally confirms the Poisson-based theoretical model
