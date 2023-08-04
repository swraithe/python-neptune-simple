from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

# Connect to your Neptune cluster
neptune_endpoint = 'database-neptune.cluster-czmqqwbmeqyz.eu-west-2.neptune.amazonaws.com'
neptune_port = '8182'
g = traversal().withRemote(DriverRemoteConnection(f'wss://{neptune_endpoint}:{neptune_port}/gremlin', 'g'))

# Insert nodes node-1, node-2, node-3
g.addV('node').property('name', 'node-1').property('info', 'Initial info for node-1').as_('node1') \
    .addV('node').property('name', 'node-2').property('info', 'Initial info for node-2').as_('node2') \
    .addV('node').property('name', 'node-3').property('info', 'Initial info for node-3').as_('node3') \
    .iterate()

# Commit the changes
g.tx().commit()