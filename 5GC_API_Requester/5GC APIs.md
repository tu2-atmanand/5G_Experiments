# HTTP request output

This file contains the output of the curl commands, which are basically HTTP requests made to the various Network Functions, inside the 5G Core system.

**NOTE : The commands are in first in first out order, so the request happened first in during the simulation, is at the bottom, then it is moved all the way up in this file.**

> curl "<http://127.0.0.10:8000/nnrf-disc/v1/nf-instances?preferred-locality=area1&requester-nf-type=AMF&supi=imsi-208930000000003&target-nf-type=PCF>"

Output :

```json
{
  "validityPeriod": 100,
  "nfInstances": [
    {
      "nfInstanceId": "e12c94c0-71f6-4fb9-8888-dc11d072f39e",
      "nfType": "PCF",
      "nfStatus": "REGISTERED",
      "plmnList": [
        {
          "mcc": "208",
          "mnc": "93"
        }
      ],
      "ipv4Addresses": [
        "127.0.0.7"
      ],
      "locality": "area1",
      "pcfInfo": {
        "dnnList": [
          "free5gc",
          "internet"
        ]
      },
      "nfServices": [
        {
          "serviceInstanceId": "3",
          "serviceName": "npcf-policyauthorization",
          "versions": [
            {
              "apiVersionInUri": "v1",
              "apiFullVersion": "1.0.1"
            }
          ],
          "scheme": "http",
          "nfServiceStatus": "REGISTERED",
          "ipEndPoints": [
            {
              "ipv4Address": "127.0.0.7",
              "transport": "TCP",
              "port": 8000
            }
          ],
          "apiPrefix": "http://127.0.0.7:8000",
          "supportedFeatures": "3"
        },
        {
          "serviceInstanceId": "4",
          "serviceName": "npcf-eventexposure",
          "versions": [
            {
              "apiVersionInUri": "v1",
              "apiFullVersion": "1.0.1"
            }
          ],
          "scheme": "http",
          "nfServiceStatus": "REGISTERED",
          "ipEndPoints": [
            {
              "ipv4Address": "127.0.0.7",
              "transport": "TCP",
              "port": 8000
            }
          ],
          "apiPrefix": "http://127.0.0.7:8000"
        },
        {
          "serviceInstanceId": "5",
          "serviceName": "npcf-ue-policy-control",
          "versions": [
            {
              "apiVersionInUri": "v1",
              "apiFullVersion": "1.0.1"
            }
          ],
          "scheme": "http",
          "nfServiceStatus": "REGISTERED",
          "ipEndPoints": [
            {
              "ipv4Address": "127.0.0.7",
              "transport": "TCP",
              "port": 8000
            }
          ],
          "apiPrefix": "http://127.0.0.7:8000"
        },
        {
          "serviceInstanceId": "0",
          "serviceName": "npcf-am-policy-control",
          "versions": [
            {
              "apiVersionInUri": "v1",
              "apiFullVersion": "1.0.1"
            }
          ],
          "scheme": "http",
          "nfServiceStatus": "REGISTERED",
          "ipEndPoints": [
            {
              "ipv4Address": "127.0.0.7",
              "transport": "TCP",
              "port": 8000
            }
          ],
          "apiPrefix": "http://127.0.0.7:8000"
        },
        {
          "serviceInstanceId": "1",
          "serviceName": "npcf-smpolicycontrol",
          "versions": [
            {
              "apiVersionInUri": "v1",
              "apiFullVersion": "1.0.1"
            }
          ],
          "scheme": "http",
          "nfServiceStatus": "REGISTERED",
          "ipEndPoints": [
            {
              "ipv4Address": "127.0.0.7",
              "transport": "TCP",
              "port": 8000
            }
          ],
          "apiPrefix": "http://127.0.0.7:8000",
          "supportedFeatures": "3fff"
        },
        {
          "serviceInstanceId": "2",
          "serviceName": "npcf-bdtpolicycontrol",
          "versions": [
            {
              "apiVersionInUri": "v1",
              "apiFullVersion": "1.0.1"
            }
          ],
          "scheme": "http",
          "nfServiceStatus": "REGISTERED",
          "ipEndPoints": [
            {
              "ipv4Address": "127.0.0.7",
              "transport": "TCP",
              "port": 8000
            }
          ],
          "apiPrefix": "http://127.0.0.7:8000"
        }
      ]
    }
  ]
}
```

