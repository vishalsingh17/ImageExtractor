from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': 'secure-connect-imgscraper.zip'
}
auth_provider = PlainTextAuthProvider('qUEZhPpEaMRjvfBerAOFkgSy', 'TDnknrH_pZMJZbEjTS0I8jNdhiZK0W357-m_.ZS+WcHxb6d5NU7zSUli.8lKle4P4W5bMEU83w3epxoNA6QLRfATznNLMgdzxGlH3qD0saOQzWpNG_eowr6ntHswJoUc')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")