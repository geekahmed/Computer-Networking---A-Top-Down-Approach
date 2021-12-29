# Chapter 1. Computer Networks and the Internet

## Section 1. What Is the Internet?
### Notes
 - The Internet is a computer network that interconnects billions of computing devices throughout the world. Theses are called hosts or end-systems like:
	 - Desktop computers.
	 - Linux workstations.
	 - Smartphones and Tablets.
	 - Gaming consoles.
	 - Home security systems.
	 - Watches.
 - End systems are connected together by a network of communication links and packet switches.
 -  Different links can transmit data at different rates, with the transmission rate of a link measured in bits/second.
 - Packets are the result of segmenting data and adding headers by the end-system in order to send it to the destination.
 - A packet switch takes a packet arriving on one of its incoming communication links and forwards that packet on one of its outgoing communication links.
	 - Routers:: Used in the network core.
	 - Link-Layer Switches: Used in access networks.
 - The sequence of communication links and packet switches traversed by a packet from the sending end system to the receiving end system is known as a route or path through the network.
 - End systems access the Internet through Internet Service Providers (ISPs)
	 - Residential ISPs: local cable or telephone companies.
	 - Corporate ISPs.
	 - University ISPs.
 - End systems, packet switches, and other pieces of the Internet run protocols that control the sending and receiving of information within the Internet.
	 - Transmission Control Protocol (TCP) 
	 - Internet Protocol (IP) 
 - Another defintion for the internet is an infrastructure that provides services to applications.
 - End systems attached to the Internet provide a socket interface that specifies how a program running on one end system asks the Internet infrastructure to deliver data to a specific destination program running on another end system.
 - A protocol defines the format and the order of messages exchanged between two or more communicating entities, as well as the actions taken on the transmission and/or receipt of a message or other event.

### Review Questions
 - What is the difference between a host and an end system? List several different types of end systems. Is a Web server an end system?
	 - There is no difference.
	 - End-systems include web servers, linux workstations, gaming consoles, etc.
 - The word protocol is often used to describe diplomatic relations. How does Wikipedia describe diplomatic protocol?
	 - Based on Wikipedia the defintion of protocol is commonly described as a set of international courtesy rules. These well-established and time-honored rules have made it easier for nations and people to live and work together. Part of protocol has always been the acknowledgment of the hierarchical standing of all present. Protocol rules are based on the principles of civility.
 - Why are standards important for protocols?
	 - As it enables to develop independent and interoperate systems.

## Section 2. The Network Edge
### Notes
- End systems are referred to as hosts because they host (run) application programs such as:
	- Web browser
	- Web server
	- E-mail client
	- E-mail server
- Access network is the network that physically connects an end system to the first router (edge router) on a path from the end system to any other distant end system.
- The two most prevalent types of broadband residential access are digital subscriber line (DSL) and cable.
- Telephone line for obtaining DSL is divided into:
	- A high-speed downstream channel (50 KHZ to 1 MHZ band)
	- A medium-speed upstream channel (4 KHZ to 50 KHZ band)
	- An ordinary two-way telephone channel (0 to 4 KHZ band)
- The DSL standards define multiple transimission rates, including downstream transmission rates 24 Mbs and 52 Mbs, and upstream rates of 3.5 Mbps and 16 Mbps.
- The access is asymmetric because the downstream and upstream rates are different.
- The actual rates are limied by:
	- The DSL provider due to tiered services.
	- The gauge if the twisted-pair line.
	- The degree of electrical interference.
