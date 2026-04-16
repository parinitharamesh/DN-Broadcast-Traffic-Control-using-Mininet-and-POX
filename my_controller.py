from pox.core import core
import pox.openflow.libopenflow_01 as of

# Create a logger to print messages in terminal
log = core.getLogger()

class BroadcastControl(object):
    def __init__(self, connection):
        # Store switch connection
        self.connection = connection
        
        # Listen for packet_in events from switch
        connection.addListeners(self)

    def _handle_PacketIn(self, event):
        # Extract packet from event
        packet = event.parsed

        #  CONDITION: Check if packet is broadcast
        if packet.dst.is_broadcast():
            # Log detection
            log.info("Broadcast packet detected -> blocking")
            
            # Drop the packet (no forwarding)
            return

        # FORWARDING: For non-broadcast packets
        msg = of.ofp_packet_out()
        
        # Attach packet data
        msg.data = event.ofp
        
        # Action: Flood to all ports
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        
        # Send message to switch
        self.connection.send(msg)

# Called when switch connects
def launch():

    def start_switch(event):
        log.info("Controlling %s" % (event.connection,))
        
        # Create controller instance for this switch
        BroadcastControl(event.connection)

    # Listen for switch connection event
    core.openflow.addListenerByName("ConnectionUp", start_switch)
