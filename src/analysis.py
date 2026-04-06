import numpy as np

def confidence_interval(series, confidence=0.95):
    mean = np.mean(series)
    std = np.std(series, ddof=1)
    n = len(series)

    z = 1.96
    margin = z * (std / np.sqrt(n))

    return {
        "mean": mean,
        "lower": mean - margin,
        "upper": mean + margin,
        "margin": margin,
        "n": n
    }