> curl "<http://127.0.0.10:8000/nnrf-disc/v1/nf-instances?requester-nf-type=SMF&target-nf-instance-id=7ffebf49-da84-41df-975b-456520818485&target-nf-type=AMF>"

Output :

```json
{
  "validityPeriod": 100,
  "nfInstances": [
    {
      "nfInstanceId": "7ffebf49-da84-41df-975b-456520818485",
      "nfType": "AMF",
      "nfStatus": "REGISTERED",
      "plmnList": [
        {
          "mcc": "208",
          "mnc": "93"
        }
      ],
      "sNssais": [
        {
          "sst": 1,
          "sd": "000001"
        },
        {
          "sst": 1,
          "sd": "000002"
        },
        {
          "sst": 1,
          "sd": "000003"
        }
      ],
      "ipv4Addresses": [
        "127.0.0.18"
      ],
      "amfInfo": {
        "amfSetId": "3f8",
        "amfRegionId": "ca",
        "guamiList": [
          {
            "plmnId": {
              "mcc": "208",
              "mnc": "93"
            },
            "amfId": "cafe00"
          }
        ],
        "taiList": [
          {
            "plmnId": {
              "mcc": "208",
              "mnc": "93"
            },
            "tac": "000001"
          }
        ]
      },
      "nfServices": [
        {
          "serviceInstanceId": "0",
          "serviceName": "namf-comm",
          "versions": [
            {
              "apiVersionInUri": "v1",
              "apiFullVersion": "1.0.3"
            }
          ],
          "scheme": "http",
          "nfServiceStatus": "REGISTERED",
          "ipEndPoints": [
            {
              "ipv4Address": "127.0.0.18",
              "transport": "TCP",
              "port": 8000
            }
          ],
          "apiPrefix": "http://127.0.0.18:8000"
        },
        {
          "serviceInstanceId": "1",
          "serviceName": "namf-evts",
          "versions": [
            {
              "apiVersionInUri": "v1",
              "apiFullVersion": "1.0.3"
            }
          ],
          "scheme": "http",
          "nfServiceStatus": "REGISTERED",
          "ipEndPoints": [
            {
              "ipv4Address": "127.0.0.18",
              "transport": "TCP",
              "port": 8000
            }
          ],
          "apiPrefix": "http://127.0.0.18:8000"
        },
        {
          "serviceInstanceId": "2",
          "serviceName": "namf-mt",
          "versions": [
            {
              "apiVersionInUri": "v1",
              "apiFullVersion": "1.0.3"
            }
          ],
          "scheme": "http",
          "nfServiceStatus": "REGISTERED",
          "ipEndPoints": [
            {
              "ipv4Address": "127.0.0.18",
              "transport": "TCP",
              "port": 8000
            }
          ],
          "apiPrefix": "http://127.0.0.18:8000"
        },
        {
          "serviceInstanceId": "3",
          "serviceName": "namf-loc",
          "versions": [
            {
              "apiVersionInUri": "v1",
              "apiFullVersion": "1.0.3"
            }
          ],
          "scheme": "http",
          "nfServiceStatus": "REGISTERED",
          "ipEndPoints": [
            {
              "ipv4Address": "127.0.0.18",
              "transport": "TCP",
              "port": 8000
            }
          ],
          "apiPrefix": "http://127.0.0.18:8000"
        },
        {
          "serviceInstanceId": "4",
          "serviceName": "namf-oam",
          "versions": [
            {
              "apiVersionInUri": "v1",
              "apiFullVersion": "1.0.3"
            }
          ],
          "scheme": "http",
          "nfServiceStatus": "REGISTERED",
          "ipEndPoints": [
            {
              "ipv4Address": "127.0.0.18",
              "transport": "TCP",
              "port": 8000
            }
          ],
          "apiPrefix": "http://127.0.0.18:8000"
        }
      ]
    }
  ]
}
```

