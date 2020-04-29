from azure.eventhub import EventHubConsumerClient
from azure.identity import ClientSecretCredential
import json

#read config file
config = json.loads(open('config.json','r').read())

#App details and further config
tenantID = config["tenantID"]
clientID = config["clientID"]
clientSecret = config["clientSecret"]
miehaddress = config["eventhubNamespaceURI"] #needs to be in FQDN format without protocal prefix, e.g. "myeventhubnamespace.servicebus.windows.net"

eventhub_name = "mitest"
consumer_group = '$Default'

#create identity
identity = ClientSecretCredential(tenant_id=tenantID, client_id=clientID, client_secret=clientSecret )

ehclient = EventHubConsumerClient(credential= identity, fully_qualified_namespace=miehaddress, eventhub_name=eventhub_name, consumer_group = consumer_group)

#funtion that needs to be implemented and passed as a parameter to receive()
def on_event(partition_context, event):
    print("Received event from partition {}".format(partition_context.partition_id))
    print(event.body_as_str())
    partition_context.update_checkpoint(event)

ehclient.receive(
    on_event=on_event, 
    starting_position="-1",  # "-1" is from the beginning of the partition.
)
# receive events from specified partition:
# client.receive(on_event=on_event, partition_id='0')