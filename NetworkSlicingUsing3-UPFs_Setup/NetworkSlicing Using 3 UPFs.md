# free5GC 5GC & UERANSIM UE / RAN Sample Configuration - Select UPF based on S-NSSAI - 3 UPF
>
> On Single Host Machine (Completely inside Virtualbox)

This describes a very simple configuration that uses free5GC and UERANSIM to select the UPF based on S-NSSAI. For 3 UPF Setup.

---
<a id="toc"></a>

## Table of Contents

- [Overview of free5GC 5GC Simulation Mobile Network](#overview)
- [Changes in configuration files of free5GC 5GC and UERANSIM UE / RAN](#changes)
  - [Changes in configuration files of free5GC 5GC C-Plane](#changes_cp)
  - [Changes in configuration files of free5GC 5GC U-Plane1](#changes_up1)
  - [Changes in configuration files of free5GC 5GC U-Plane2](#changes_up2)
  - [Changes in configuration files of UERANSIM UE / RAN](#changes_ueransim)
    - [Changes in configuration files of RAN (gNodeB)](#changes_ran)
    - [Changes in configuration files of UE[SST:1, SD:0x000001] (IMSI-001010000000000)](#changes_ue_sd1)
    - [Changes in configuration files of UE[SST:1, SD:0x000002] (IMSI-001010000000000)](#changes_ue_sd2)
- [Network settings of free5GC 5GC and UERANSIM UE / RAN](#network_settings)
  - [Network settings of free5GC 5GC C-Plane](#network_settings_cp)
  - [Network settings of free5GC 5GC U-Plane1](#network_settings_up1)
  - [Network settings of free5GC 5GC U-Plane2](#network_settings_up2)
- [Build free5GC and UERANSIM](#build)
- [Run free5GC 5GC and UERANSIM UE / RAN](#run)
  - [Run free5GC 5GC U-Plane1 & U-Plane2](#run_up)
  - [Run free5GC 5GC C-Plane](#run_cp)
  - [Run UERANSIM (gNodeB)](#run_ran)
  - [Run UERANSIM (UE[SST:1, SD:0x000001])](#run_sd1)
    - [UE connects to U-Plane1 based on SST:1 and SD:0x000001](#con_sd1)
    - [Ping google.com going through DN=10.60.0.0/16 on U-Plane1](#ping_sd1)
  - [Run UERANSIM (UE[SST:1, SD:0x000002])](#run_sd2)
    - [UE connects to U-Plane2 based on SST:1 and SD:0x000002](#con_sd2)
    - [Ping google.com going through DN=10.61.0.0/16 on U-Plane2](#ping_sd2)
- [Changelog (summary)](#changelog)

---
<a id="overview"></a>

## Overview of free5GC 5GC Simulation Mobile Network

The following minimum configuration was set as a condition.

- The UE selects a pair of SMF and UPF based on S-NSSAI.

The built simulation environment is as follows.

![Alt text](image-1.png)
The 5GC / UE / RAN used are as follows.

- 5GC - free5GC v3.2.1 (2023.02.12) - <https://github.com/free5gc/free5gc>
- UE / RAN - UERANSIM v3.2.6 (2023.03.17) - <https://github.com/aligungr/UERANSIM>

Each VMs are as follows.

| VM # | SW & Role             | IP address                                                                             | OS           | Memory (Min) | HDD (Min) |
| ---- | --------------------- | -------------------------------------------------------------------------------------- | ------------ | ------------ | --------- |
| VM1  | free5GC  5GC C-Plane  | 192.168.56.141/24 <br> 192.168.56.142/24 <br> 192.168.56.143/24 <br> 192.168.56.147/24 | Ubuntu 22.04 | 1GB          | 20GB      |
| VM2  | free5GC  5GC U-Plane1 | 192.168.56.144/24                                                                      | Ubuntu 22.04 | 1GB          | 10GB      |
| VM3  | free5GC  5GC U-Plane2 | 192.168.56.145/24                                                                      | Ubuntu 22.04 | 1GB          | 10GB      |
| VM4  | free5GC  5G U-Plane 3 | 192.168.56.146/24                                                                      | Ubuntu 22.04 | 1GB          | 10GB      |
| VM5  | UERANSIM RAN (gNodeB) | 192.168.56.131/24                                                                      | Ubuntu 22.04 | 1GB          | 10GB      |
| VM6  | UERANSIM UE           | 192.168.56.132/24                                                                      | Ubuntu 22.04 | 1GB          | 10GB      |

AMF & SMF addresses are as follows.  

| NF   | IP address     | IP address on SBI | Supported S-NSSAI                                                  |
| ---- | -------------- | ----------------- | ------------------------------------------------------------------ |
| AMF  | 192.168.56.141 | 127.0.0.18        | SST:1, SD:0x000001 <br> SST:1, SD:0x000002 <br> SST:1, SD:0x000003 |
| SMF1 | 192.168.56.142 | 127.0.0.2         | SST:1, SD:0x000001                                                 |
| SMF2 | 192.168.56.143 | 127.0.0.12        | SST:1, SD:0x000002                                                 |
| SMF3 | 192.168.56.147 | 127.0.0.22        | SST:1, SD:0x000003                                                 |

gNodeB Information (other information is default) is as follows.

| IP address | Supported S-NSSAI |
| --- | --- |
| 192.168.56.131 | SST:1, SD:0x000001 <br> SST:1, SD:0x000002 <br> SST:1, SD:0x000003 |

Subscriber Information (other information is default) is as follows.  
**Note. Please select OP or OPc according to the setting of UERANSIM UE configuration files.**

| UE | IMSI | DNN | OP/OPc | S-NSSAI |
| --- | --- | --- | --- | --- |
| UE | 001010000000000 | internet | OPc | SST:1, SD:0x000001 <br> SST:1, SD:0x000002 <br> SST:1, SD:0x000003|

I registered these information with the free5GC WebUI.
In addition, [3GPP TS 35.208](https://www.3gpp.org/DynaReport/35208.htm) "4.3 Test Sets" is published by 3GPP as test data for the 3GPP authentication and key generation functions (MILENAGE).

Each DNs are as follows.

| DN           | S-NSSAI                | TUNnel interface of DN | DNN      | TUNnel interface of UE | U-Plane # |
| ------------ | ---------------------- | ---------------------- | -------- | ---------------------- | --------- |
| 10.60.0.0/16 | SST:1 <br> SD:0x000001 | upfgtp                 | internet | uesimtun0              | U-Plane1  |
| 10.61.0.0/16 | SST:1 <br> SD:0x000002 | upfgtp                 | internet | uesimtun0              | U-Plane2  |
| 10.62.0.0/16 | SST:1 <br> SD:0x000003 | upfgtp                 | internet | uesimtun0              | U-Plane3  |

<a id="changes"></a>

## Changes in configuration files of free5GC 5GC and UERANSIM UE / RAN

Please refer to the following for building free5GC and UERANSIM respectively.

- free5GC v3.2.1 (2023.02.12) - <https://free5gc.org/guide/>
- UERANSIM v3.2.6 (2023.03.17) - <https://github.com/aligungr/UERANSIM/wiki/Installation>

<a id="changes_cp"></a>

### Changes in configuration files of free5GC 5GC C-Plane

- `free5gc/config/amfcfg.yaml`

```yaml
info:
  version: 1.0.3
  description: AMF initial local configuration

configuration:
  amfName: AMF # the name of this AMF
  ngapIpList:  # the IP list of N2 interfaces on this AMF
    - 192.168.56.141 #127.0.0.18
  sbi: # Service-based interface information
    scheme: http # the protocol for sbi (http or https)
    registerIPv4: 127.0.0.18 # IP used to register to NRF
    bindingIPv4: 127.0.0.18  # IP used to bind the service
    port: 8000 # port used to bind the service
    tls: # the local path of TLS key
      pem: config/TLS/amf.pem # AMF TLS Certificate
      key: config/TLS/amf.key # AMF TLS Private key
  serviceNameList: # the SBI services provided by this AMF, refer to TS 29.518
    - namf-comm # Namf_Communication service
    - namf-evts # Namf_EventExposure service
    - namf-mt   # Namf_MT service
    - namf-loc  # Namf_Location service
    - namf-oam  # OAM service
  servedGuamiList: # Guami (Globally Unique AMF ID) list supported by this AMF
    # <GUAMI> = <MCC><MNC><AMF ID>
    - plmnId: # Public Land Mobile Network ID, <PLMN ID> = <MCC><MNC>
        mcc: 208 # Mobile Country Code (3 digits string, digit: 0~9)
        mnc: 93 # Mobile Network Code (2 or 3 digits string, digit: 0~9)
      amfId: cafe00 # AMF identifier (3 bytes hex string, range: 000000~FFFFFF)
  supportTaiList:  # the TAI (Tracking Area Identifier) list supported by this AMF
    - plmnId: # Public Land Mobile Network ID, <PLMN ID> = <MCC><MNC>
        mcc: 208 # Mobile Country Code (3 digits string, digit: 0~9)
        mnc: 93 # Mobile Network Code (2 or 3 digits string, digit: 0~9)
      tac: 1 # Tracking Area Code (uinteger, range: 0~16777215)
  plmnSupportList: # the PLMNs (Public land mobile network) list supported by this AMF
    - plmnId: # Public Land Mobile Network ID, <PLMN ID> = <MCC><MNC>
        mcc: 208 # Mobile Country Code (3 digits string, digit: 0~9)
        mnc: 93 # Mobile Network Code (2 or 3 digits string, digit: 0~9)
      snssaiList: # the S-NSSAI (Single Network Slice Selection Assistance Information) list supported by this AMF
        - sst: 1 # Slice/Service Type (uinteger, range: 0~255)
          sd: 000001 # Slice Differentiator (3 bytes hex string, range: 000000~FFFFFF)
        - sst: 1 # Slice/Service Type (uinteger, range: 0~255)
          sd: 000002
        - sst: 1
          sd: 000003 # Slice Differentiator (3 bytes hex string, range: 000000~FFFFFF)
  supportDnnList:  # the DNN (Data Network Name) list supported by this AMF
    - internet
  nrfUri: http://127.0.0.10:8000 # a valid URI of NRF
  security:  # NAS security parameters
    integrityOrder: # the priority of integrity algorithms
      - NIA2
      # - NIA0
    cipheringOrder: # the priority of ciphering algorithms
      - NEA0
      # - NEA2
  networkName:  # the name of this core network
    full: free5GC
    short: free
  locality: area1 # Name of the location where a set of AMF, SMF and UPFs are located
  networkFeatureSupport5GS: # 5gs Network Feature Support IE, refer to TS 24.501
    enable: true # append this IE in Registration accept or not
    length: 1 # IE content length (uinteger, range: 1~3)
    imsVoPS: 0 # IMS voice over PS session indicator (uinteger, range: 0~1)
    emc: 0 # Emergency service support indicator for 3GPP access (uinteger, range: 0~3)
    emf: 0 # Emergency service fallback indicator for 3GPP access (uinteger, range: 0~3)
    iwkN26: 0 # Interworking without N26 interface indicator (uinteger, range: 0~1)
    mpsi: 0 # MPS indicator (uinteger, range: 0~1)
    emcN3: 0 # Emergency service support indicator for Non-3GPP access (uinteger, range: 0~1)
    mcsi: 0 # MCS indicator (uinteger, range: 0~1)
  t3502Value: 720  # timer value (seconds) at UE side
  t3512Value: 3600 # timer value (seconds) at UE side
  non3gppDeregistrationTimerValue: 3240 # timer value (seconds) at UE side
  # retransmission timer for paging message
  t3513:
    enable: true     # true or false
    expireTime: 6s   # default is 6 seconds
    maxRetryTimes: 4 # the max number of retransmission
  # retransmission timer for NAS Deregistration Request message
  t3522:
    enable: true     # true or false
    expireTime: 6s   # default is 6 seconds
    maxRetryTimes: 4 # the max number of retransmission
  # retransmission timer for NAS Registration Accept message
  t3550:
    enable: true     # true or false
    expireTime: 6s   # default is 6 seconds
    maxRetryTimes: 4 # the max number of retransmission
  # retransmission timer for NAS Authentication Request/Security Mode Command message
  t3560:
    enable: true     # true or false
    expireTime: 6s   # default is 6 seconds
    maxRetryTimes: 4 # the max number of retransmission
  # retransmission timer for NAS Notification message
  t3565:
    enable: true     # true or false
    expireTime: 6s   # default is 6 seconds
    maxRetryTimes: 4 # the max number of retransmission
  # retransmission timer for NAS Identity Request message
  t3570:
    enable: true     # true or false
    expireTime: 6s   # default is 6 seconds
    maxRetryTimes: 4 # the max number of retransmission

# the kind of log output
# debugLevel: how detailed to output, value: trace, debug, info, warn, error, fatal, panic
# ReportCaller: enable the caller report or not, value: true or false
logger:
  AMF:
    debugLevel: info
    ReportCaller: false
  NAS:
    debugLevel: info
    ReportCaller: false
  FSM:
    debugLevel: info
    ReportCaller: false
  NGAP:
    debugLevel: info
    ReportCaller: false
  Aper:
    debugLevel: info
    ReportCaller: false

```

- `free5gc/config/smfcfg1.yaml`

```yaml
info:
  version: 1.0.2
  description: SMF initial local configuration

configuration:
  smfName: SMF # the name of this SMF
  sbi: # Service-based interface information
    scheme: http # the protocol for sbi (http or https)
    registerIPv4: 127.0.0.2 # IP used to register to NRF
    bindingIPv4: 127.0.0.2  # IP used to bind the service
    port: 8000 # Port used to bind the service
    tls: # the local path of TLS key
      key: config/TLS/smf.key # SMF TLS Certificate
      pem: config/TLS/smf.pem # SMF TLS Private key
  serviceNameList: # the SBI services provided by this SMF, refer to TS 29.502
    - nsmf-pdusession # Nsmf_PDUSession service
    - nsmf-event-exposure # Nsmf_EventExposure service
    - nsmf-oam # OAM service
  snssaiInfos: # the S-NSSAI (Single Network Slice Selection Assistance Information) list supported by this AMF
    - sNssai: # S-NSSAI (Single Network Slice Selection Assistance Information)
        sst: 1 # Slice/Service Type (uinteger, range: 0~255)
        sd: 000001 # Slice Differentiator (3 bytes hex string, range: 000000~FFFFFF)
      dnnInfos: # DNN information list
        - dnn: internet # Data Network Name
          dns: # the IP address of DNS
            ipv4: 8.8.8.8
  plmnList: # the list of PLMN IDs that this SMF belongs to (optional, remove this key when unnecessary)
    - mcc: "208" # Mobile Country Code (3 digits string, digit: 0~9)
      mnc: "93" # Mobile Network Code (2 or 3 digits string, digit: 0~9)
  locality: area1 # Name of the location where a set of AMF, SMF and UPFs are located
  pfcp: # the IP address of N4 interface on this SMF (PFCP)
    addr: 192.168.56.142 #127.0.0.1
  userplaneInformation: # list of userplane information
    upNodes: # information of userplane node (AN or UPF)
      gNB1: # the name of the node
        type: AN # the type of the node (AN or UPF)
      UPF:  # the name of the node
        type: UPF # the type of the node (AN or UPF)
        nodeID: 192.168.56.144 #127.0.0.8 # the IP/FQDN of N4 interface on this UPF (PFCP)
        sNssaiUpfInfos: # S-NSSAI information list for this UPF
          - sNssai: # S-NSSAI (Single Network Slice Selection Assistance Information)
              sst: 1 # Slice/Service Type (uinteger, range: 0~255)
              sd: 000001 # Slice Differentiator (3 bytes hex string, range: 000000~FFFFFF)
            dnnUpfInfoList: # DNN information list for this S-NSSAI
              - dnn: internet
                pools:
                  - cidr: 10.60.0.0/16
        interfaces: # Interface list for this UPF
          - interfaceType: N3 # the type of the interface (N3 or N9)
            endpoints: # the IP address of this N3/N9 interface on this UPF
              - 192.168.56.144 #127.0.0.8
            networkInstance: internet # Data Network Name (DNN)
    links: # the topology graph of userplane, A and B represent the two nodes of each link
      - A: gNB1
        B: UPF
  nrfUri: http://127.0.0.10:8000 # a valid URI of NRF
  ulcl: false
# the kind of log output
# debugLevel: how detailed to output, value: trace, debug, info, warn, error, fatal, panic
# ReportCaller: enable the caller report or not, value: true or false
logger:
  SMF:
    debugLevel: info
    ReportCaller: false
  NAS:
    debugLevel: info
    ReportCaller: false
  NGAP:
    debugLevel: info
    ReportCaller: false
  Aper:
    debugLevel: info
    ReportCaller: false
  PFCP:
    debugLevel: info
    ReportCaller: false

```

- `free5gc/config/smfcfg2.yaml`

```yaml
info:
  version: 1.0.2
  description: SMF initial local configuration

configuration:
  smfName: SMF # the name of this SMF
  sbi: # Service-based interface information
    scheme: http # the protocol for sbi (http or https)
    registerIPv4: 127.0.0.12 # IP used to register to NRF
    bindingIPv4: 127.0.0.12  # IP used to bind the service
    port: 8000 # Port used to bind the service
    tls: # the local path of TLS key
      key: config/TLS/smf.key # SMF TLS Certificate
      pem: config/TLS/smf.pem # SMF TLS Private key
  serviceNameList: # the SBI services provided by this SMF, refer to TS 29.502
    - nsmf-pdusession # Nsmf_PDUSession service
    - nsmf-event-exposure # Nsmf_EventExposure service
    - nsmf-oam # OAM service
  snssaiInfos: # the S-NSSAI (Single Network Slice Selection Assistance Information) list supported by this AMF
    - sNssai: # S-NSSAI (Single Network Slice Selection Assistance Information)
        sst: 1 # Slice/Service Type (uinteger, range: 0~255)
        sd: 000002 # Slice Differentiator (3 bytes hex string, range: 000000~FFFFFF)
      dnnInfos: # DNN information list
        - dnn: internet # Data Network Name
          dns: # the IP address of DNS
            ipv4: 8.8.8.8
  plmnList: # the list of PLMN IDs that this SMF belongs to (optional, remove this key when unnecessary)
    - mcc: "208" # Mobile Country Code (3 digits string, digit: 0~9)
      mnc: "93" # Mobile Network Code (2 or 3 digits string, digit: 0~9)
  locality: area1 # Name of the location where a set of AMF, SMF and UPFs are located
  pfcp: # the IP address of N4 interface on this SMF (PFCP)
    addr: 192.168.56.143 #127.0.0.1
  userplaneInformation: # list of userplane information
    upNodes: # information of userplane node (AN or UPF)
      gNB1: # the name of the node
        type: AN # the type of the node (AN or UPF)
      UPF:  # the name of the node
        type: UPF # the type of the node (AN or UPF)
        nodeID: 192.168.56.145 #127.0.0.8 # the IP/FQDN of N4 interface on this UPF (PFCP)
        sNssaiUpfInfos: # S-NSSAI information list for this UPF
          - sNssai: # S-NSSAI (Single Network Slice Selection Assistance Information)
              sst: 1 # Slice/Service Type (uinteger, range: 0~255)
              sd: 000002 # Slice Differentiator (3 bytes hex string, range: 000000~FFFFFF)
            dnnUpfInfoList: # DNN information list for this S-NSSAI
              - dnn: internet
                pools:
                  - cidr: 10.61.0.0/16
        interfaces: # Interface list for this UPF
          - interfaceType: N3 # the type of the interface (N3 or N9)
            endpoints: # the IP address of this N3/N9 interface on this UPF
              - 192.168.56.145 #127.0.0.8
            networkInstance: internet # Data Network Name (DNN)
    links: # the topology graph of userplane, A and B represent the two nodes of each link
      - A: gNB1
        B: UPF
  nrfUri: http://127.0.0.10:8000 # a valid URI of NRF
  ulcl: false
# the kind of log output
# debugLevel: how detailed to output, value: trace, debug, info, warn, error, fatal, panic
# ReportCaller: enable the caller report or not, value: true or false
logger:
  SMF:
    debugLevel: info
    ReportCaller: false
  NAS:
    debugLevel: info
    ReportCaller: false
  NGAP:
    debugLevel: info
    ReportCaller: false
  Aper:
    debugLevel: info
    ReportCaller: false
  PFCP:
    debugLevel: info
    ReportCaller: false

```

- `free5gc/config/smfcfg3.yaml`

```yaml
info:
  version: 1.0.2
  description: SMF initial local configuration

configuration:
  smfName: SMF # the name of this SMF
  sbi: # Service-based interface information
    scheme: http # the protocol for sbi (http or https)
    registerIPv4: 127.0.0.22 # IP used to register to NRF
    bindingIPv4: 127.0.0.22  # IP used to bind the service
    port: 8000 # Port used to bind the service
    tls: # the local path of TLS key
      key: config/TLS/smf.key # SMF TLS Certificate
      pem: config/TLS/smf.pem # SMF TLS Private key
  serviceNameList: # the SBI services provided by this SMF, refer to TS 29.502
    - nsmf-pdusession # Nsmf_PDUSession service
    - nsmf-event-exposure # Nsmf_EventExposure service
    - nsmf-oam # OAM service
  snssaiInfos: # the S-NSSAI (Single Network Slice Selection Assistance Information) list supported by this AMF
    - sNssai: # S-NSSAI (Single Network Slice Selection Assistance Information)
        sst: 1 # Slice/Service Type (uinteger, range: 0~255)
        sd: 000003 # Slice Differentiator (3 bytes hex string, range: 000000~FFFFFF)
      dnnInfos: # DNN information list
        - dnn: internet # Data Network Name
          dns: # the IP address of DNS
            ipv4: 8.8.8.8
  plmnList: # the list of PLMN IDs that this SMF belongs to (optional, remove this key when unnecessary)
    - mcc: "208" # Mobile Country Code (3 digits string, digit: 0~9)
      mnc: "93" # Mobile Network Code (2 or 3 digits string, digit: 0~9)
  locality: area1 # Name of the location where a set of AMF, SMF and UPFs are located
  pfcp: # the IP address of N4 interface on this SMF (PFCP)
    addr: 192.168.56.147 #127.0.0.1
  userplaneInformation: # list of userplane information
    upNodes: # information of userplane node (AN or UPF)
      gNB1: # the name of the node
        type: AN # the type of the node (AN or UPF)
      UPF:  # the name of the node
        type: UPF # the type of the node (AN or UPF)
        nodeID: 192.168.56.146 #127.0.0.8 # the IP/FQDN of N4 interface on this UPF (PFCP)
        sNssaiUpfInfos: # S-NSSAI information list for this UPF
          - sNssai: # S-NSSAI (Single Network Slice Selection Assistance Information)
              sst: 1 # Slice/Service Type (uinteger, range: 0~255)
              sd: 000003 # Slice Differentiator (3 bytes hex string, range: 000000~FFFFFF)
            dnnUpfInfoList: # DNN information list for this S-NSSAI
              - dnn: internet
                pools:
                  - cidr: 10.62.0.0/16
        interfaces: # Interface list for this UPF
          - interfaceType: N3 # the type of the interface (N3 or N9)
            endpoints: # the IP address of this N3/N9 interface on this UPF
              - 192.168.56.146 #127.0.0.8
            networkInstance: internet # Data Network Name (DNN)
    links: # the topology graph of userplane, A and B represent the two nodes of each link
      - A: gNB1
        B: UPF
  nrfUri: http://127.0.0.10:8000 # a valid URI of NRF
  ulcl: false
# the kind of log output
# debugLevel: how detailed to output, value: trace, debug, info, warn, error, fatal, panic
# ReportCaller: enable the caller report or not, value: true or false
logger:
  SMF:
    debugLevel: info
    ReportCaller: false
  NAS:
    debugLevel: info
    ReportCaller: false
  NGAP:
    debugLevel: info
    ReportCaller: false
  Aper:
    debugLevel: info
    ReportCaller: false
  PFCP:
    debugLevel: info
    ReportCaller: false

```

- `free5gc/config/ausfcfg.yaml`

```yaml
info:
  version: 1.0.2
  description: AUSF initial local configuration

configuration:
  sbi: # Service-based interface information
    scheme: http # the protocol for sbi (http or https)
    registerIPv4: 127.0.0.9 # IP used to register to NRF
    bindingIPv4: 127.0.0.9  # IP used to bind the service
    port: 8000 # Port used to bind the service
    tls: # the local path of TLS key
      pem: config/TLS/ausf.pem # AUSF TLS Certificate
      key: config/TLS/ausf.key # AUSF TLS Private key
  serviceNameList: # the SBI services provided by this AUSF, refer to TS 29.509
    - nausf-auth # Nausf_UEAuthentication service
  nrfUri: http://127.0.0.10:8000 # a valid URI of NRF
  plmnSupportList: # the PLMNs (Public Land Mobile Network) list supported by this AUSF
    - mcc: 208 # Mobile Country Code (3 digits string, digit: 0~9)
      mnc: 93  # Mobile Network Code (2 or 3 digits string, digit: 0~9)
  groupId: ausfGroup001 # ID for the group of the AUSF
  eapAkaSupiImsiPrefix: false # including "imsi-" prefix or not when using the SUPI to do EAP-AKA' authentication

# the kind of log output
# debugLevel: how detailed to output, value: trace, debug, info, warn, error, fatal, panic
# ReportCaller: enable the caller report or not, value: true or false
logger:
  AUSF:
    debugLevel: info
    ReportCaller: false

```

- `free5gc/config/nrfcfg.yaml`

```diff
info:
  version: 1.0.1
  description: NRF initial local configuration

configuration:
  MongoDBName: free5gc # database name in MongoDB
  MongoDBUrl: mongodb://127.0.0.1:27017 # a valid URL of the mongodb
  sbi: # Service-based interface information
    scheme: http # the protocol for sbi (http or https)
    registerIPv4: 127.0.0.10 # IP used to serve NFs or register to another NRF
    bindingIPv4: 127.0.0.10  # IP used to bind the service
    port: 8000 # port used to bind the service
    tls: # the local path of TLS key
      pem: config/TLS/nrf.pem # NRF TLS Certificate
      key: config/TLS/nrf.key # NRF TLS Private key
  DefaultPlmnId:
    mcc: 208 # Mobile Country Code (3 digits string, digit: 0~9)
    mnc: 93 # Mobile Network Code (2 or 3 digits string, digit: 0~9)
  serviceNameList: # the SBI services provided by this NRF, refer to TS 29.510
    - nnrf-nfm # Nnrf_NFManagement service
    - nnrf-disc # Nnrf_NFDiscovery service

# the kind of log output
# debugLevel: how detailed to output, value: trace, debug, info, warn, error, fatal, panic
# ReportCaller: enable the caller report or not, value: true or false
logger:
  NRF:
    debugLevel: info
    ReportCaller: false

```

- `free5gc/config/nssfcfg.yaml`

```yaml
info:
  version: 1.0.1
  description: NSSF initial local configuration

configuration:
  nssfName: NSSF # the name of this NSSF
  sbi: # Service-based interface information
    scheme: http # the protocol for sbi (http or https)
    registerIPv4: 127.0.0.31 # IP used to register to NRF
    bindingIPv4: 127.0.0.31  # IP used to bind the service
    port: 8000 # Port used to bind the service
    tls: # the local path of TLS key
      pem: config/TLS/nssf.pem # NSSF TLS Certificate
      key: config/TLS/nssf.key # NSSF TLS Private key
  serviceNameList: # the SBI services provided by this SMF, refer to TS 29.531
    - nnssf-nsselection # Nnssf_NSSelection service
    - nnssf-nssaiavailability # Nnssf_NSSAIAvailability service
  nrfUri: http://127.0.0.10:8000 # a valid URI of NRF
  supportedPlmnList: # the PLMNs (Public land mobile network) list supported by this NSSF
    - mcc: 208 # Mobile Country Code (3 digits string, digit: 0~9)
      mnc: 93 # Mobile Network Code (2 or 3 digits string, digit: 0~9)
  supportedNssaiInPlmnList: # Supported S-NSSAI List for each PLMN
    - plmnId: # Public Land Mobile Network ID, <PLMN ID> = <MCC><MNC>
        mcc: 208 # Mobile Country Code (3 digits string, digit: 0~9)
        mnc: 93 # Mobile Network Code (2 or 3 digits string, digit: 0~9)
      supportedSnssaiList: # Supported S-NSSAIs of the PLMN
        - sst: 1 # Slice/Service Type (uinteger, range: 0~255)
          sd: 000001 # Slice Differentiator (3 bytes hex string, range: 000000~FFFFFF)
        - sst: 1 # Slice/Service Type (uinteger, range: 0~255)
          sd: 000002
        - sst: 1
          sd: 000003 # Slice Differentiator (3 bytes hex string, range: 000000~FFFFFF)
  nsiList: # List of available Network Slice Instance (NSI)
    - snssai: # S-NSSAI of this NSI
        sst: 1 # Slice/Service Type (uinteger, range: 0~255)
        sd: 000001
      nsiInformationList: # Information list of this NSI
        # the NRF to be used to select the NFs/services within the selected NSI, and an optonal ID
        - nrfId: http://127.0.0.10:8000/nnrf-nfm/v1/nf-instances
          nsiId: 1
    - snssai: # S-NSSAI of this NSI
        sst: 1 # Slice/Service Type (uinteger, range: 0~255)
        sd: 000002 # Slice Differentiator (3 bytes hex string, range: 000000~FFFFFF)
      nsiInformationList: # Information list of this NSI
        # the NRF to be used to select the NFs/services within the selected NSI, and an optonal ID
        - nrfId: http://127.0.0.10:8000/nnrf-nfm/v1/nf-instances
          nsiId: 2
    - snssai:
        sst: 1
        sd: 000003
      nsiInformationList:

        - nrfId: http://127.0.0.10:8000/nnrf-nfm/v1/nf-instances
          nsiId: 3
  amfSetList: # List of AMF Sets that my be assigned by this NSSF
    - amfSetId: 1 # the AMF Set identifier
      amfList: # Instance ID of the AMFs in this set
      # URI of the NRF used to determine the list of candidate AMF(s) from the AMF Set
      nrfAmfSet: http://127.0.0.10:8000/nnrf-nfm/v1/nf-instances
      # the Nssai availability data information per TA supported by the AMF
      supportedNssaiAvailabilityData:
        - tai: # Tracking Area Identifier
            plmnId: # Public Land Mobile Network ID, <PLMN ID> = <MCC><MNC>
              mcc: 208 # Mobile Country Code (3 digits string, digit: 0~9)
              mnc: 93 # Mobile Network Code (2 or 3 digits string, digit: 0~9)
            tac: 1 # Tracking Area Code (uinteger, range: 0~16777215)
          supportedSnssaiList: # Supported S-NSSAIs of the tracking area
            - sst: 1 # Slice/Service Type (uinteger, range: 0~255)
              sd: 000001 # Slice Differentiator (3 bytes hex string, range: 000000~FFFFFF)
            - sst: 1 # Slice/Service Type (uinteger, range: 0~255)
              sd: 000002
            - sst: 1
              sd: 000003 # Slice Differentiator (3 bytes hex string, range: 000000~FFFFFF)
  taList: # List of supported tracking area and their related information of this NSSF instance
    - tai: # Tracking Area Identity
        plmnId: # Public Land Mobile Network ID, <PLMN ID> = <MCC><MNC>
          mcc: 208 # Mobile Country Code (3 digits string, digit: 0~9)
          mnc: 93 # Mobile Network Code (2 or 3 digits string, digit: 0~9)
        tac: 1 # Tracking Area Code (uinteger, range: 0~16777215)
      accessType: 3GPP_ACCESS # Access type of the tracking area
      supportedSnssaiList: # List of supported S-NSSAIs of the tracking area
        - sst: 1 # Slice/Service Type (uinteger, range: 0~255)
          sd: 000001 # Slice Differentiator (3 bytes hex string, range: 000000~FFFFFF)
        - sst: 1 # Slice/Service Type (uinteger, range: 0~255)
          sd: 000002
        - sst: 1
          sd: 000003 # Slice Differentiator (3 bytes hex string, range: 000000~FFFFFF)

# the kind of log output
# debugLevel: how detailed to output, value: trace, debug, info, warn, error, fatal, panic
# ReportCaller: enable the caller report or not, value: true or false
logger:
  NSSF:
    debugLevel: info
    ReportCaller: false

```

<a id="changes_up1"></a>

### Changes in configuration files of free5GC 5GC U-Plane1

- `free5gc/config/upfcfg.yaml`

```diff
version: 1.0.3
description: UPF initial local configuration

# The listen IP and nodeID of the N4 interface on this UPF (Can't set to 0.0.0.0)
pfcp:
  addr: 192.168.56.144 #127.0.0.8   # IP addr for listening
  nodeID: 192.168.56.144 # 127.0.0.8 # External IP or FQDN can be reached
  retransTimeout: 1s # retransmission timeout
  maxRetrans: 3 # the max number of retransmission

gtpu:
  forwarder: gtp5g
  # The IP list of the N3/N9 interfaces on this UPF
  # If there are multiple connection, set addr to 0.0.0.0 or list all the addresses
  ifList:
    - addr: 192.168.56.144 #127.0.0.8
      type: N3
      # name: upf.5gc.nctu.me
      # ifname: gtpif

# The DNN list supported by UPF
dnnList:
  - dnn: internet # Data Network Name
    cidr: 10.60.0.0/16 # Classless Inter-Domain Routing for assigned IPv4 pool of UE
    # natifname: eth0

logger: # log output setting
  enable: true # true or false
  level: info # how detailed to output, value: trace, debug, info, warn, error, fatal, panic
  reportCaller: false # enable the caller report or not, value: true or false

```

<a id="changes_up2"></a>

### Changes in configuration files of free5GC 5GC U-Plane2

- `free5gc/config/upfcfg.yaml`

```diff
version: 1.0.3
description: UPF initial local configuration

# The listen IP and nodeID of the N4 interface on this UPF (Can't set to 0.0.0.0)
pfcp:
  addr: 192.168.56.145 #127.0.0.8   # IP addr for listening
  nodeID: 192.168.56.145 #127.0.0.8 # External IP or FQDN can be reached
  retransTimeout: 1s # retransmission timeout
  maxRetrans: 3 # the max number of retransmission

gtpu:
  forwarder: gtp5g
  # The IP list of the N3/N9 interfaces on this UPF
  # If there are multiple connection, set addr to 0.0.0.0 or list all the addresses
  ifList:
    - addr: 192.168.56.145 #127.0.0.8
      type: N3
      # name: upf.5gc.nctu.me
      # ifname: gtpif

# The DNN list supported by UPF
dnnList:
  - dnn: internet # Data Network Name
    cidr: 10.61.0.0/16 # Classless Inter-Domain Routing for assigned IPv4 pool of UE
    # natifname: eth0

logger: # log output setting
  enable: true # true or false
  level: info # how detailed to output, value: trace, debug, info, warn, error, fatal, panic
  reportCaller: false # enable the caller report or not, value: true or false

```

### Changes in configuration files of free5GC 5GC U-Plane3

- `free5gc/config/upfcfg.yaml`

```yaml
version: 1.0.3
description: UPF initial local configuration

# The listen IP and nodeID of the N4 interface on this UPF (Can't set to 0.0.0.0)
pfcp:
  addr: 192.168.56.146 #127.0.0.8   # IP addr for listening
  nodeID: 192.168.56.146 #127.0.0.8 # External IP or FQDN can be reached
  retransTimeout: 1s # retransmission timeout
  maxRetrans: 3 # the max number of retransmission

gtpu:
  forwarder: gtp5g
  # The IP list of the N3/N9 interfaces on this UPF
  # If there are multiple connection, set addr to 0.0.0.0 or list all the addresses
  ifList:
    - addr: 192.168.56.146 #127.0.0.8
      type: N3
      # name: upf.5gc.nctu.me
      # ifname: gtpif

# The DNN list supported by UPF
dnnList:
  - dnn: internet # Data Network Name
    cidr: 10.62.0.0/16 # Classless Inter-Domain Routing for assigned IPv4 pool of UE
    # natifname: eth0

logger: # log output setting
  enable: true # true or false
  level: info # how detailed to output, value: trace, debug, info, warn, error, fatal, panic
  reportCaller: false # enable the caller report or not, value: true or false

```

<a id="changes_ueransim"></a>

### Changes in configuration files of UERANSIM UE / RAN

<a id="changes_ran"></a>

#### Changes in configuration files of RAN (gNodeB)

- `UERANSIM/config/free5gc-gnb.yaml`

```diff
mcc: '208'          # Mobile Country Code value
mnc: '93'           # Mobile Network Code value (2 or 3 digits)

nci: '0x000000010'  # NR Cell Identity (36-bit)
idLength: 32        # NR gNB ID length in bits [22...32]
tac: 1              # Tracking Area Code

linkIp: 192.168.56.131 #127.0.0.1   # gNB's local IP address for Radio Link Simulation (Usually same with local IP)
ngapIp: 192.168.56.131 #127.0.0.1   # gNB's local IP address for N2 Interface (Usually same with local IP)
gtpIp: 192.168.56.131 #127.0.0.1    # gNB's local IP address for N3 Interface (Usually same with local IP)

# List of AMF address information
amfConfigs:
  - address: 192.168.56.141 #127.0.0.1
    port: 38412

# List of supported S-NSSAIs by this gNB
slices:
  - sst: 1
    sd: 0x000003
  - sst: 1
    sd: 0x000002
  - sst: 1
    sd: 0x000001

# Indicates whether or not SCTP stream number errors should be ignored.
ignoreStreamIds: true

```

<a id="changes_ue_sd1"></a>

#### Changes in configuration files of UE[SST:1, SD:0x000001] (IMSI-001010000000000)

- `UERANSIM/config/free5gc-ue-sd1.yaml`

```diff
# IMSI number of the UE. IMSI = [MCC|MNC|MSISDN] (In total 15 digits)
supi: 'imsi-208930000000003'
# Mobile Country Code value of HPLMN
mcc: '208'
# Mobile Network Code value of HPLMN (2 or 3 digits)
mnc: '93'
# SUCI Protection Scheme : 0 for Null-scheme, 1 for Profile A and 2 for Profile B
protectionScheme: 0
# Home Network Public Key for protecting with SUCI Profile A
homeNetworkPublicKey: '5a8d38864820197c3394b92613b20b91633cbd897119273bf8e4a6f4eec0a650'
# Home Network Public Key ID for protecting with SUCI Profile A
homeNetworkPublicKeyId: 1
# Routing Indicator
routingIndicator: '0000'

# Permanent subscription key
key: '8baf473f2f8fd09487cccbd7097c6862'
# Operator code (OP or OPC) of the UE
op: '8e27b6af0e692e750f32667a3b14605d'
# This value specifies the OP type and it can be either 'OP' or 'OPC'
opType: 'OPC'
# Authentication Management Field (AMF) value
amf: '8000'
# IMEI number of the device. It is used if no SUPI is provided
imei: '356938035643803'
# IMEISV number of the device. It is used if no SUPI and IMEI is provided
imeiSv: '4370816125816151'

# List of gNB IP addresses for Radio Link Simulation
gnbSearchList:
  - 192.168.56.131 #127.0.0.1

# UAC Access Identities Configuration
uacAic:
  mps: false
  mcs: false

#uacAic:
#  - type: 'IPv4'
#    apn: 'internet'
#    slice:
#      sst: 1
#      sd: 0x000001

# UAC Access Control Class
uacAcc:
  normalClass: 0
  class11: false
  class12: false
  class13: false
  class14: false
  class15: false

# Initial PDU sessions to be established
sessions:
  - type: 'IPv4'
    apn: 'internet'
    slice:
      sst: 1
      sd: 0x000001

# Configured NSSAI for this UE by HPLMN
configured-nssai:
  - sst: 1
    sd: 0x000001

# Default Configured NSSAI for this UE
default-nssai:
  - sst: 1
    sd: 0x000001

# Supported integrity algorithms by this UE
integrity:
  IA1: true
  IA2: true
  IA3: true

# Supported encryption algorithms by this UE
ciphering:
  EA1: true
  EA2: true
  EA3: true

# Integrity protection maximum data rate for user plane
integrityMaxRate:
  uplink: 'full'
  downlink: 'full'

```

<a id="changes_ue_sd2"></a>

#### Changes in configuration files of UE[SST:1, SD:0x000002] (IMSI-001010000000000)

- `UERANSIM/config/free5gc-ue-sd2.yaml`

```diff
# IMSI number of the UE. IMSI = [MCC|MNC|MSISDN] (In total 15 digits)
supi: 'imsi-208930000000003'
# Mobile Country Code value of HPLMN
mcc: '208'
# Mobile Network Code value of HPLMN (2 or 3 digits)
mnc: '93'
# SUCI Protection Scheme : 0 for Null-scheme, 1 for Profile A and 2 for Profile B
protectionScheme: 0
# Home Network Public Key for protecting with SUCI Profile A
homeNetworkPublicKey: '5a8d38864820197c3394b92613b20b91633cbd897119273bf8e4a6f4eec0a650'
# Home Network Public Key ID for protecting with SUCI Profile A
homeNetworkPublicKeyId: 1
# Routing Indicator
routingIndicator: '0000'

# Permanent subscription key
key: '8baf473f2f8fd09487cccbd7097c6862'
# Operator code (OP or OPC) of the UE
op: '8e27b6af0e692e750f32667a3b14605d'
# This value specifies the OP type and it can be either 'OP' or 'OPC'
opType: 'OPC'
# Authentication Management Field (AMF) value
amf: '8000'
# IMEI number of the device. It is used if no SUPI is provided
imei: '356938035643803'
# IMEISV number of the device. It is used if no SUPI and IMEI is provided
imeiSv: '4370816125816151'

# List of gNB IP addresses for Radio Link Simulation
gnbSearchList:
  - 192.168.56.131 #127.0.0.1

# UAC Access Identities Configuration
uacAic:
  mps: false
  mcs: false

#uacAic:
#  - type: 'IPv4'
#    apn: 'internet'
#    slice:
#      sst: 1
#      sd: 0x000002

# UAC Access Control Class
uacAcc:
  normalClass: 0
  class11: false
  class12: false
  class13: false
  class14: false
  class15: false

# Initial PDU sessions to be established
sessions:
  - type: 'IPv4'
    apn: 'internet'
    slice:
      sst: 1
      sd: 0x000002

# Configured NSSAI for this UE by HPLMN
configured-nssai:
  - sst: 1
    sd: 0x000002

# Default Configured NSSAI for this UE
default-nssai:
  - sst: 1
    sd: 0x000002

# Supported integrity algorithms by this UE
integrity:
  IA1: true
  IA2: true
  IA3: true

# Supported encryption algorithms by this UE
ciphering:
  EA1: true
  EA2: true
  EA3: true

# Integrity protection maximum data rate for user plane
integrityMaxRate:
  uplink: 'full'
  downlink: 'full'

```

#### Changes in configuration files of UE[SST:1, SD:0x000003] (IMSI-001010000000000)

- `UERANSIM/config/free5gc-ue-sd3.yaml`

```yaml
# IMSI number of the UE. IMSI = [MCC|MNC|MSISDN] (In total 15 digits)
supi: 'imsi-208930000000003'
# Mobile Country Code value of HPLMN
mcc: '208'
# Mobile Network Code value of HPLMN (2 or 3 digits)
mnc: '93'
# SUCI Protection Scheme : 0 for Null-scheme, 1 for Profile A and 2 for Profile B
protectionScheme: 0
# Home Network Public Key for protecting with SUCI Profile A
homeNetworkPublicKey: '5a8d38864820197c3394b92613b20b91633cbd897119273bf8e4a6f4eec0a650'
# Home Network Public Key ID for protecting with SUCI Profile A
homeNetworkPublicKeyId: 1
# Routing Indicator
routingIndicator: '0000'

# Permanent subscription key
key: '8baf473f2f8fd09487cccbd7097c6862'
# Operator code (OP or OPC) of the UE
op: '8e27b6af0e692e750f32667a3b14605d'
# This value specifies the OP type and it can be either 'OP' or 'OPC'
opType: 'OPC'
# Authentication Management Field (AMF) value
amf: '8000'
# IMEI number of the device. It is used if no SUPI is provided
imei: '356938035643803'
# IMEISV number of the device. It is used if no SUPI and IMEI is provided
imeiSv: '4370816125816151'

# List of gNB IP addresses for Radio Link Simulation
gnbSearchList:
  - 192.168.56.131 #127.0.0.1

# UAC Access Identities Configuration
uacAic:
  mps: false
  mcs: false

#uacAic:
#  - type: 'IPv4'
#    apn: 'internet'
#    slice:
#      sst: 1
#      sd: 0x000002

# UAC Access Control Class
uacAcc:
  normalClass: 0
  class11: false
  class12: false
  class13: false
  class14: false
  class15: false

# Initial PDU sessions to be established
sessions:
  - type: 'IPv4'
    apn: 'internet'
    slice:
      sst: 1
      sd: 0x000003

# Configured NSSAI for this UE by HPLMN
configured-nssai:
  - sst: 1
    sd: 0x000003

# Default Configured NSSAI for this UE
default-nssai:
  - sst: 1
    sd: 0x000003

# Supported integrity algorithms by this UE
integrity:
  IA1: true
  IA2: true
  IA3: true

# Supported encryption algorithms by this UE
ciphering:
  EA1: true
  EA2: true
  EA3: true

# Integrity protection maximum data rate for user plane
integrityMaxRate:
  uplink: 'full'
  downlink: 'full'

```

<a id="network_settings"></a>

## Network settings of free5GC 5GC and UERANSIM UE / RAN

<a id="network_settings_cp"></a>

### Network settings of free5GC 5GC C-Plane

Add IP addresses for SMF1 and SMF2.

```
ip addr add 192.168.56.142/24 dev enp0s8
ip addr add 192.168.56.143/24 dev enp0s8
ip addr add 192.168.56.147/24 dev enp0s8
```

**Note. `enp0s8` is the network interface of `192.168.0.0/24` in my VirtualBox environment.
Please change it according to your environment.**

<a id="network_settings_up1"></a>

### Network settings of free5GC 5GC U-Plane1

First, uncomment the next line in the `/etc/sysctl.conf` file and reflect it in the OS.

```
net.ipv4.ip_forward=1
```

```
# sysctl -p
```

Next, configure NAPT.

```
# iptables -t nat -A POSTROUTING -s 10.60.0.0/16 ! -o upfgtp -j MASQUERADE
```

<a id="network_settings_up2"></a>

### Network settings of free5GC 5GC U-Plane2

First, uncomment the next line in the `/etc/sysctl.conf` file and reflect it in the OS.

```
net.ipv4.ip_forward=1
```

```
# sysctl -p
```

Next, configure NAPT.

```
# iptables -t nat -A POSTROUTING -s 10.61.0.0/16 ! -o upfgtp -j MASQUERADE
```

## Runing the Experiment

First run the 5GC, then UERANSIM (UE & RAN implementation).
<a id="run_up"></a>

### Run free5GC 5GC U-Plane1, 2 & 3

First, run free5GC 5GC U-Planes. Please see [here](https://github.com/free5gc/free5gc/issues/170#issuecomment-773214169) for the reason.  
**Note. It was improved on 2022.11.08, and you don't have to worry about the startup order of C-Plane and U-Plane.**

- free5GC 5GC U-Plane1

```
# cd free5gc
# bin/upf
```

- free5GC 5GC U-Plane2

```
# cd free5gc
# bin/upf
```

- free5GC 5GC U-Plane3

```
# cd free5gc
# bin/upf
```

Then run `tcpdump` on one more terminal for each U-Plane.

- Run `tcpdump` on VM2 (U-Plane1)

```
# tcpdump -i upfgtp -n
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on upfgtp, link-type RAW (Raw IP), capture size 262144 bytes
```

- Run `tcpdump` on VM3 (U-Plane2)

```
# tcpdump -i upfgtp -n
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on upfgtp, link-type RAW (Raw IP), capture size 262144 bytes
```

<a id="run_cp"></a>

### Run free5GC 5GC C-Plane

Next, run free5GC 5GC C-Plane.

- free5GC 5GC C-Plane

Create the following shell script and run it.

```bash
#!/usr/bin/env bash

PID_LIST=()

NF_LIST1="smf"
NF_LIST2="amf udr pcf udm nssf ausf"

export GIN_MODE=release

./bin/nrf &
PID_LIST+=($!)
sleep 1

for NF in ${NF_LIST1}; do
    ./bin/${NF} -c config/${NF}cfg1.yaml &
    PID_LIST+=($!)
    sleep 1
    ./bin/${NF} -c config/${NF}cfg2.yaml &
    PID_LIST+=($!)
    sleep 1
 ./bin/${NF} -c config/${NF}cfg3.yaml &
    PID_LIST+=($!)
    sleep 1
done

for NF in ${NF_LIST2}; do
    ./bin/${NF} &
    PID_LIST+=($!)
    sleep 1
done

function terminate()
{
    sudo kill -SIGTERM ${PID_LIST[${#PID_LIST[@]}-2]} ${PID_LIST[${#PID_LIST[@]}-1]}
    sleep 2
}

trap terminate SIGINT
wait ${PID_LIST}
```

Also run the server in another terminal :

```
cd 5NR-CP/webconsole
go run server.go
```

<a id="run_ran"></a>

### Run UERANSIM (gNodeB)

Please refer to the following for usage of UERANSIM.

<https://github.com/aligungr/UERANSIM/wiki/Usage>

```
# ./nr-gnb -c ../config/free5gc-gnb.yaml
UERANSIM v3.2.6
[2023-03-18 19:25:17.730] [sctp] [info] Trying to establish SCTP connection... (192.168.0.141:38412)
[2023-03-18 19:25:17.733] [sctp] [info] SCTP connection established (192.168.0.141:38412)
[2023-03-18 19:25:17.733] [sctp] [debug] SCTP association setup ascId[7]
[2023-03-18 19:25:17.733] [ngap] [debug] Sending NG Setup Request
[2023-03-18 19:25:17.740] [ngap] [debug] NG Setup Response received
[2023-03-18 19:25:17.741] [ngap] [info] NG Setup procedure is successful
```

The free5GC C-Plane log when executed is as follows.

```
2023-03-18T19:25:17.734605363+09:00 [INFO][AMF][NGAP] [AMF] SCTP Accept from: 192.168.0.131:50228
2023-03-18T19:25:17.735510262+09:00 [INFO][AMF][NGAP] Create a new NG connection for: 192.168.0.131:50228
2023-03-18T19:25:17.739838968+09:00 [INFO][AMF][NGAP][192.168.0.131:50228] Handle NG Setup request
2023-03-18T19:25:17.740052244+09:00 [INFO][AMF][NGAP][192.168.0.131:50228] Send NG-Setup response
```

<a id="run_sd1"></a>

### Run UERANSIM (UE[SST:1, SD:0x000001])

Confirm that the packet goes through the DN of U-Plane1 based on SST:1 and SD:0x000001.

<a id="con_sd1"></a>

#### UE connects to U-Plane1 based on SST:1 and SD:0x000001

```
# ./nr-ue -c ../config/free5gc-ue-sd1.yaml 
UERANSIM v3.2.6
[2023-03-18 19:27:29.241] [nas] [info] UE switches to state [MM-DEREGISTERED/PLMN-SEARCH]
[2023-03-18 19:27:29.242] [rrc] [debug] New signal detected for cell[1], total [1] cells in coverage
[2023-03-18 19:27:29.242] [nas] [info] Selected plmn[001/01]
[2023-03-18 19:27:29.242] [rrc] [info] Selected cell plmn[001/01] tac[1] category[SUITABLE]
[2023-03-18 19:27:29.243] [nas] [info] UE switches to state [MM-DEREGISTERED/PS]
[2023-03-18 19:27:29.243] [nas] [info] UE switches to state [MM-DEREGISTERED/NORMAL-SERVICE]
[2023-03-18 19:27:29.243] [nas] [debug] Initial registration required due to [MM-DEREG-NORMAL-SERVICE]
[2023-03-18 19:27:29.245] [nas] [debug] UAC access attempt is allowed for identity[0], category[MO_sig]
[2023-03-18 19:27:29.245] [nas] [debug] Sending Initial Registration
[2023-03-18 19:27:29.245] [rrc] [debug] Sending RRC Setup Request
[2023-03-18 19:27:29.246] [nas] [info] UE switches to state [MM-REGISTER-INITIATED]
[2023-03-18 19:27:29.246] [rrc] [info] RRC connection established
[2023-03-18 19:27:29.246] [rrc] [info] UE switches to state [RRC-CONNECTED]
[2023-03-18 19:27:29.247] [nas] [info] UE switches to state [CM-CONNECTED]
[2023-03-18 19:27:29.284] [nas] [debug] Authentication Request received
[2023-03-18 19:27:29.295] [nas] [debug] Security Mode Command received
[2023-03-18 19:27:29.296] [nas] [debug] Selected integrity[2] ciphering[0]
[2023-03-18 19:27:29.346] [nas] [debug] Registration accept received
[2023-03-18 19:27:29.346] [nas] [info] UE switches to state [MM-REGISTERED/NORMAL-SERVICE]
[2023-03-18 19:27:29.347] [nas] [debug] Sending Registration Complete
[2023-03-18 19:27:29.347] [nas] [info] Initial Registration is successful
[2023-03-18 19:27:29.347] [nas] [debug] Sending PDU Session Establishment Request
[2023-03-18 19:27:29.347] [nas] [debug] UAC access attempt is allowed for identity[0], category[MO_sig]
[2023-03-18 19:27:29.608] [nas] [debug] PDU Session Establishment Accept received
[2023-03-18 19:27:29.613] [nas] [info] PDU Session establishment is successful PSI[1]
[2023-03-18 19:27:29.634] [app] [info] Connection setup for PDU session[1] is successful, TUN interface[uesimtun0, 10.60.0.1] is up.
```

The free5GC C-Plane log when executed is as follows.

```

```

The free5GC U-Plane1 log when executed is as follows.

```
2023-03-18T19:27:29.593228827+09:00 [INFO][UPF][PFCP][LAddr:192.168.0.144:8805] handleSessionEstablishmentRequest
2023-03-18T19:27:29.593262784+09:00 [INFO][UPF][PFCP][LAddr:192.168.0.144:8805][CPNodeID:192.168.0.142][CPSEID:0x1][UPSEID:0x1] New session
2023-03-18T19:27:29.607060430+09:00 [INFO][UPF][PFCP][LAddr:192.168.0.144:8805] handleSessionModificationRequest
```

The TUNnel interface `uesimtun0` is created as follows.

```
# ip addr show
...
10: uesimtun0: <POINTOPOINT,PROMISC,NOTRAILERS,UP,LOWER_UP> mtu 1400 qdisc fq_codel state UNKNOWN group default qlen 500
    link/none 
    inet 10.60.0.1/32 scope global uesimtun0
       valid_lft forever preferred_lft forever
    inet6 fe80::3873:9adb:55fb:719d/64 scope link stable-privacy 
       valid_lft forever preferred_lft forever
...
```

<a id="ping_sd1"></a>

#### Ping google.com or the corresponding UPF machine IP going through DN=10.60.0.0/16 on U-Plane1

Confirm by using `tcpdump` that the packet goes through `if=upfgtp` on U-Plane1.

```
# ping google.com -I uesimtun0 -n
PING google.com (172.217.175.110) from 10.60.0.1 uesimtun0: 56(84) bytes of data.
64 bytes from 172.217.175.110: icmp_seq=1 ttl=61 time=21.3 ms
64 bytes from 172.217.175.110: icmp_seq=2 ttl=61 time=18.1 ms
64 bytes from 172.217.175.110: icmp_seq=3 ttl=61 time=17.5 ms
```

<a id="run_sd2"></a>

### Run UERANSIM (UE[SST:1, SD:0x000002])

Then the UE disconnects from gNodeB and connects to gNodeB using the configuration file for SST:1 and SD:0x000002.
Confirm that the packet goes through the DN of U-Plane2 based on SST:1 and SD:0x000002.

<a id="con_sd2"></a>

#### UE connects to U-Plane2 based on SST:1 and SD:0x000002

```
# ./nr-ue -c ../config/free5gc-ue-sd2.yaml 
UERANSIM v3.2.6
[2023-03-18 19:34:17.464] [nas] [info] UE switches to state [MM-DEREGISTERED/PLMN-SEARCH]
[2023-03-18 19:34:17.464] [rrc] [debug] New signal detected for cell[1], total [1] cells in coverage
[2023-03-18 19:34:17.464] [nas] [info] Selected plmn[001/01]
[2023-03-18 19:34:17.465] [rrc] [info] Selected cell plmn[001/01] tac[1] category[SUITABLE]
[2023-03-18 19:34:17.465] [nas] [info] UE switches to state [MM-DEREGISTERED/PS]
[2023-03-18 19:34:17.465] [nas] [info] UE switches to state [MM-DEREGISTERED/NORMAL-SERVICE]
[2023-03-18 19:34:17.465] [nas] [debug] Initial registration required due to [MM-DEREG-NORMAL-SERVICE]
[2023-03-18 19:34:17.467] [nas] [debug] UAC access attempt is allowed for identity[0], category[MO_sig]
[2023-03-18 19:34:17.467] [nas] [debug] Sending Initial Registration
[2023-03-18 19:34:17.467] [rrc] [debug] Sending RRC Setup Request
[2023-03-18 19:34:17.468] [nas] [info] UE switches to state [MM-REGISTER-INITIATED]
[2023-03-18 19:34:17.468] [rrc] [info] RRC connection established
[2023-03-18 19:34:17.468] [rrc] [info] UE switches to state [RRC-CONNECTED]
[2023-03-18 19:34:17.468] [nas] [info] UE switches to state [CM-CONNECTED]
[2023-03-18 19:34:17.487] [nas] [debug] Authentication Request received
[2023-03-18 19:34:17.495] [nas] [debug] Security Mode Command received
[2023-03-18 19:34:17.495] [nas] [debug] Selected integrity[2] ciphering[0]
[2023-03-18 19:34:17.523] [nas] [debug] Registration accept received
[2023-03-18 19:34:17.523] [nas] [info] UE switches to state [MM-REGISTERED/NORMAL-SERVICE]
[2023-03-18 19:34:17.523] [nas] [debug] Sending Registration Complete
[2023-03-18 19:34:17.523] [nas] [info] Initial Registration is successful
[2023-03-18 19:34:17.523] [nas] [debug] Sending PDU Session Establishment Request
[2023-03-18 19:34:17.524] [nas] [debug] UAC access attempt is allowed for identity[0], category[MO_sig]
[2023-03-18 19:34:17.773] [nas] [debug] PDU Session Establishment Accept received
[2023-03-18 19:34:17.776] [nas] [info] PDU Session establishment is successful PSI[1]
[2023-03-18 19:34:17.797] [app] [info] Connection setup for PDU session[1] is successful, TUN interface[uesimtun0, 10.61.0.1] is up.
```

The free5GC C-Plane log when executed is as follows.

```

```

The free5GC U-Plane2 log when executed is as follows.

```
2023-03-18T19:34:17.774659569+09:00 [INFO][UPF][PFCP][LAddr:192.168.0.145:8805] handleSessionEstablishmentRequest
2023-03-18T19:34:17.774693252+09:00 [INFO][UPF][PFCP][LAddr:192.168.0.145:8805][CPNodeID:192.168.0.143][CPSEID:0x1][UPSEID:0x1] New session
2023-03-18T19:34:17.784494287+09:00 [INFO][UPF][PFCP][LAddr:192.168.0.145:8805] handleSessionModificationRequest
```

The TUNnel interface `uesimtun0` is created as follows.

```
# ip addr show
...
11: uesimtun0: <POINTOPOINT,PROMISC,NOTRAILERS,UP,LOWER_UP> mtu 1400 qdisc fq_codel state UNKNOWN group default qlen 500
    link/none 
    inet 10.61.0.1/32 scope global uesimtun0
       valid_lft forever preferred_lft forever
    inet6 fe80::ace7:dd5d:309e:1bc2/64 scope link stable-privacy 
       valid_lft forever preferred_lft forever
...
```

<a id="ping_sd2"></a>

#### Ping google.com going through DN=10.61.0.0/16 on U-Plane2

Confirm by using `tcpdump` that the packet goes through `if=upfgtp` on U-Plane2.

```
# ping google.com -I uesimtun0 -n
PING google.com (142.250.199.110) from 10.61.0.1 uesimtun0: 56(84) bytes of data.
64 bytes from 142.250.199.110: icmp_seq=1 ttl=61 time=26.7 ms
64 bytes from 142.250.199.110: icmp_seq=2 ttl=61 time=30.6 ms
64 bytes from 142.250.199.110: icmp_seq=3 ttl=61 time=21.5 ms
```


### Similarly run for UE-3 (UE[SST:1, SD:0x000003])