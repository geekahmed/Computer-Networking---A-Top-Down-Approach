# Chapter 3.  Transport Layer
## Section 1. Introduction and Transport-Layer Services
### Notes
- A transport-layer protocol provides for logical communication between application processes running on different hosts.
- A network-layer protocol provides logical communication between hosts.
- A computer network may make available multiple transport protocols, with each protocol offering a different service model to applications.
- The services that a transport protocol can provide are often constrained by the service model of the underlying network-layer protocol.
  - If the network-layer protocol cannot provide delay or bandwidth guarantees for transport-layer segments sent between hosts, then the transport-layer protocol cannot provide delay or bandwidth guarantees for application messages sent between processes.
- A transport protocol can use encryption to guarantee that application messages are not read by intruders, even when the network layer cannot guarantee the confidentiality of transport-layer segments.
- UDP (User Datagram Protocol) provides an unreliable, connectionless service to the invoking application.
- TCP (Transmission Control Protocol) provides a reliable, connection-oriented service to the invoking application.
- Extending host-to-host delivery to process-to-process delivery is called transport-layer multiplexing and demultiplexing.
  
## Section 2.  Multiplexing and Demultiplexing  
### Notes
- The job of delivering the data in a transport-layer segment to the correct socket is called demultiplexing.
- The job of gathering data chunks at the source host from different sockets, encapsulating each data chunk with header information (that will later be used in demultiplexing) to create segments, and passing the segments to the network layer is called multiplexing.
- The transport-layer multiplexing requires
  - (1) that sockets have unique identifiers,
  - (2) that each segment have special fields that indicate the socket to which the segment is to be delivered.
- The port numbers ranging from 0 to 1023 are called well-known port numbers and are restricted.
- UDP socket is fully identified by a two-tuple consisting of a destination IP address and a destination port number.
  - if two UDP segments have different source IP addresses and/or source port numbers, but have the same destination IP address and destination port number, then the two segments will be directed to the same destination process via the same destination socket.
- TCP socket is identified by a four-tuple: (source IP address, source port number, destination IP address, destination port number).
  - when a TCP segment arrives from the network to a host, the host uses all four values to direct (demultiplex) the segment to the appropriate socket.
   
## Section 2. Connectionless Transport: UDP
### Notes
 - UDP does just about as little as a transport protocol can do.
   - multiplexing/demultiplexing and light error checking.
  - With UDP there is no handshaking between sending and receiving transport-layer entities before sending a segment.
	  - This is the reason of calling UDP connectionless protocol.
  - UDP is unreliable transport-layer protocol.
  - The reasons of using UDP protocol with some applications:
	  - Finer application-level control over what data is sent, and when.
	  - No connection establishment.
	  - No connection state.
	  - Small packet header overhead.
  - UDP Segment Structure
```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
-----------------------------------------------------------------
|          Source Port          |        Destination Port       |
-----------------------------------------------------------------
|             Length            |            Checksum           |
-----------------------------------------------------------------
                                DATA
```
	- The application data occupies the data field of the UDP segment.
	- The UDP header has only four fields, each consisting of two bytes.
	- The port numbers are used in multiplexing and de-multiplexing features.
	- The length field specifies the number of bytes in the UDP segment (header + data).
	- The checksum is used by the receiving host to check whether errors have been introduced into the segment .
- UDP Checksum
	- UDP at the sender side performs the 1s complement of the sum of all the 16-bit words in the segment, with any overflow encountered during the sum being wrapped around.
	- Example of this mechanism.
	- For the following three 16-bit words:
		- 0110011001100000
		- 0101010101010101
		- 1000111100001100
	- The sum of first two of these 16-bit words is
		- 0110011001100000 
		- 0101010101010101
		- +----------------------
		- 1011101110110101
	- Adding the third word to the above sum gives:
		- 1011101110110101 
		- 1000111100001100 
		- =------------------------
		- 0100101011000010
	- The 1s complement is obtained by converting all the 0s to 1s and converting all the 1s to 0s. Thus, the 1s complement of the sum 0100101011000010 is 1011010100111101, which becomes the checksum.
	- At the receiver, all four 16-bit words are added, including the checksum. If no errors are introduced into the packet, then clearly the sum at the receiver will be 1111111111111111.
	- If one of the bits is a 0, then we know that errors have been introduced into the packet.
- Why UDP provides a checksum in the first place, as many link-layer protocols also provide error checking?
	- There is no guarantee that all the links between source and destination provide error checking.
	-  If segments are correctly transferred across a link, it’s possible that bit errors could be introduced when a segment is stored in a router’s memory.
- End-end principle is a system design principle which states that since certain functionality must be implemented on an end-end basis: “functions placed at the lower levels may be redundant or of little value when compared to the cost of providing them at the higher level.”
### Review Questions - Sections 3.1–3.3
- Suppose the network layer provides the following service. The network layer in the source host accepts a segment of maximum size 1,200 bytes and a destination host address from the transport layer. The network layer then guarantees to deliver the segment to the transport layer at the destination host. Suppose many network application processes can be running at the destination host.
  - Design the simplest possible transport-layer protocol that will get application data to the desired process at the destination host. Assume the operating system in the destination host has assigned a 4-byte port number to each running application process.
  - Modify this protocol so that it provides a “return address” to the destination process.
  - In your protocols, does the transport layer “have to do anything” in the core of the computer network?
