import sys
import pandas as pd

# create the original dataframe from input csv file
input = sys.argv[1:]
try:
    point_spent = int(input[0])
    with open(input[1]) as f:
        df = pd.read_csv(f)

except Exception as e:
    print(e)


# sort rows of dataframe based on timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values(by="timestamp").reset_index()


# calculate points after transaction

df = df[["payer", "points"]]
points = list(df["points"])
for i in range(len(points)):
    if (points[i] <= 0):
        point_spent = point_spent - points[i]
        points_after = 0
        points[i] = points_after
        continue
    elif (points[i] >= point_spent):
        points_after = points[i] - point_spent
        points[i] = points_after
        break
    else:
        point_spent = point_spent - points[i]
        points_after = 0
        points[i] = points_after

# update the calculated result to dataframe
df.loc[:, "points"] = points


# use hashmap to show all payer's points left
hash_map = {}

for index, row in df.iterrows():
    payer = row["payer"]
    points = row["points"]

    if payer not in hash_map:
        hash_map[payer] = points
    else:
        hash_map[payer] = hash_map[payer] + points

print(hash_map)