- DSL is designed for short distances between 5 and 10 miles.
- Cable internet access makes use if the cable television company's existing cable television infrastructure.
- Physical media is categorized as
	- Guides media:
		- Fiber-optic cable
			- An optical fiber is a thin, flexible medium that conducts pulses of light, with each pulse representing a bit.
			- They are immune to electromagnetic interference, have very low signal attinuation up to 100 KMs.
			- The Optical Carrier (OC) standard link speeds range from 51.8 Mbps to 39.8 Gbps. These specifications are often referred to as OC-n, where the link speed equals n * 51.8 Mbps.
		- Twisted-pair copper wire
			- Consists of two insulated copper wires, each about 1 mm thick, arranged in a regular spiral pattern.
			- The wires are twisted together to reduce the electrical interference from similar pairs close by.
		- Coaxial cable
			- Consists of two copper conductors, but the two are cocentric rather than parallel.
			- It can be used as a guided shared medium.
	- Unguided media:
		- Wireless LAN
		- Digital satellite channel
- The actual cost of physical link is relatively minor compared with other networking costs.
### Review Questions
-  List four access technologies. Classify each one as home access, enterprise access, or wide-area wireless access.
	- Home access: Ethernet LAN, Digital Subscriber Line over telephone line, and Cable internet access.
	- Enterprise access: Ethernet, WI-FI.
	- Wide-are Wireless access: 4G, 5G.
- Is HFC transmission rate dedicated or shared among users? Are collisions possible in a downstream HFC channel? Why or why not?
	- Shared.
	- On the downstream channel, all packets emanate from a single source, namely, the head end. Thus, there are no collisions in the downstream channel.
-  List the available residential access technologies in your city. For each type of access, provide the advertised downstream rate, upstream rate, and monthly price.
- What is the transmission rate of Ethernet LANs?
	- Ethernet LANs have transmission rates of 10 Mbps, 100 Mbps, 1 Gbps and 10 Gbps. 
- What are some of the physical media that Ethernet can run over?
	- Twisted-pair copper cables.
	- Fiber-optics cables.
- HFC, DSL, and FTTH are all used for residential access. For each of these access technologies, provide a range of transmission rates and comment on whether the transmission rate is shared or dedicated.
	- HFC: up to 42.8 Mbps and upstream rates of up to 30.7 Mbps, bandwidth is shared
	- DSL: up to 24 Mbps downstream and 2.5 Mbps upstream, bandwidth is dedicated
	- FTTH: 2-10Mbps upload; 10-20 Mbps download; bandwidth is not shared.
- Describe the most popular wireless Internet access technologies today. Compare and contrast them.
	- Wifi (802.11) In a wireless LAN, wireless users transmit/receive packets to/from an base station (i.e., wireless access point) within a radius of few tens of meters. The base station is typically connected to the wired Internet and thus serves to connect wireless users to the wired network.
	- 3G and 4G wide-area wireless access networks. In these systems, packets are transmitted over the same wireless infrastructure used for cellular telephony, with the base station thus being managed by a telecommunications provider. This provides wireless access to users within a radius of tens of kilometers of the base station.

## Section 3. The Network Core
### Notes
 - To send a message from source end system to a destination end system, the source breaks long messages into smaller chunks of data known as packets.
 - Packet switches implement the store-and-forward mechanism.
	- That means the packet switch must receive the entire packet before it can begin to transmit the first bit of the packet onto the outbound link.
 - Propagation delay is the time takes for the bits to travel across the wire near the speed of light.
 - End-to-end delay equals: N*(L/R)
	- N: number of links.
	- R: rate of each link
	- L: packet length
 - Each packet switch has multiple links attached to it.
	- For each attached link, the packet switch has an output buffer, which stores packets that the router is about to send into that link.
 - Packets suffer from delaying due to store-and-forward and queuing.
 - Packet loss occurs when there is a congestion in the network which results in the filling of the output buffer.
 - Each router has a forwarding table that maps destination addresses to the router's outbound links.
