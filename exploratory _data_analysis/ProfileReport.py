import pandas as pd
from pandas_profiling import ProfileReport

lunarData = pd.read_csv('LunarEclipse.csv')
solarData = pd.read_csv('SolarEclipse.csv')

lunarProfile = ProfileReport(lunarData)
solarProfile = ProfileReport(solarData)

lunarProfile.to_file(output_file = 'LunarEclipse.html')
solarProfile.to_file(output_file = 'SolarEclipse.html')