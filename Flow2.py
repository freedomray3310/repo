[
    {
        "id": "16e38af3.fadfe5",
        "type": "tab",
        "label": "Flow 5",
        "disabled": false,
        "info": ""
    },
    {
        "id": "acb80d6e.6ee4c",
        "type": "inject",
        "z": "16e38af3.fadfe5",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 190,
        "y": 160,
        "wires": [
            [
                "79bf429c.41ba1c"
            ]
        ]
    },
    {
        "id": "79bf429c.41ba1c",
        "type": "function",
        "z": "16e38af3.fadfe5",
        "name": "payload",
        "func": "msg.headers={\n    devicekey: \"YYEFletLjL0bKPFO\"\n    };\n    \nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 390,
        "y": 260,
        "wires": [
            [
                "8b09e875.8cba88"
            ]
        ]
    },
    {
        "id": "8aac085c.262fb8",
        "type": "http response",
        "z": "16e38af3.fadfe5",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 650,
        "y": 380,
        "wires": []
    },
    {
        "id": "8b09e875.8cba88",
        "type": "http request",
        "z": "16e38af3.fadfe5",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "paytoqs": false,
        "url": "http://api.mediatek.com/mcs/v2/devices/DgIXVwn5/datachannels/Temperature/datapoints.csv",
        "tls": "",
        "proxy": "",
        "authType": "",
        "x": 450,
        "y": 420,
        "wires": [
            [
                "8aac085c.262fb8",
                "e01fb022.762a7"
            ]
        ]
    },
    {
        "id": "e01fb022.762a7",
        "type": "debug",
        "z": "16e38af3.fadfe5",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 680,
        "y": 480,
        "wires": []
    }
]