### Review Questions
 - Suppose there is exactly one packet switch between a sending host and a receiving host. The transmission rates between the sending host and the switch and between the switch and the receiving host are R1 and R2, respectively. Assuming that the switch uses store-and-forward packet switching, what is the total end-to-end delay to send a packet of length L? (Ignore queuing, propagation delay, and processing delay.)
	 - (L/R1)+(L/R2)
 - What advantage does a circuit-switched network have over a packet switched network? What advantages does TDM have over FDM in a circuit-switched network?
	 - Circuit-switched networks are well suitable for real time servicessuch as voice calls and video calls whereas packet-switched network are not suitable for real time services. They are suitable for handling data.
	 - In circuit-switched networks, the transmission link is pre-allocated without taking into consideration the demand whereas packet-switched network allocates transmission link on demand.
	 - In circuit-switched network, the bandwidth is reserved and so packets arrive within the bandwidth whereas in packet-switched network, the bandwidth is not reserved and so the packets may have to wait for their turn to be forwarded.
	 - In time division multiplexing, all connections operate with same frequency at different times where as in frequency division multiplexing, all connections operate with different frequencies at the same time.
	 - In TDM, when the network establishes a connection across a link, the network dedicates one time slot in every frame to the connection which is used only for that connection.
 -  Suppose users share a 2 Mbps link. Also suppose each user transmits continuously at 1 Mbps when transmitting, but each user transmits only 20 percent of the time.
	 - When circuit switching is used, how many users can be supported?
		 - 2 users can be supported because each user requires half of the link bandwidth.
	 - For the remainder of this problem, suppose packet switching is used. Why will there be essentially no queuing delay before the link if two or fewer users transmit at the same time? Why will there be a queuing delay if three users transmit at the same time?
		 - Since each user requires 1Mbps when transmitting, if two or fewer users transmit simultaneously, a maximum of 2Mbps will be required. Since the available bandwidth of the shared link is 2Mbps, there will be no queuing delay before the link. Whereas, if three users transmit simultaneously, the bandwidth required will be 3Mbps which is more than the available bandwidth of the shared link. In this case, there will be queuing delay before the link.
	 - Find the probability that a given user is transmitting.
		 - 0.008
	 - Suppose now there are three users. Find the probability that at any given time, all three users are transmitting simultaneously. Find the fraction of time during which the queue grows.
		 - Since the queue grows when all the users are transmitting, the fraction of time during which the queue grows (which is equal to the probability that all three users are transmitting simultaneously) is 0.008.
 - Why will two ISPs at the same level of the hierarchy often peer with each other? How does an IXP earn money?
	 - By peering with each other, two ISP’s can reduce their cost and avoid paying to the intermediate ISP provider.
	- An Internet Exchange Points (IXP) can earn money by charging each ISP that connects to it. The IXP charges each ISP based on the amount of traffic sent to or received from the IXP.
 -  Some content providers have created their own networks. Describe Google’s network. What motivates content providers to create these networks?
	- Google’s network: 
		- This network provides global data. 
		- It is used to transfer content within the Google servers. 
		- Its contains some Tier-1 ISP and interconnect with TCP/IP.
	- Motivates: 
		- It is used to save money by transfer data and less time to travel content. 
		- Content providers to control over the services.
## Section 4. Delay, Loss, and Throughput in Packet-Switched Networks
### Notes
- The most important delays that face packets are:
	- Nodal Processing Delay
		- The time required to examine the packet's header and determine where to direct the packet.
		- This delay is typically on the order of microseconds or less.
	- Queuing Delay
		- At the queue, the packet experiences a delay as it waits to be transmitted onto the link.
		- This delay can be on the order of microseconds to milliseconds.
	- Transmission Delay
		- The amount of time required to push all of the packet's bits into the link.
		- This delay is on the order of microseconds to milliseconds.
	- Propagation Delay
		- The time required to propagate from the beginning of the link to the next router.
		- The speed depends on the link physical medium.
		- In WAN, this dely is on the order of milliseconds.
- The traffic intensity is the ration of (arrival rate of bits) and (service rate of bits)
	- let, a: average packet arrival rate, L: packet length (bits), R: link bandwidth (bit transmission rate).
	- Traffic Intensity = L.a/R
	- La/R ~ 0: avg. queueing delay small
	- La/R -> 1: avg. queueing delay large
	- La/R > 1: more “work” arriving  is more than can be serviced -  average delay infinite!
