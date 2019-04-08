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

row_filter = row_filters.CellsColumnLimitFilter(1)

print('Scanning for all greetings:')
partial_rows = table.read_rows(filter_=row_filter)

for row in partial_rows:
    cell = row.cells["team"]['team'.encode()][0]
    print(cell.value.decode('utf-8'))