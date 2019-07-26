import graduates
import numpy as np
import matplotlib.pyplot as plt

list_of_grad_major = graduates.get_majors()

wanted = ["Chemical Engineering", "Mechanical Engineering", "Electrical Engineering", "Civil Engineering", "Other Engineering", "Computer Science and Math"]
wantedmajors = {}


wantedMaj = []

for entry in list_of_grad_major:
    for maj in wanted:
        if entry['Education']['Major'] == maj:
            wantedMaj.append(entry)


finalResults = {}

for maj in wanted:
    finalResults[maj] = {"female": 0, "male": 0}

for entry in wantedMaj:
    finalResults[entry['Education']['Major']]['female'] += entry['Demographics']['Gender']['Females']
    finalResults[entry['Education']['Major']]['male'] += entry['Demographics']['Gender']['Males']

print(finalResults)

# data to plot
n_groups = 6
number_female = (finalResults["Chemical Engineering"]["female"], finalResults["Mechanical Engineering"]["female"], finalResults["Electrical Engineering"]["female"], finalResults["Civil Engineering"]["female"],finalResults["Computer Science and Math"]["female"],finalResults["Other Engineering"]["female"])
number_male = (finalResults["Chemical Engineering"]["male"], finalResults["Mechanical Engineering"]["male"], finalResults["Electrical Engineering"]["male"], finalResults["Civil Engineering"]["male"],finalResults["Computer Science and Math"]["male"],finalResults["Other Engineering"]["male"])
print(finalResults["Chemical Engineering"]["female"])
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, number_female, bar_width,
alpha=opacity,
color='b',
label='Female')

rects2 = plt.bar(index + bar_width, number_male, bar_width,
alpha=opacity,
color='g',
label='Male')

plt.xlabel('Major')
plt.ylabel('# of Graduates')
plt.title('Demographics of STEM Majors')
plt.xticks(index + bar_width, ("ChemEng", "MechEng", "ElecEng", "CivEng", "OthrEng", "CompSci&Math"))
plt.legend()

plt.tight_layout()
plt.show()
