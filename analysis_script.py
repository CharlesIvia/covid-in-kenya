# Import required libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read-in data into a dataframe
df = pd.read_csv("covid_data.csv")
print(df)

# Overview of the data
columns = df.columns
print(columns)

df_info = df.info()
print(columns)

# From 'df.info()', we notice that vaccinations and total_population variables are strings and not integers

# Data cleaning
# Remove the comma and convert total_population and vaccinations columns into integers

df["vaccinations(2 doses)"] = (
    df["vaccinations(2 doses)"].str.replace(",", "").astype(int)
)
df["total_population(millions)"] = (
    df["total_population(millions)"].str.replace(",", "").astype(int)
)

# Run df.info() again to confirm
df_info = df.info()
print(columns)

# Get a summary of the data

summary = df.describe()
print(summary)

# Sort dataframe by total cases
df.sort_values(by="total_cases", ascending=False, ignore_index=True, inplace=True)
print(df)

# Correlation between covid-19 cases and population density
cases_pop_density_corr = df["total_cases"].corr(df["population_density"])
print(f"Cases v Population density correlation {cases_pop_density_corr}")

# Visualize above correlation using a scatterplot
plt.figure(figsize=(8, 4.21), dpi=100)
plt.title("Total Cases v Populatin Density", pad=20, loc="left")
sns.scatterplot(data=df, y="total_cases", x="population_density")
plt.show()

# From the visualization Nairobi and Mombasa are outliers
# Next, remove Nairobi and Mombasa and compute correlation again

df_without_nrb_and_mbs = df[2:]
cases_pop_density_without_nrb_and_mbs_corr = df_without_nrb_and_mbs["total_cases"].corr(
    df_without_nrb_and_mbs["population_density"]
)
print(
    f"Cases v Pop Density without outliers {cases_pop_density_without_nrb_and_mbs_corr}"
)

# Visualize above correlation using a scatterplot

plt.figure(figsize=(8, 4.21), dpi=100)
plt.title("Total Cases v Population Density", pad=20, loc="left")
sns.scatterplot(data=df_without_nrb_and_mbs, y="total_cases", x="population_density")
plt.show()


# Correlation between Vaccinations and Total Covid-19 cases

cases_vaccination_corr = df["total_cases"].corr(df["vaccinations(2 doses)"])
print(f"Vaccinations v Total cases corr {cases_vaccination_corr}")

# Visualize the data
plt.figure(figsize=(8, 4.21), dpi=100)
plt.title("Vaccinations v Total Cases", pad=20, loc="left")
sns.scatterplot(data=df, y="vaccinations(2 doses)", x="total_cases")
plt.show()

# Nairobi is an outlier
# Next, remove Nairobi and compute the correlation

df_without_nrb = df[1:]
cases_vaccination_corr_without_nrb = df_without_nrb["total_cases"].corr(
    df_without_nrb["vaccinations(2 doses)"]
)

print(f"Vaccinations v Total cases without nrb {cases_vaccination_corr_without_nrb}")

# Visualize above data
plt.figure(figsize=(8, 4.21), dpi=100)
plt.title("Vaccinations v Total Cases", pad=20, loc="left")
sns.scatterplot(data=df_without_nrb, y="vaccinations(2 doses)", x="total_cases")
plt.show()


# Next, determine what percentage of the total cases nairobi makes up
total_cases = df["total_cases"].sum()
nairobi_cases = df["total_cases"][0]

nairobi_cases_pc = nairobi_cases / total_cases * 100
print(f"Nairobi percentage {nairobi_cases_pc}")

# Next, determine what percentage of total cases the top 10 counties make up
top_10_total_cases = df["total_cases"][:9].sum()
top_10_total_cases_pc = top_10_total_cases / total_cases * 100
print(f"Top 10 counties percentage {top_10_total_cases_pc}")
