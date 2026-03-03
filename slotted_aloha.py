import random
import math
import matplotlib.pyplot as plt


def simulate_slotted_aloha(num_nodes: int, p: float, slots: int = 10000, seed: int = 1):
    random.seed(seed)

    success = 0
    collision = 0
    idle = 0

    for _ in range(slots):
        tx = 0
        for _ in range(num_nodes):
            if random.random() < p:
                tx += 1

        if tx == 0:
            idle += 1
        elif tx == 1:
            success += 1
        else:
            collision += 1

    return {
        "throughput": success / slots,
        "collision_rate": collision / slots,
        "idle_rate": idle / slots,
    }


def theo_throughput(G: float) -> float:
    return G * math.exp(-G)


def theo_idle(G: float) -> float:
    return math.exp(-G)


def theo_collision(G: float) -> float:
    return 1.0 - math.exp(-G) - G * math.exp(-G)


if __name__ == "__main__":
    slots = 20000
    seed = 1
    N = 30
    p_values = [0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.05, 0.06, 0.08, 0.10]

    print("\nSweep for N=30")
    print("p\tG=Np\tthroughput\tcollision\tidle")

    results = []
    for p in p_values:
        stats = simulate_slotted_aloha(num_nodes=N, p=p, slots=slots, seed=seed)
        G = N * p
        results.append((p, G, stats["throughput"], stats["collision_rate"], stats["idle_rate"]))
        print(f"{p:.3f}\t{G:.3f}\t{stats['throughput']:.4f}\t\t{stats['collision_rate']:.4f}\t\t{stats['idle_rate']:.4f}")

    G_values = [r[1] for r in results]
    sim_S = [r[2] for r in results]
    sim_C = [r[3] for r in results]
    sim_I = [r[4] for r in results]

    th_S = [theo_throughput(G) for G in G_values]
    th_C = [theo_collision(G) for G in G_values]
    th_I = [theo_idle(G) for G in G_values]

    # Plot 1: Throughput
    plt.figure()
    plt.plot(G_values, sim_S, "o-", label="Simulation")
    plt.plot(G_values, th_S, "--", label=r"Theory ($Ge^{-G}$)")
    plt.xlabel("Offered Load G")
    plt.ylabel("Throughput S")
    plt.title("Slotted ALOHA Throughput")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot 2: Idle & Collision
    plt.figure()
    plt.plot(G_values, sim_I, "o-", label="Idle (Simulation)")
    plt.plot(G_values, th_I, "--", label="Idle (Theory)")
    plt.plot(G_values, sim_C, "s-", label="Collision (Simulation)")
    plt.plot(G_values, th_C, ":", label="Collision (Theory)")
    plt.xlabel("Offered Load G")
    plt.ylabel("Probability")
    plt.title("Idle and Collision Probability")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