> curl "<http://127.0.0.10:8000/nnrf-disc/v1/nf-instances?requester-nf-type=AMF&supi=imsi-208930000000003&target-nf-type=UDM>"

Output :

```json
{
  "validityPeriod": 100,
  "nfInstances": [
    {
      "nfInstanceId": "874d6926-fb2d-4951-b94d-5dcfddcec7f0",
      "nfType": "UDM",
      "nfStatus": "REGISTERED",
      "plmnList": [
        {
          "mcc": "208",
          "mnc": "93"
        }
      ],
      "ipv4Addresses": [
        "127.0.0.3"
      ],
      "udmInfo": {},
      "nfServices": [
        {
          "serviceInstanceId": "1",
          "serviceName": "nudm-uecm",
          "versions": [
            {
              "apiVersionInUri": "v1",
              "apiFullVersion": "1.0.2"
            }
          ],
          "scheme": "http",
          "nfServiceStatus": "REGISTERED",
          "ipEndPoints": [
            {
              "ipv4Address": "127.0.0.3",
              "transport": "TCP",
              "port": 8000
            }
          ],
          "apiPrefix": "http://127.0.0.3:8000"
        },
        {
          "serviceInstanceId": "2",
          "serviceName": "nudm-ueau",
          "versions": [
            {
              "apiVersionInUri": "v1",
              "apiFullVersion": "1.0.2"
            }
          ],
          "scheme": "http",
          "nfServiceStatus": "REGISTERED",
          "ipEndPoints": [
            {
              "ipv4Address": "127.0.0.3",
              "transport": "TCP",
              "port": 8000
            }
          ],
          "apiPrefix": "http://127.0.0.3:8000"
        },
        {
          "serviceInstanceId": "3",
          "serviceName": "nudm-ee",
          "versions": [
            {
              "apiVersionInUri": "v1",
              "apiFullVersion": "1.0.2"
            }
          ],
          "scheme": "http",
          "nfServiceStatus": "REGISTERED",
          "ipEndPoints": [
            {
              "ipv4Address": "127.0.0.3",
              "transport": "TCP",
              "port": 8000
            }
          ],
          "apiPrefix": "http://127.0.0.3:8000"
        },
        {
          "serviceInstanceId": "4",
          "serviceName": "nudm-pp",
          "versions": [
            {
              "apiVersionInUri": "v1",
              "apiFullVersion": "1.0.2"
            }
          ],
          "scheme": "http",
          "nfServiceStatus": "REGISTERED",
          "ipEndPoints": [
            {
              "ipv4Address": "127.0.0.3",
              "transport": "TCP",
              "port": 8000
            }
          ],
          "apiPrefix": "http://127.0.0.3:8000"
        },
        {
          "serviceInstanceId": "0",
          "serviceName": "nudm-sdm",
          "versions": [
            {
              "apiVersionInUri": "v1",
              "apiFullVersion": "1.0.2"
            }
          ],
          "scheme": "http",
          "nfServiceStatus": "REGISTERED",
          "ipEndPoints": [
            {
              "ipv4Address": "127.0.0.3",
              "transport": "TCP",
              "port": 8000
            }
          ],
          "apiPrefix": "http://127.0.0.3:8000"
        }
      ]
    }
  ]
}
```

> curl "<http://127.0.0.10:8000/nnrf-disc/v1/nf-instances?requester-nf-type=AMF&supi=imsi-208930000000003&target-nf-type=UDR>"

Output :

```json
{
  "validityPeriod": 100,
  "nfInstances": [
    {
      "nfInstanceId": "8a9786de-82f2-48b8-a70b-dc4bc9704bf3",
      "nfType": "UDR",
      "nfStatus": "REGISTERED",
      "plmnList": [
        {
          "mcc": "208",
          "mnc": "93"
        }
      ],
      "ipv4Addresses": [
        "127.0.0.4"
      ],
      "udrInfo": {
        "supportedDataSets": [
          "SUBSCRIPTION"
        ]
      },
      "nfServices": [
        {
          "serviceInstanceId": "datarepository",
          "serviceName": "nudr-dr",
          "versions": [
            {
              "apiVersionInUri": "v1",
              "apiFullVersion": "1.0.1"
            }
          ],
          "scheme": "http",
          "nfServiceStatus": "REGISTERED",
          "ipEndPoints": [
            {
              "ipv4Address": "127.0.0.4",
              "transport": "TCP",
              "port": 8000
            }
          ],
          "apiPrefix": "http://127.0.0.4:8000"
        }
      ]
    }
  ]
}
 ```




