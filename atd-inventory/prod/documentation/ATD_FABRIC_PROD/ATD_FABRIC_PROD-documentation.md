# ATD_FABRIC_PROD

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| ATD_FABRIC_PROD | l3leaf | s2-leaf1 | 192.168.0.22/24 | CEOS-LAB | Provisioned | - |
| ATD_FABRIC_PROD | l3leaf | s2-leaf2 | 192.168.0.23/24 | CEOS-LAB | Provisioned | - |
| ATD_FABRIC_PROD | spine | s2-spine1 | 192.168.0.20/24 | CEOS-LAB | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | s2-leaf1 | Ethernet2 | spine | s2-spine1 | Ethernet2 |
| l3leaf | s2-leaf2 | Ethernet2 | spine | s2-spine1 | Ethernet3 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 172.30.255.0/24 | 256 | 4 | 1.57 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| s2-leaf1 | Ethernet2 | 172.30.255.1/31 | s2-spine1 | Ethernet2 | 172.30.255.0/31 |
| s2-leaf2 | Ethernet2 | 172.30.255.3/31 | s2-spine1 | Ethernet3 | 172.30.255.2/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.0.255.0/24 | 256 | 3 | 1.18 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| ATD_FABRIC_PROD | s2-leaf1 | 192.0.255.3/32 |
| ATD_FABRIC_PROD | s2-leaf2 | 192.0.255.4/32 |
| ATD_FABRIC_PROD | s2-spine1 | 192.0.255.1/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 192.0.254.0/24 | 256 | 2 | 0.79 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| ATD_FABRIC_PROD | s2-leaf1 | 192.0.254.3/32 |
| ATD_FABRIC_PROD | s2-leaf2 | 192.0.254.4/32 |
