from google.cloud import bigtable
from google.cloud.bigtable import column_family
from google.cloud.bigtable import row_filters
import datetime

project_id = "pictetinterview"
instance_id = "pictetinterviewbigtable"

table_id = "attendance"

client = bigtable.Client(project=project_id, admin=True)
instance = client.instance(instance_id)

print('Creating the {} table.'.format(table_id))
table = instance.table(table_id)

max_versions_rule = column_family.MaxVersionsGCRule(2)
column_family_id = 'team'
column_families = {column_family_id: max_versions_rule}
if not table.exists():
    table.create(column_families=column_families)
else:
    print("Table {} already exists.".format(table_id))

team_dataset_file = open("nba_teams_dataset.csv", "r+")

lines = team_dataset_file.readlines()
headers = lines[0].strip().split(";")
data = map(lambda x: x.strip().split(";"), lines[1:])

rows = []
for row_data in data:
    row_key = row_data[0] + "/" + row_data[19]
    row = table.row(row_key)
    print(row_data)
    for i, header in enumerate(headers):
        print(row_data[i])
        print(header)
        row.set_cell("team",
                    header,
                    row_data[i],
                    timestamp=datetime.datetime.utcnow())
    rows.append(row)
table.mutate_rows(rows)