> curl "http://127.0.0.10:8000/nnrf-nfm/v1/nf-instances/fa7203e5-5aac-49e6-ab95-50f5d2a89c1e"

Output :
```json
{
  "ipv4Addresses": [
    "127.0.0.2"
  ],
  "locality": "area1",
  "nfInstanceId": "fa7203e5-5aac-49e6-ab95-50f5d2a89c1e",
  "nfServices": [
    {
      "apiPrefix": "http://127.0.0.2:8000",
      "nfServiceStatus": "REGISTERED",
      "scheme": "https",
      "serviceInstanceId": "fa7203e5-5aac-49e6-ab95-50f5d2a89c1ensmf-pdusession",
      "serviceName": "nsmf-pdusession",
      "versions": [
        {
          "apiFullVersion": "https://127.0.0.2:8000/nsmf-pdusession/v1",
          "apiVersionInUri": "v1",
          "expiry": "2023-12-25T18:18:25.917550401Z"
        }
      ]
    },
    {
      "apiPrefix": "http://127.0.0.2:8000",
      "nfServiceStatus": "REGISTERED",
      "scheme": "https",
      "serviceInstanceId": "fa7203e5-5aac-49e6-ab95-50f5d2a89c1ensmf-event-exposure",
      "serviceName": "nsmf-event-exposure",
      "versions": [
        {
          "apiFullVersion": "https://127.0.0.2:8000/nsmf-pdusession/v1",
          "apiVersionInUri": "v1",
          "expiry": "2023-12-25T18:18:25.917550401Z"
        }
      ]
    },
    {
      "apiPrefix": "http://127.0.0.2:8000",
      "nfServiceStatus": "REGISTERED",
      "scheme": "https",
      "serviceInstanceId": "fa7203e5-5aac-49e6-ab95-50f5d2a89c1ensmf-oam",
      "serviceName": "nsmf-oam",
      "versions": [
        {
          "apiFullVersion": "https://127.0.0.2:8000/nsmf-pdusession/v1",
          "apiVersionInUri": "v1",
          "expiry": "2023-12-25T18:18:25.917550401Z"
        }
      ]
    }
  ],
  "nfStatus": "REGISTERED",
  "nfType": "SMF",
  "plmnList": [
    {
      "mcc": "208",
      "mnc": "93"
    }
  ],
  "sNssais": [
    {
      "sd": "000001",
      "sst": 1
    }
  ],
  "smfInfo": {
    "sNssaiSmfInfoList": [
      {
        "dnnSmfInfoList": [
          {
            "dnn": "internet"
          }
        ],
        "sNssai": {
          "sd": "000001",
          "sst": 1
        }
      }
    ]
  }
}
```

> curl "<http://127.0.0.10:8000/nnrf-nfm/v1/nf-instances/fa7203e5-5aac-49e6-ab95-50f5d2a89c1e>"

Output :

