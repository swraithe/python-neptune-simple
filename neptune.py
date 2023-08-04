from __future__  import print_function  # Python 2/3 compatibility

from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

graph = Graph()

remoteConn = DriverRemoteConnection('wss://database-neptune-instance-1.czmqqwbmeqyz.eu-west-2.neptune.amazonaws.com:8182/gremlin','g')
g = graph.traversal().withRemote(remoteConn)
# Insert nodes node-1, node-2, node-3
g.addV('node').property('name', 'node-1').property('info', 'Initial info for node-1').as_('node1') \
    .addV('node').property('name', 'node-2').property('info', 'Initial info for node-2').as_('node2') \
    .addV('node').property('name', 'node-3').property('info', 'Initial info for node-3').as_('node3') \
    .iterate()

# Commit the changes
g.tx().commit()

print(g.V().limit(2).toList())
remoteConn.close()