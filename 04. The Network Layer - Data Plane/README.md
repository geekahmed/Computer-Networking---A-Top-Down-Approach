# Chapter 4.  The Network Layer: Data Plane
## Section 1. Overview of Network Layer
### Notes
- The primary role of the network layer is to move packets from a sending host to a receiving host.
- Forwarding refers to the router-local action of transferring a packet from an input link interface to the appropriate output link interface.
	- takes place at very short timescales
	- implemented in hardware.
- Routing refers to the network-wide process that determines the end-to-end paths that packets take from source to destination.
	- takes place on much longer timescalesas
	- implemented in software.
- Forwarding table in a router stores values that indicate the outgoing link interface at that router to which the packet is to be forwarded.
	- The content of the forwarding table is determined using routing algorithms.
- The routing algorithm function in one router communicates with the routing algorithm function in other routers to compute the values of its forwarding table.
	- This communication is performed by exchanging routing messages containing routing information according to a routing protocol.
- In SDN, controle-plane routing functionality is spearated from the physical router.
	- The routing device performs forwarding only, while the remote controller computes and distributes forwarding tables.
- The network service model defines the characteristics of end-to-end delivery of packets between sending and receiving hosts.
- List of possible network-layer sevices:
	- Guaranteed delivery.
	- Guarenteed delivery with bounded delay.
	- In-order packet delivery.
	- Guaranteed minimal bandwidth.
	- Security.
- The internet's network layer provides a single service, known as best-effort service. 
### Review Questions
- Let’s review some of the terminology used in this textbook. Recall that the name of a transport-layer packet is segment and that the name of a link-layer packet is frame. What is the name of a network-layer packet? Recall that both routers and link-layer switches are called packet switches. What is the fundamental difference between a router and link-layer switch?
	- Datagram.
	- Router forwards the packets based on header values like IP address.
	- Switch uses link-layer frame header MAC.
- We noted that network layer functionality can be broadly divided into data plane functionality and control plane functionality. What are the main functions of the data plane? Of the control plane?
	- Data plane basically is responsible of forwarding the data.
	- Controle plane is responsible of routing algorithms and the end-to-end path.
- We made a distinction between the forwarding function and the routing function performed in the network layer. What are the key differences between routing and forwarding?
	- Routing functionality is a global functionality and many routers cooperate with each other to define the best routes.
	- While switching functionality, is a local functionality in a specific router to forward the data to an outgoing link interface.
- What is the role of the forwarding table within a router?
	- Stores ranges of IP addresses accombined with the outgoing interface.
- We said that a network layer’s service model “defines the characteristics of end-to-end transport of packets between sending and receiving hosts.” What is the service model of the Internet’s network layer? What guarantees are made by the Internet’s service model regarding the host to-host delivery of datagrams?
	- Best-effort.
	- It gurantees nothing litteraly.
## Section 2. What’s Inside a Router?
### Notes
- A generic router architecture contains the following components:
	- Input ports: perform the following functions:
		- Physical layer function of terminating an incoming physical link at a router.
		- Link-Layer functions needed to interoperate with the link-layer at the other side of the incoming link.
		- Lookup function consulting the forward table to determine the router output port to which an arriving packet will be forwarded via the switching fabric.
	- Switching fabric: connects the router's input ports to its output ports.
	- Output ports: stores packets received from the switching fabric and transmits these packets on the outgoing link by performing the necessary link-layer and physical-layer functions.
	- Routing processor: performs the control-plane functions.
- The forwarding table is copied from from the routing processor to the lie cards over a separate bus.
	- This shadow copy at each line card makes forwarding decisions be made locally at each input port without invoking the centeralized routing processor on per-packet basis and this avoiding a centralized processing bottleneck.
- The forwarding table save the prefix of ranges mapped to the interface link.
- If an IP could be mapped to two prefixes, then the router uses the longest prefix matching rule.
- Some other actions taken in the input port:
	- physical- and link-layer processing must occur
	- the packet’s version number, checksum and time-to-live field must be checked and the latter two fields rewritten
	- counters used for network management (such as the number of IP datagrams received) must be updated.
### Review Questions
- In Section 4.2, we saw that a router typically consists of input ports, output ports, a switching fabric and a routing processor. Which of these are implemented in hardware and which are implemented in software? Why? Returning to the notion of the network layer’s data plane and control plane, which are implemented in hardware and which are implemented in software? Why?
- Discuss why each input port in a high-speed router stores a shadow copy of the forwarding table.
- What is meant by destination-based forwarding? How does this differ from generalized forwarding (assuming you’ve read Section 4.4, which of the two approaches are adopted by Software-Defined Networking)?
- Suppose that an arriving packet matches two or more entries in a router’s forwarding table. With traditional destination-based forwarding, what rule does a router apply to determine which of these rules should be applied to determine the output port to which the arriving packet should be switched?
- Three types of switching fabrics are discussed in Section 4.2. List and briefly describe each type. Which, if any, can send multiple packets across the fabric in parallel?
- Describe how packet loss can occur at input ports. Describe how packet loss at input ports can be eliminated (without using infinite buffers).
- Describe how packet loss can occur at output ports. Can this loss be pre- vented by increasing the switch fabric speed?
- What is HOL blocking? Does it occur in input ports or output ports?
- In Section 4.2, we studied FIFO, Priority, Round Robin (RR), and Weighted Fair Queueing (WFQ) packet scheduling disciplines? Which of these queueing disciplines ensure that all packets depart in the order in which they arrived?
- Give an example showing why a network operator might want one class of packets to be given priority over another class of packets.
- What is an essential different between RR and WFQ packet scheduling? Is there a case (Hint: Consider the WFQ weights) where RR and WFQ will behave exactly the same?

