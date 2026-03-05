import random
import math
import matplotlib.pyplot as plt

def simulate_pure_aloha(G: float, total_time: float = 20000.0, seed: int = 1) -> float:
    rng = random.Random(seed)

    if G <= 0:
        return 0.0

    t = 0.0
    arrivals = []
    while t < total_time:
        u = rng.random()
        dt = -math.log(1.0 - u) / G 
        t += dt
        if t < total_time:
            arrivals.append(t)

    n = len(arrivals)
    if n == 0:
        return 0.0

    successes = 0

    for i in range(n):
        left_ok = True
        right_ok = True
        if i > 0:
            left_ok = (arrivals[i] - arrivals[i - 1]) >= 1.0
        if i < n - 1:
            right_ok = (arrivals[i + 1] - arrivals[i]) >= 1.0
        if left_ok and right_ok:
            successes += 1

    return successes / total_time  


def theo_pure(G: float) -> float:
    return G * math.exp(-2.0 * G)


def simulate_slotted_aloha(num_nodes: int, p: float, slots: int = 20000, seed: int = 1) -> float:
    random.seed(seed)
    success = 0

    for _ in range(slots):
        tx = 0
        for _ in range(num_nodes):
            if random.random() < p:
                tx += 1
        if tx == 1:
            success += 1

    return success / slots


def theo_slotted(G: float) -> float:
    return G * math.exp(-G)


if __name__ == "__main__":
    seed = 1

    N = 30
    slots = 20000


    total_time = 20000.0


    G_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0]

    pure_sim = []
    slotted_sim = []
    pure_th = []
    slotted_th = []

    print("\nALOHA Comparison")
    print("G\tPure(sim)\tPure(th)\tSlotted(sim)\tSlotted(th)")

    for G in G_values:
      
        s_pure = simulate_pure_aloha(G=G, total_time=total_time, seed=seed)
     
        p = G / N
        s_slot = simulate_slotted_aloha(num_nodes=N, p=p, slots=slots, seed=seed)

        pure_sim.append(s_pure)
        slotted_sim.append(s_slot)
        pure_th.append(theo_pure(G))
        slotted_th.append(theo_slotted(G))

        print(f"{G:.2f}\t{ s_pure:.4f}\t\t{theo_pure(G):.4f}\t\t{s_slot:.4f}\t\t{theo_slotted(G):.4f}")


    plt.figure()
    plt.plot(G_values, pure_sim, "o-", label="Pure ALOHA (Simulation)")
    plt.plot(G_values, pure_th, "--", label=r"Pure ALOHA (Theory: $Ge^{-2G}$)")
    plt.plot(G_values, slotted_sim, "s-", label="Slotted ALOHA (Simulation)")
    plt.plot(G_values, slotted_th, ":", label=r"Slotted ALOHA (Theory: $Ge^{-G}$)")
    plt.xlabel("Offered Load G")
    plt.ylabel("Throughput S")
    plt.title("Pure ALOHA vs Slotted ALOHA: Simulation vs Theory")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

 
