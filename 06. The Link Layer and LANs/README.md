# Chapter 6.  The Link Layer and LANs
## Section 1. Introduction to the Link Layer
### Notes
- Any device that runs a link-layer protocol is a node.
	- hosts
	- routers
	- switches
	- WiFi Access Points
- The communication channels that connect adjacent nodes along the communication path are referred as links.
- Over a given link, a transmitting node encapsulates the datagram in a link-layer frame and transmits the frame into the link.
- In this transportation analogy, the tourist is a datagram, each transportation segment is a link, the transportation mode is a link-layer protocol, and the travel agent is a routing protocol.
- Services that can be offered by a link-layer protocol
	- Framing
		- Almost all link-layer protocols encapsulate each network-layer data-gram within a link-layer frame before transmission over the link.
		- A frame consists of a data field, in which the network-layer datagram is inserted, and a number of header fields.
	- Link access
		- A medium access control (MAC) protocol specifies the rules by which a frame is transmitted onto the link.
		- No problem in point-to-point links. The problem occurs when multiple nodes share a single broadcast link—the so-called multiple access problem. 
	- Reliable delivery
		- When a link-layer protocol provides reliable delivery service, it guarantees to move each network-layer datagram across the link without error.
	- Error detection and correction
		- The link-layer hardware in a receiving node can incorrectly decide that a bit in a frame is zero when it was transmitted as a one, and vice versa.
		- Such bit errors are introduced by signal attenuation and electromagnetic noise.
- The link layer is implemented on a chip called the network adapter, also sometimes known as a network interface controller (NIC).
- The software components of the link layer implement higher-level link-layer functionality such as assembling link-layer addressing information and activating the controller hardware.
## Section 2. Error-Detection and -Correction Techniques
### Notes
- Error-detection and -correction techniques allow the receiver to sometimes, but not always, detect that bit errors have occurred.
	- Even with the use of error-detection bits there still may be undetected bit errors; that is, the receiver may be unaware that the received information contains bit errors.
- The simplest form of error detection is the use of a single parity bit.
- In an even parity scheme, the sender simply includes one additional bit and chooses its value such that the total number of 1s in the d + 1 bits (the original information plus a parity bit) is even.
	- For odd parity schemes, the parity bit value is chosen such that there is an odd number of 1s.
- The ability of the receiver to both detect and correct errors is known as forward error correction (FEC).
- In checksumming techniques, the d bits of data are treated as a sequence of k-bit integers.
	- One simple checksumming method is to simply sum these k-bit integers and use the resulting sum as the error-detection bits.
- An error-detection technique used widely in today’s computer networks is based on cyclic redundancy check (CRC) codes. CRC codes are also known as polynomial codes, since it is possible to view the bit string to be sent as a polynomial whose coefficients are the 0 and 1 values in the bit string, with operations on the bit string interpreted as polynomial arithmetic.
### Review Questions - SECTIONS 6.1–6.2
- Consider the transportation analogy in Section 6.1.1. If the passenger is analagous to a datagram, what is analogous to the link layer frame?
	- Link-layer frame is analogous to transportation tickets like plane ticket or bus ticket.
	- The transportation mode, e.g., car, bus, train, car.
- If all the links in the Internet were to provide reliable delivery service, would the TCP reliable delivery service be redundant? Why or why not?
	- TCP Relaible Delivery Service is not redundant. Although each link guarantees that an IP datagram sent over the link will be received at the other end of the link without errors, it is not guaranteed that the IP datagrams will arrive at the ultimate destination in the proper order. With IP, datagrams emerging from the same TCP connection can take different routes in the network, and therefore arrive out of order. TCP is still needed to provide the receiving end of the application the byte stream in the correct order, also, IP can lose packets due to routing loops or equiptment failure.
- What are some of the possible services that a link-layer protocol can offer to the network layer? Which of these link-layer services have corresponding services in IP? In TCP?
	- The below are some of the possible services that a link-layer protocol that offer to the network:
		- Link access
		- Reliable delivery
		- Framing
		- Error detection and correction
	- The above 4 link-layer services(Link access, Reliable delivery, Framing, and Error dection and correction) have corresponding services in TCP(Transfer control protocol). 
	- The  below 3 link layer services that  have corresponding to the services of IP are as follows: 
		- Link access
		- Framing 
		- Error detection and correction
