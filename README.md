# JS8-APRS

## Introduction
Many APRS clients make provision for bi-directional processing of APRS packets via KISS over TCP.  JS8Call provides access to a robust weak-signal HF modem via either a bi-directional TCP or UDP port utilizing JSON.  JS8-APRS allows an amateur radio operator to utilize a preferred KISS TCP-compatible APRS client to send and receive APRS traffic over HF using JS8 as the transport.

## Legacy Transports
From the earliest years of APRS, the HF transport for APRS data has historically been a single "channel" at the top end of the 30m band using 300 baud FSK packet to send and receive data.  While the 30m band has proved a sound choice for propagation, 300 baud FSK packets are easily corrupted by path noise, fading, and interference.  The reliability of the transport results in significant packet loss before channel congestion even becomes a factor.

## A Better Way
Historic HF APRS transmissions have been conducted at packet transmission rates far below the rates of APRS packets over VHF and UHF channels.  The low rate transmissions are intended to avoid packet collisions and channel congestion due to the far-reaching propagation of the 30m band, combined with the singular channel for data transmission.

JS8 as an HF APRS transport provides a significantly improved mechanism for moving APRS data over HF for the following reasons:

- Multiple simultaneous JS8 transmissions can be conducted inside the 200Hz bandwidth of a single legacy HF APRS packet.  Using the JS8 Normal mode with its 50Hz bandwidth, up to four JS8 packets can be simultaneously transmitted and decoded in the bandwidth used by one FSK APRS packet.  If expanded out to a nominal 2500Hz bandwidth compatible with almost every computer-radio audio interface, theoretically up to 50 stations can simultaneously transmit APRS data.
- Current FS8 and JS8 usage have proved that band-specific frequencies can be identified for APRS operation, allowing JS8-APRS operators the ability to shift HF operations to frequencies that support propagation, regardless of band conditions, solar cycle, and other factors impacting HF propagation.
- Leveraging the APRS-IS gateway features of software like YAAC and XASTIR, JS8-APRS gives remote amateur operators the ability to connect to the wider APRS infrastructure, while using existing connect filters and other features keep channel traffic manageable from a congestion standpoint.  In addition, the far-reaching propagation of HF packets reduces the need for complex APRS digipeater infrastructure needed for VHF operation.  Only a few receiving stations in a wide area need be configured as APRS-IS Gateway stations for JS8-APRS to provide effective access to the wider APRS network.
- JS8Call's native ability to encode and decode packet transmissions at varying data rates provides a powerful tool for JS8-APRS operators to adjust their data rate based on propagation conditions, available transmit power, and desired data rate.

While common-sense settings for bi-directional HF packet operation are still required (as they always were with legacy FSK APRS), JS8 provides a significantly improved HF APRS capability without the need for expensive external hardware.

## Gateway Operations
APRS client software such as YAAC, XASTIR, and Direwolf all provide native abilities to function as an APRS-IS gateway.  APRS-IS provides the ability to use connect filters to limit information flow on a specific APRS channel.  Some software suites also provide additional client-side filtering to further limit data flow on a single APRS channel.  The intelligent use of these filtering features allow JS8-APRS clients to send/receive APRS text messages, weather alerts, and whitelisted "buddy" station locations while eliminating non-pertient traffic on the low data rate channel.  Using the native gateway features of existing APRS client software eliminates the need for HF APRS operators to set up and configure additional software to provide gateway functionality for wide area operation.  A few dozen properly configured gateway stations around USA are all that would be needed to provide a working bidirectional HF-to-APRSIS network.
