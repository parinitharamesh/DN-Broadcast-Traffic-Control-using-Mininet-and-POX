# SDN Broadcast Traffic Control using Mininet and POX

## Problem Statement

The objective of this project is to control excessive broadcast traffic in a network using Software Defined Networking (SDN). Broadcast traffic can lead to unnecessary flooding and reduced network efficiency.

---

## Objective

* Detect broadcast packets in the network
* Block broadcast traffic to limit flooding
* Allow only required (non-broadcast) traffic
* Compare controlled vs normal network behavior

---

##  Tools Used

* Mininet (Network Emulator)
* POX Controller (SDN Controller)
* Ubuntu (Virtual Machine)

---

## Setup and Execution Steps

### 1. Start Controller

cd ~/pox
python3 pox.py my_controller


### 2. Start Mininet

sudo mn -c
sudo mn --controller=remote

## Testing Commands

Inside Mininet:

pingall
h1 ping h2
iperf
dpctl dump-flows

##  Test Scenarios

### Scenario 1: Broadcast Blocking (Custom Controller)

* Broadcast packets are detected and blocked
* Communication fails
* Output: **100% packet loss**

---

###  Scenario 2: Normal Network (Default Controller)

* Broadcast allowed
* Communication successful
* Output: **0% packet loss**

---

##  Results

* Blocking broadcast traffic prevents communication because ARP uses broadcast
* Normal controller allows communication and shows proper network behavior
* Throughput measured using iperf
* Latency observed using ping

---

##  SDN Logic Explanation

The controller listens for `packet_in` events.
If the destination MAC address is broadcast, the packet is dropped.
Otherwise, the packet is forwarded using OpenFlow actions.

This demonstrates **match–action logic in SDN**.

---

## Proof of Execution

Screenshots included:

* Controller running
* pingall (blocked)
* pingall (working)
* h1 ping h2
* iperf output
* Flow table

---

##  References

* Mininet Documentation
* POX Controller Documentation

---

##  Conclusion

This project demonstrates how SDN can centrally control network behavior by blocking broadcast traffic and comparing it with normal network performance.
