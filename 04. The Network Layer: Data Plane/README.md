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
