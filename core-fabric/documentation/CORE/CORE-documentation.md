# CORE

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [ISIS CLNS interfaces](#isis-clns-interfaces)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| CORE | pe | s1-core1 | 192.168.0.102/24 | cEOSLab | Provisioned | - |
| CORE | pe | s1-core2 | 192.168.0.103/24 | cEOSLab | Provisioned | - |
| CORE | pe | s2-core1 | 192.168.0.202/24 | cEOSLab | Provisioned | - |
| CORE | pe | s2-core2 | 192.168.0.203/24 | cEOSLab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| pe | s1-core1 | Ethernet1 | pe | s1-core2 | Ethernet1 |
| pe | s1-core1 | Ethernet4 | pe | s2-core1 | Ethernet4 |
| pe | s1-core1 | Ethernet6 | pe | s1-core2 | Ethernet6 |
| pe | s1-core2 | Ethernet4 | pe | s2-core2 | Ethernet4 |
| pe | s2-core1 | Ethernet1 | pe | s2-core2 | Ethernet1 |
| pe | s2-core1 | Ethernet6 | pe | s2-core2 | Ethernet6 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.255.0.0/24 | 256 | 12 | 4.69 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| s1-core1 | Ethernet1 | 10.255.0.0/31 | s1-core2 | Ethernet1 | 10.255.0.1/31 |
| s1-core1 | Ethernet4 | 10.255.0.4/31 | s2-core1 | Ethernet4 | 10.255.0.5/31 |
| s1-core1 | Ethernet6 | 10.255.0.2/31 | s1-core2 | Ethernet6 | 10.255.0.3/31 |
| s1-core2 | Ethernet4 | 10.255.0.6/31 | s2-core2 | Ethernet4 | 10.255.0.7/31 |
| s2-core1 | Ethernet1 | 10.255.0.8/31 | s2-core2 | Ethernet1 | 10.255.0.9/31 |
| s2-core1 | Ethernet6 | 10.255.0.10/31 | s2-core2 | Ethernet6 | 10.255.0.11/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.200.10.0/24 | 256 | 4 | 1.57 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| CORE | s1-core1 | 10.200.10.1/32 |
| CORE | s1-core2 | 10.200.10.2/32 |
| CORE | s2-core1 | 10.200.10.3/32 |
| CORE | s2-core2 | 10.200.10.4/32 |

### ISIS CLNS interfaces

| POD | Node | CLNS Address |
| --- | ---- | ------------ |
| CORE | s1-core1 | 49.0001.0000.0001.0001.00 |
| CORE | s1-core2 | 49.0001.0000.0001.0002.00 |
| CORE | s2-core1 | 49.0001.0000.0001.0003.00 |
| CORE | s2-core2 | 49.0001.0000.0001.0004.00 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
