from neo4j import GraphDatabase
driver = GraphDatabase.driver(
    "neo4j+s://4c4b3423.databases.neo4j.io",
    auth=("4c4b3423", "Z6vdj_x_TidjsEi4exhDUVMwQBjElFiYL5ql3Qw5kbk")
)
driver.verify_connectivity()
print("✅ OK")
driver.close()