- The fraction of lost packets increases as the traffic intensity increases.
- Performance at a node is often measured not only in terms of delay, but also in terms of the probability of packet loss.
- traceroute program: provides delay measurement from source to router along end-end Internet path towards destination.
- Throughput: rate (bits/time unit) at which bits are being sent from sender to receiver.
	- instantaneous: rate at given point in time.
	- average: rate over longer period of time.
- bottleneck link: link on end-end path that constrains  end-end throughput.
### Review Questions
- Consider sending a packet from a source host to a destination host over a fixed route. List the delay components in the end-to-end delay. Which of these delays are constant and which are variable?
	- Nodal Processing Delay (Constant).
	- Queuing Dealy (Variable).
	- Transmission Delay (Constant).
	- Propagation Delay (Constant).
-  How long does it take a packet of length 1,000 bytes to propagate over a link of distance 2,500 km, propagation speed 2.5 * 10^8 m/s, and transmission rate 2 Mbps? More generally, how long does it take a packet of length L to propagate over a link of distance d, propagation speed s, and transmission rate R bps? Does this delay depend on packet length? Does this delay depend on transmission rate?
	- The propagation delay is the ratio between the distance and the speed which is numerically equal to 0.01 seconds.
	- This numerical value doesn't depend on the length of the packet or the transmission rate.
- Suppose Host A wants to send a large file to Host B. The path from Host A to Host B has three links, of rates R1 = 500 kbps, R2 = 2 Mbps, and R3 = 1 Mbps. 
	- a. Assuming no other traffic in the network, what is the throughput for the file transfer?
		- The minimum value of the rates of the three links = 500 Kbps.
	- b. Suppose the file is 4 million bytes. Dividing the file size by the throughput, roughly how long will it take to transfer the file to Host B?
		- 64 seconds.
## Section 5. Protocol Layers and Their Service Models
### Notes
- A layered architecture allows us to discuss a well-defined, specific part of a large and complex system.
- The internet protocol stack consists of the following layers from top to down:
	- Application layer: HTTP, SMTP, FTP, DNS
	- Transport layer: TCP, UDP
	- Network layer: IP
	- Link layer: Ethernet, WIFI
	- Physical layer
### Review Questions
-  List five tasks that a layer can perform. Is it possible that one (or more) of these tasks could be performed by two (or more) layers?
	-  Five generic tasks are error control, flow control, segmentation and reassembly, multiplexing, and connection setup.
	- Yes. Each layer in the Internet protocal stack implement an error recovery on pre-link basis and end-to-end basis.
- What are the five layers in the Internet protocol stack? What are the principal responsibilities of each of these layers?
	- Application layer: 
	- Transport layer: transports application-layer messages between application endpoints.
	- Network layer: moves network-layer packets from one host to another.
	- Link layer: routes a datagram through a series of routers between the source and destination.
	- Physical layer: moves the individual bits within the frame from one node to the next.
- What is an application-layer message? A transport-layer segment? A network-layer datagram? A link-layer frame?
	- Application-layer message is the information at the application layer.
	- Transport-layer segment is the packet at the transport layer after adding headers.
- Which layers in the Internet protocol stack does a router process? Which layers does a link-layer switch process? Which layers does a host process?
	- Routers process network, link and physical layers (layers 1 through 3).
	- Link layer switches process link and physical layers (layers 1 through 2).
	- Hosts process all five layers.
## Section 6. Networks Under Attack
### Notes
- 
### Review Questions
-  What is self-replicating malware?
- Describe how a botnet can be created and how it can be used for a DDoS attack.
- Suppose Alice and Bob are sending packets to each other over a computer network. Suppose Trudy positions herself in the network so that she can capture all the packets sent by Alice and send whatever she wants to Bob; she can also capture all the packets sent by Bob and send whatever she wants to Alice. List some of the malicious things Trudy can do from this position.
## Section 7. History of Computer Networking and the Internet
### Notes

