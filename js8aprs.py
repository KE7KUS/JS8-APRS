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

from socket import socket, AF_INET, SOCK_STREAM

# Default ports for data transport
# NOTE: These ports are dynamically configurable in both JS8Call and APRS client software

JS8_TCP = 2449
JS8_UDP = 2242
YAAC_KISS = 8001

server = '127.0.0.1'

class Connection:
  
  """Class to manage network connections."""
  
  def __init__(self, server_ip, port, protocol):
  
    """Initialize a network connection.  Server IP address in dotted quad format.  Valid protocols are TCP and UDP."""
   
    try:
      if ipaddress.ip_address(server_ip):
        self.server_ip = server_ip
    
    except:      
      raise Exception('Server IP address should be in dotted quad format (i.e. 127.0.0.1).')
      
    self.port = port
    
    try:
      valid_protocol = re.compile('[TCP]|[UDP]', re.IGNORECASE)
      if valid_protocol.match(protocol):
        self.protocol = protocol.upper()
      else:
        raise Exception('Valid protocols are either TCP or UDP.')
    
    except:
      raise Exception('Valid protocols are either TCP or UDP.')
  
if __name__ == "__main__":
    connection = Connection(server,JS8_TCP,'TCP')
