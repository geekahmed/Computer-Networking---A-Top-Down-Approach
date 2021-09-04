
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
### Review Questions

## Section 4. Delay, Loss, and Throughput in Packet-Switched Networks
### Notes
### Review Questions
## Section 5. Protocol Layers and Their Service Models
### Notes
### Review Questions
## Section 6. Networks Under Attack
### Notes
### Review Questions
## Section 7. History of Computer Networking and the Internet
### Notes
### Review Questions

