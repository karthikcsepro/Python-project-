import matplotlib.pyplot as plt
from covid import Covid

covid = Covid(source="worldometers")

countries = []
confirmed = []
active = []
recovered = []
deaths = []

print("Enter country names separated by comma")
print("Example: India, USA, UK")

user_input = input("Enter Countries Name: ")

countries = [c.strip().title() for c in user_input.split(",")]

for country in countries:
    try:
        data = covid.get_status_by_country_name(country)

        confirmed.append(data["confirmed"] / 1_000_000)
        active.append(data["active"] / 1_000_000)
        recovered.append(data["recovered"] / 1_000_000)
        deaths.append(data["deaths"] / 1_000_000)

    except:
        print("Data not available for", country)

plt.figure(figsize=(10, 6))

plt.bar(countries, recovered, label="Recovered")
plt.bar(countries, active, bottom=recovered, label="Active")
plt.bar(
    countries,
    deaths,
    bottom=[recovered[i] + active[i] for i in range(len(countries))],
    label="Deaths"
)

plt.xlabel("Country Name")
plt.ylabel("Cases in Millions")
plt.title("COVID-19 Statistics")
plt.xticks(rotation=30)
plt.legend()
plt.tight_layout()
plt.show()