```json
{
  "ipv4Addresses": [
    "127.0.0.2"
  ],
  "locality": "area1",
  "nfInstanceId": "fa7203e5-5aac-49e6-ab95-50f5d2a89c1e",
  "nfServices": [
    {
      "apiPrefix": "http://127.0.0.2:8000",
      "nfServiceStatus": "REGISTERED",
      "scheme": "https",
      "serviceInstanceId": "fa7203e5-5aac-49e6-ab95-50f5d2a89c1ensmf-pdusession",
      "serviceName": "nsmf-pdusession",
      "versions": [
        {
          "apiFullVersion": "https://127.0.0.2:8000/nsmf-pdusession/v1",
          "apiVersionInUri": "v1",
          "expiry": "2023-12-25T18:18:25.917550401Z"
        }
      ]
    },
    {
      "apiPrefix": "http://127.0.0.2:8000",
      "nfServiceStatus": "REGISTERED",
      "scheme": "https",
      "serviceInstanceId": "fa7203e5-5aac-49e6-ab95-50f5d2a89c1ensmf-event-exposure",
      "serviceName": "nsmf-event-exposure",
      "versions": [
        {
          "apiFullVersion": "https://127.0.0.2:8000/nsmf-pdusession/v1",
          "apiVersionInUri": "v1",
          "expiry": "2023-12-25T18:18:25.917550401Z"
        }
      ]
    },
    {
      "apiPrefix": "http://127.0.0.2:8000",
      "nfServiceStatus": "REGISTERED",
      "scheme": "https",
      "serviceInstanceId": "fa7203e5-5aac-49e6-ab95-50f5d2a89c1ensmf-oam",
      "serviceName": "nsmf-oam",
      "versions": [
        {
          "apiFullVersion": "https://127.0.0.2:8000/nsmf-pdusession/v1",
          "apiVersionInUri": "v1",
          "expiry": "2023-12-25T18:18:25.917550401Z"
        }
      ]
    }
  ],
  "nfStatus": "REGISTERED",
  "nfType": "SMF",
  "plmnList": [
    {
      "mcc": "208",
      "mnc": "93"
    }
  ],
  "sNssais": [
    {
      "sd": "000001",
      "sst": 1
    }
  ],
  "smfInfo": {
    "sNssaiSmfInfoList": [
      {
        "dnnSmfInfoList": [
          {
            "dnn": "internet"
          }
        ],
        "sNssai": {
          "sd": "000001",
          "sst": 1
        }
      }
    ]
  }
}
```

> curl "<http://127.0.0.10:8000/nnrf-nfm/v1/nf-instances/dd328f7e-c57d-4777-b63a-08591f83f02a>"

Output :

```json
{
  "ipv4Addresses": [
    "127.0.0.12"
  ],
  "locality": "area1",
  "nfInstanceId": "dd328f7e-c57d-4777-b63a-08591f83f02a",
  "nfServices": [
    {
      "apiPrefix": "http://127.0.0.12:8000",
      "nfServiceStatus": "REGISTERED",
      "scheme": "https",
      "serviceInstanceId": "dd328f7e-c57d-4777-b63a-08591f83f02ansmf-pdusession",
      "serviceName": "nsmf-pdusession",
      "versions": [
        {
          "apiFullVersion": "https://127.0.0.12:8000/nsmf-pdusession/v1",
          "apiVersionInUri": "v1",
          "expiry": "2023-12-25T18:18:26.694582247Z"
        }
      ]
    },
    {
      "apiPrefix": "http://127.0.0.12:8000",
      "nfServiceStatus": "REGISTERED",
      "scheme": "https",
      "serviceInstanceId": "dd328f7e-c57d-4777-b63a-08591f83f02ansmf-event-exposure",
      "serviceName": "nsmf-event-exposure",
      "versions": [
        {
          "apiFullVersion": "https://127.0.0.12:8000/nsmf-pdusession/v1",
          "apiVersionInUri": "v1",
          "expiry": "2023-12-25T18:18:26.694582247Z"
        }
      ]
    },
    {
      "apiPrefix": "http://127.0.0.12:8000",
      "nfServiceStatus": "REGISTERED",
      "scheme": "https",
      "serviceInstanceId": "dd328f7e-c57d-4777-b63a-08591f83f02ansmf-oam",
      "serviceName": "nsmf-oam",
      "versions": [
        {
          "apiFullVersion": "https://127.0.0.12:8000/nsmf-pdusession/v1",
          "apiVersionInUri": "v1",
          "expiry": "2023-12-25T18:18:26.694582247Z"
        }
      ]
    }
  ],
  "nfStatus": "REGISTERED",
  "nfType": "SMF",
  "plmnList": [
    {
      "mcc": "208",
      "mnc": "93"
    }
  ],
  "sNssais": [
    {
      "sd": "000002",
      "sst": 1
    }
  ],
  "smfInfo": {
    "sNssaiSmfInfoList": [
      {
        "dnnSmfInfoList": [
          {
            "dnn": "internet"
          }
        ],
        "sNssai": {
          "sd": "000002",
          "sst": 1
        }
      }
    ]
  }
}
```
