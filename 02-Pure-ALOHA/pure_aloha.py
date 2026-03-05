import random
import math
import matplotlib.pyplot as plt


def simulate_pure_aloha(
        G: float, 
        total_time: float = 20000.0, 
        seed: int = 1):
    rng = random.Random(seed)

    if G <= 0:
        return {"throughput": 0.0, "attempt_rate": 0.0}

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
        return {"throughput": 0.0, "attempt_rate": 0.0}

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

    throughput = successes / total_time
    attempt_rate = n / total_time
    return {"throughput": throughput, "attempt_rate": attempt_rate}


def theo_throughput(G: float) -> float:
    return G * math.exp(-2.0 * G)


if __name__ == "__main__":
    seed = 1
    total_time = 20000.0

    G_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0]

    print("\nPure ALOHA Sweep")
    print("G\tS(sim)\t\tS(theory)\tattempt_rate(sim)")

    sim_S = []
    th_S = []
    sim_attempt = []

    for G in G_values:
        stats = simulate_pure_aloha(G=G, total_time=total_time, seed=seed)
        s_sim = stats["throughput"]
        s_th = theo_throughput(G)

        sim_S.append(s_sim)
        th_S.append(s_th)
        sim_attempt.append(stats["attempt_rate"])

        print(f"{G:.2f}\t{s_sim:.4f}\t\t{s_th:.4f}\t\t{stats['attempt_rate']:.4f}")

    plt.figure()
    plt.plot(G_values, sim_S, "o-", label="Simulation")
    plt.plot(G_values, th_S, "--", label=r"Theory ($Ge^{-2G}$)")
    plt.xlabel("Offered Load G")
    plt.ylabel("Throughput S")
    plt.title("Pure ALOHA Throughput: Simulation vs Theory")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
