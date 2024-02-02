import pandas as pd

companies_df = pd.read_csv("solar_energy_companies.csv")

phone = companies_df.loc[0, "phoneNumber"]

characters_to_remove = ["+55", " ", "-"]

for character in characters_to_remove:
    phone = phone.replace(character, "")

link = "wa.me/" + phone

print(link)