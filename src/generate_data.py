import pandas as pd
import numpy as np
import random

def generate_dummy_data(n=300, seed=42):
    np.random.seed(seed)
    random.seed(seed)

    locations = ["Jakarta", "Bandung", "Surabaya", "Medan", "Yogyakarta"]
    brands = ["Samsung", "Apple", "Xiaomi", "Oppo", "Vivo"]
    interests = ["Low", "Medium", "High"]
    location_types = ["Mall", "Office", "Cafe", "Campus"]

    df = pd.DataFrame({
        "Nama Lokasi": np.random.choice(locations, n),
        "Jam Login": np.random.randint(0, 24, n),
        "Nama": [f"User_{i}" for i in range(n)],
        "Email": [f"user{i}@gmail.com" for i in range(n)],
        "No Telepon": ["08" + ''.join([str(random.randint(0,9)) for _ in range(10)]) for _ in range(n)],
        "Tahun Lahir": np.random.randint(1980, 2005, n),
        "Merk HP": np.random.choice(brands, n),
        "Minat Digital": np.random.choice(interests, n, p=[0.3,0.4,0.3]),
        "Tipe Lokasi": np.random.choice(location_types, n)
    })

    # Feature Engineering
    df["Umur"] = 2026 - df["Tahun Lahir"]

    df["Kategori Umur"] = df["Umur"].apply(lambda x:
        "Gen Z" if x < 25 else
        "Young Adult" if x <= 35 else
        "Adult" if x <= 45 else
        "Senior"
    )

    df["Kategori Waktu Login"] = df["Jam Login"].apply(lambda x:
        "Dini Hari" if x <= 6 else
        "Pagi" if x <= 11 else
        "Siang" if x <= 17 else
        "Malam"
    )

    mapping = {"Low":1, "Medium":2, "High":3}
    df["Skor Minat Digital"] = df["Minat Digital"].map(mapping)

    df["Potensi Customer"] = df.apply(lambda row:
        "High" if row["Skor Minat Digital"] == 3 and 25 <= row["Umur"] <= 40
        else "Medium" if row["Skor Minat Digital"] == 2
        else "Low", axis=1
    )

    return df
