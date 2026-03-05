# ALOHA Protocol Comparison

This project compares the performance of **Pure ALOHA** and **Slotted ALOHA** by analyzing how their throughput changes as the offered load increases.

Both protocols are simulated and compared against their theoretical throughput models.

---

# Background

ALOHA protocols are random access methods that allow multiple nodes to share a communication channel.

When two or more nodes transmit at the same time, a **collision** occurs and the transmitted packets are lost.

Two main versions exist:

**Pure ALOHA**

Nodes transmit whenever they have data to send.

**Slotted ALOHA**

Time is divided into fixed slots and nodes may only begin transmission at the start of a slot.

This synchronization significantly reduces collisions.

---

# Throughput Models

The throughput of the two protocols is given by the following theoretical models.

## Pure ALOHA

Because packets can start at any time, the vulnerable period is **2T**.

The throughput is:

$$
S = G e^{-2G}
$$

The maximum throughput occurs when:

$$
G = 0.5
$$

Maximum efficiency:

$$
S_{max} \approx 0.184
$$

---

## Slotted ALOHA

Because transmissions are synchronized into slots, the vulnerable period becomes **T**.

The throughput is:

$$
S = G e^{-G}
$$

The maximum throughput occurs when:

$$
G = 1
$$

Maximum efficiency:

$$
S_{max} \approx 0.368
$$

---

# Results

The figure below compares the simulated throughput of both protocols with their theoretical models.

<img width="1260" height="949" alt="image" src="https://github.com/user-attachments/assets/d8e90b09-7f92-45e9-9fe1-41a10f4adb61" />


Key observations from the comparison:

- **Slotted ALOHA achieves nearly double the maximum throughput of Pure ALOHA**
- The maximum throughput of Pure ALOHA occurs near **G ≈ 0.5** with efficiency ≈ **18.4%**
- The maximum throughput of Slotted ALOHA occurs near **G ≈ 1.0** with efficiency ≈ **36.8%**
- Synchronizing transmissions into time slots reduces the vulnerable period from **2T to T**
- As the offered load increases, collisions dominate and throughput decreases in both protocols

This comparison highlights the advantage of **time-slot synchronization in random access protocols**, which significantly reduces collisions and improves channel efficiency.

