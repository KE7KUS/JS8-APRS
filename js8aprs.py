#!/usr/bin/python3

# JS8-APRS
# Client software allowing the use of the JS8 digital mode as an APRS data transport on HF
# Copyright 2022 Kurt Kochendarfer, KE7KUS

# This file is part of JS8-APRS.

# JS8-APRS is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License, as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# JS8-APRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with JS8-APRS. If not, see <https://www.gnu.org/licenses/>.

import json
import time
import sys
import ipaddress
import re
import kiss

from socket import socket, AF_INET, SOCK_STREAM

# Default ports for data transport
# NOTE: These ports are dynamically configurable in both JS8Call and APRS client software

JS8_TCP = 2449
JS8_UDP = 2242
YAAC_KISS = 8001

server = '127.0.0.1'

class Connection:
  
  """Class to manage network connections."""
  
  def __init__(self, server_ip, port, protocol = 'TCP'):
  
    """Initialize a network connection.  Server IP address can be in any format supported by ipaddress."""
   
    try:
      if ipaddress.ip_address(server_ip):
        self.server_ip = server_ip
    
    except:      
      raise Exception('Server IP address not in a supported format.  See ipaddress documentation for details.')
      
    try:
      if port in range(1,65535):
        self.port = port
      else:
        raise Exception('Valid port range is 1-65535.')
    
    except:
      raise Exception('Valid port range is 1-65535.')
    
    try:
      valid_protocol = re.compile('[TCP]|[UDP]', re.IGNORECASE)
      if valid_protocol.match(protocol):
        self.protocol = protocol.upper()
      else:
        raise Exception('Valid protocols are either TCP or UDP.')
    
    except:
      raise Exception('Valid protocols are either TCP or UDP.')
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def closeConnection(connection):
      
    """Close existing network connection."""
      
class Message:
  
  """Class to manage message traffic between software clients."""
  
  def __init__(self):
    
    """Initialize a data message."""
  
  def sendToJS8(sock, payload):
    
    """Send message to JS8Call TCP port, where 'sock' is a valid socket object and 'payload' is the payload to be converted to a JSON string."""
    
    try:
      message = json.dumps(payload)
      skt.sendall(message)
    
    except:
      raise Exception('Error sending message to JS8Call.')
  
# TODO: Open JS8Call software
# TODO: Open APRS Client software (YAAC, XASTIR, Direwolf, etc.)
# TODO: Initialize js8aprs functionality
# TODO: Open TCP server on port 2449 to send/receive JS8Call JSON traffic
# TODO: Open TCP server on port 8001 to send/receive KISS TCP traffic

# TODO: Create simple GUI in Qt to set the following parameters:
# - JS8Call executable location
# - APRS client executable location
# - Set JS8Call TCP port
# - Set APRS Client KISS TCP port
# - Display running window of traffic to/from JS8Call
# -- Use packet data colorization similar to Direwolf to identify packet content/source/destination

# SENDING APRS DATA TO JS8CALL
# - Receive KISS TCP packet on port 8001
# - Strip KISS encapsulation from packet to obtain payload message
# - Convert payload into JS8Call API JSON TX.SEND_MESSAGE format
# - Send JSON TCP packet on port 2449

# RECEIVING APRS DATA FROM JS8CALL
# - Receive JSON TCP using JS8Call API RX.ACTIVITY or RX.TEXT format on port 2449
# - Parse JSON packet to obtain payload data
# -- Depending on what is received from JS8Call, may have to use regex and/or string slicing to identify & parse APRS packets
# -- May have to implement full-blown APRS packet validator to ensure only valid packets are forwarded to the KISS TCP port
# - Convert payload into KISS TCP packet
# - Send KISS TCP packet on port 8001

  
if __name__ == "__main__":
    js8call_connection = Connection(server,JS8_TCP,'TCP')
