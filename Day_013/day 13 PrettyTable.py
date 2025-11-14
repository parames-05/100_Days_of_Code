import prettytable as pta
table=pta.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Charmander","Squirtle","Geode"])
table.add_column("Type",["Electric","Fire","Water", "Rock"])
table.align ="r"
print(table)
