import pytest

@pytest.fixture
def list_1():
    return [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2021-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  },
  {
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  },
  {
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {
      "amount": "43318.34",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "to": "Счет 74489636417521191160"
  },
  {
    "id": 214024827,
    "date": "2018-12-20T16:43:26.929246",
    "operationAmount": {
      "amount": "70946.18",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 10848359769870775355",
    "to": "Счет 21969751544412966366"
  },
  {
    "id": 522357576,
    "state": "CANCELL",
    "date": "2019-07-12T20:41:47.882230",
    "operationAmount": {
      "amount": "51463.70",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 48894435694657014368",
    "to": "Счет 38976430693692818358"
  }]

@pytest.fixture
def list_2():
  return [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2021-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 285353808,
    "state": "EXECUTED",
    "date": "2018-08-06T16:22:54.643491",
    "operationAmount": {
      "amount": "82946.19",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 12189246980267075758"
  },
  {
    "id": 556488059,
    "state": "CANCELED",
    "date": "2019-05-17T01:50:00.166954",
    "operationAmount": {
      "amount": "74604.56",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "МИР 8021883699486544",
    "to": "Visa Gold 8702717057933248"
  }]

@pytest.fixture
def list_3():
    return [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2021-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  },
  {
    "id": 100392079,
    "state": "EXECUTED",
    "date": "2019-03-03T03:13:18.622393",
    "operationAmount": {
      "amount": "44493.45",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Visa Classic 6319351940209800",
    "to": "Счет 14073196441261107791"
  }
  ]

@pytest.fixture
def list_4():
    return [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2021-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}, {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}, {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404', 'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'}, {'id': 214024827, 'state': 'EXECUTED', 'date': '2018-12-20T16:43:26.929246', 'operationAmount': {'amount': '70946.18', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 10848359769870775355', 'to': 'Счет 21969751544412966366'}, {'id': 522357576, 'state': 'EXECUTED', 'date': '2019-07-12T20:41:47.882230', 'operationAmount': {'amount': '51463.70', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 48894435694657014368', 'to': 'Счет 38976430693692818358'}, {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916', 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'}, {'id': 716496732, 'state': 'EXECUTED', 'date': '2018-04-04T17:33:34.701093', 'operationAmount': {'amount': '40701.91', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Gold 5999414228426353', 'to': 'Счет 72731966109147704472'}, {'id': 147815167, 'state': 'EXECUTED', 'date': '2018-01-26T15:40:13.413061', 'operationAmount': {'amount': '50870.71', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'Maestro 4598300720424501', 'to': 'Счет 43597928997568165086'}, {'id': 518707726, 'state': 'EXECUTED', 'date': '2018-11-29T07:18:23.941293', 'operationAmount': {'amount': '3348.98', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'MasterCard 3152479541115065', 'to': 'Visa Gold 9447344650495960'}, {'id': 649467725, 'state': 'EXECUTED', 'date': '2018-04-14T19:35:28.978265', 'operationAmount': {'amount': '96995.73', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Счет 27248529432547658655', 'to': 'Счет 97584898735659638967'}, {'id': 782295999, 'state': 'EXECUTED', 'date': '2019-09-11T17:30:34.445824', 'operationAmount': {'amount': '54280.01', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 24763316288121894080', 'to': 'Счет 96291777776753236930'}, {'id': 542678139, 'state': 'EXECUTED', 'date': '2018-10-14T22:27:25.205631', 'operationAmount': {'amount': '90582.51', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 2256483756542539', 'to': 'Счет 78808375133947439319'}, {'id': 558167602, 'state': 'EXECUTED', 'date': '2019-04-12T17:27:27.896421', 'operationAmount': {'amount': '43861.89', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 73654108430135874305', 'to': 'Счет 89685546118890842412'}, {'id': 407169720, 'state': 'EXECUTED', 'date': '2018-02-03T14:52:08.093722', 'operationAmount': {'amount': '67011.26', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на карту', 'from': 'MasterCard 4047671689373225', 'to': 'Maestro 3806652527413662'}, {'id': 361044570, 'state': 'EXECUTED', 'date': '2018-03-02T02:03:11.563721', 'operationAmount': {'amount': '7484.91', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 96008924215040031147', 'to': 'Счет 30377212495530283001'}, {'id': 536723678, 'state': 'EXECUTED', 'date': '2018-06-12T07:17:01.311610', 'operationAmount': {'amount': '26334.08', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Classic 4195191172583802', 'to': 'Счет 17066032701791012883'}, {'id': 633268359, 'state': 'EXECUTED', 'date': '2019-07-12T08:11:47.735774', 'operationAmount': {'amount': '2631.44', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Gold 3589276410671603', 'to': 'Счет 96292138399386853355'}, {'id': 988276204, 'state': 'EXECUTED', 'date': '2018-02-22T00:40:19.984219', 'operationAmount': {'amount': '71771.90', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 4956649687637418', 'to': 'Счет 90562872508279542248'}, {'id': 888407131, 'state': 'EXECUTED', 'date': '2019-09-29T14:25:28.588059', 'operationAmount': {'amount': '45849.53', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 35421428450077339637', 'to': 'Счет 46723050671868944961'}, {'id': 634356296, 'state': 'EXECUTED', 'date': '2018-01-21T01:10:28.317704', 'operationAmount': {'amount': '96900.90', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 33407225454123927865', 'to': 'Счет 79619011266276091215'}, {'id': 34148726, 'state': 'EXECUTED', 'date': '2018-11-23T23:52:36.999661', 'operationAmount': {'amount': '79428.73', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Platinum 5355133159258236', 'to': 'Maestro 8045769817179061'}, {'id': 104807525, 'state': 'EXECUTED', 'date': '2019-06-01T06:46:16.803326', 'operationAmount': {'amount': '60888.63', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'МИР 8201420097886664', 'to': 'Счет 35116633516390079956'}, {'id': 550607912, 'state': 'EXECUTED', 'date': '2018-07-31T12:25:32.579413', 'operationAmount': {'amount': '34380.08', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 8532498887072395', 'to': 'Счет 44238164562083919420'}, {'id': 484201274, 'state': 'EXECUTED', 'date': '2019-04-11T23:10:21.514616', 'operationAmount': {'amount': '62621.51', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на карту', 'from': 'МИР 8193813157568899', 'to': 'МИР 9425591958944146'}, {'id': 547682597, 'state': 'EXECUTED', 'date': '2018-12-29T21:45:18.495053', 'operationAmount': {'amount': '66263.93', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Счет 77977573135347241529', 'to': 'Счет 33062909508148771891'}, {'id': 811920303, 'state': 'EXECUTED', 'date': '2019-06-14T19:37:49.044089', 'operationAmount': {'amount': '63150.74', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 73222753239048295679', 'to': 'Счет 78544755774551298747'}, {'id': 509645757, 'state': 'EXECUTED', 'date': '2019-10-30T01:49:52.939296', 'operationAmount': {'amount': '23036.03', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'Visa Gold 7756673469642839', 'to': 'Счет 48943806953649539453'}, {'id': 122284694, 'state': 'EXECUTED', 'date': '2019-08-08T21:58:06.688541', 'operationAmount': {'amount': '98657.83', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Счет 99668626339273709694', 'to': 'Счет 27219929444683698245'}, {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614', 'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 7810846596785568', 'to': 'Счет 43241152692663622869'}, {'id': 743628025, 'state': 'EXECUTED', 'date': '2018-06-04T06:59:55.424356', 'operationAmount': {'amount': '978.31', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 54883981902864782073', 'to': 'Счет 61834060137088759145'}, {'id': 743278119, 'state': 'EXECUTED', 'date': '2018-10-15T08:05:34.061711', 'operationAmount': {'amount': '51203.12', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'MasterCard 1435442169918409', 'to': 'Maestro 7452400219469235'}, {'id': 871921546, 'state': 'EXECUTED', 'date': '2019-02-14T03:09:23.006652', 'operationAmount': {'amount': '47022.09', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Classic 6216537926639975', 'to': 'Счет 67667879435628279708'}, {'id': 373912477, 'state': 'EXECUTED', 'date': '2018-03-09T02:11:01.339352', 'operationAmount': {'amount': '33249.01', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'Visa Classic 7022985698476865', 'to': 'Счет 60979028617970883410'}, {'id': 720751477, 'state': 'EXECUTED', 'date': '2018-11-08T08:21:45.902633', 'operationAmount': {'amount': '16872.46', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75743795418434298755', 'to': 'Счет 80785963509390811744'}, {'id': 949194534, 'state': 'EXECUTED', 'date': '2019-08-15T01:48:10.042554', 'operationAmount': {'amount': '31222.43', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Счет 65298957349197687907', 'to': 'Счет 38784565940893479418'}, {'id': 260972664, 'state': 'EXECUTED', 'date': '2018-01-23T01:48:30.477053', 'operationAmount': {'amount': '2974.30', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 3414396880443483', 'to': 'Visa Gold 2684274847577419'}, {'id': 317987878, 'state': 'EXECUTED', 'date': '2018-01-13T13:00:58.458625', 'operationAmount': {'amount': '55985.82', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 8906171742833215', 'to': 'Visa Platinum 6086997013848217'}, {'id': 72122709, 'state': 'EXECUTED', 'date': '2018-12-18T17:07:09.800800', 'operationAmount': {'amount': '19683.25', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 86675623828180311969', 'to': 'Счет 15351391408911677994'}, {'id': 242885401, 'state': 'EXECUTED', 'date': '2019-07-08T00:08:32.986663', 'operationAmount': {'amount': '10083.68', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 38427597486442637521', 'to': 'Счет 83889757415570699323'}, {'id': 286706711, 'state': 'EXECUTED', 'date': '2018-02-06T06:42:02.219233', 'operationAmount': {'amount': '621.37', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'MasterCard 9175985085449563', 'to': 'Счет 82781399328834147668'}, {'id': 100392079, 'state': 'EXECUTED', 'date': '2019-03-03T03:13:18.622393', 'operationAmount': {'amount': '44493.45', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на счет', 'from': 'Visa Classic 6319351940209800', 'to': 'Счет 14073196441261107791'}, {'id': 51314762, 'state': 'EXECUTED', 'date': '2018-08-25T02:58:18.764678', 'operationAmount': {'amount': '52245.30', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 4040551273087672', 'to': 'Visa Platinum 7825450883088021'}, {'id': 894961746, 'state': 'EXECUTED', 'date': '2019-08-04T20:17:25.443322', 'operationAmount': {'amount': '2523.44', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 33721541831646393763', 'to': 'Счет 68774571780974952778'}, {'id': 360577236, 'state': 'EXECUTED', 'date': '2019-09-07T07:20:13.889610', 'operationAmount': {'amount': '18536.73', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на карту', 'from': 'Maestro 4284341727554246', 'to': 'МИР 1582474475547301'}, {'id': 416017997, 'state': 'EXECUTED', 'date': '2019-05-07T01:32:37.142797', 'operationAmount': {'amount': '29033.65', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'МИР 4878656375033856', 'to': 'Maestro 6890749237669619'}, {'id': 74897425, 'state': 'EXECUTED', 'date': '2019-02-08T09:09:35.038506', 'operationAmount': {'amount': '62654.30', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 28429442875257789335', 'to': 'Счет 95473010446151855633'}, {'id': 636137913, 'state': 'EXECUTED', 'date': '2019-06-16T22:17:01.825020', 'operationAmount': {'amount': '24260.78', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на счет', 'from': 'Visa Platinum 8990850370884895', 'to': 'Счет 15574304810835774010'}, {'id': 813238385, 'state': 'EXECUTED', 'date': '2018-05-04T03:29:30.253483', 'operationAmount': {'amount': '22007.02', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на счет', 'from': 'MasterCard 3595832182277400', 'to': 'Счет 79697233246085035210'}, {'id': 854048120, 'state': 'EXECUTED', 'date': '2019-03-29T10:57:20.635567', 'operationAmount': {'amount': '30234.99', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на счет', 'from': 'Visa Classic 1203921041964079', 'to': 'Счет 34616199494072692721'}, {'id': 269462132, 'state': 'EXECUTED', 'date': '2018-08-14T05:42:30.104666', 'operationAmount': {'amount': '19010.50', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 18125798580985711166', 'to': 'Счет 98841213648056852372'}, {'id': 431131847, 'state': 'EXECUTED', 'date': '2018-05-05T01:38:56.538074', 'operationAmount': {'amount': '56071.02', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'MasterCard 9454780748494532', 'to': 'Счет 51958934737718181351'}, {'id': 15948212, 'state': 'EXECUTED', 'date': '2018-12-23T11:47:52.403285', 'operationAmount': {'amount': '47408.20', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'МИР 8665240839126074', 'to': 'Maestro 3000704277834087'}, {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890', 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'}, {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051', 'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794', 'to': 'Счет 46765464282437878125'}, {'id': 414894334, 'state': 'EXECUTED', 'date': '2019-06-30T15:11:53.136004', 'operationAmount': {'amount': '95860.47', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 59956820797131895975', 'to': 'Счет 43475624104328495820'}, {'id': 509552992, 'state': 'EXECUTED', 'date': '2019-04-19T12:02:30.129240', 'operationAmount': {'amount': '81513.74', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на карту', 'from': 'Maestro 9171987821259925', 'to': 'МИР 2052809263194182'}, {'id': 596914981, 'state': 'EXECUTED', 'date': '2018-04-16T17:34:19.241289', 'operationAmount': {'amount': '65169.27', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 1813166339376336', 'to': 'Счет 97848259954268659635'}, {'id': 879660146, 'state': 'EXECUTED', 'date': '2018-07-22T07:42:32.953324', 'operationAmount': {'amount': '92130.50', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 19628854383215954147', 'to': 'Счет 90887717138446397473'}, {'id': 390558607, 'state': 'EXECUTED', 'date': '2019-02-12T00:08:07.524972', 'operationAmount': {'amount': '16796.95', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 72645194281643232984', 'to': 'Счет 95782287258966264115'}, {'id': 902831954, 'state': 'EXECUTED', 'date': '2018-04-22T17:01:46.885252', 'operationAmount': {'amount': '84732.61', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 3530191547567121', 'to': 'Счет 46878338893256147528'}, {'id': 86608620, 'state': 'EXECUTED', 'date': '2019-08-16T04:23:41.621065', 'operationAmount': {'amount': '6004.00', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'MasterCard 8826230888662405', 'to': 'Счет 96119739109420349721'}, {'id': 232222017, 'state': 'EXECUTED', 'date': '2018-07-06T22:32:10.495465', 'operationAmount': {'amount': '37160.27', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 4062745111784804', 'to': 'Maestro 8602249654751155'}, {'id': 280743947, 'state': 'EXECUTED', 'date': '2018-09-27T14:26:24.629306', 'operationAmount': {'amount': '45653.70', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Счет 23177857685058835559', 'to': 'Счет 56363465303962313778'}, {'id': 185048835, 'state': 'EXECUTED', 'date': '2019-05-06T00:17:42.736209', 'operationAmount': {'amount': '74895.83', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 27921306202254867520', 'to': 'Счет 49884962711830774470'}, {'id': 422035015, 'state': 'EXECUTED', 'date': '2019-02-27T03:59:25.921176', 'operationAmount': {'amount': '69311.35', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'MasterCard 8847384717023026', 'to': 'Счет 85458008326755993377'}, {'id': 917824439, 'state': 'EXECUTED', 'date': '2019-07-18T12:27:13.355343', 'operationAmount': {'amount': '82139.20', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Platinum 6942697754917688', 'to': 'МИР 2956603572573342'}, {'id': 736942989, 'state': 'EXECUTED', 'date': '2019-09-06T00:48:01.081967', 'operationAmount': {'amount': '6357.56', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Gold 3654412434951162', 'to': 'Счет 59986621134048778289'}, {'id': 580054042, 'state': 'EXECUTED', 'date': '2018-06-20T03:59:34.851630', 'operationAmount': {'amount': '96350.51', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на счет', 'from': 'МИР 3766446452238784', 'to': 'Счет 86655182730188443980'}, {'id': 619287771, 'state': 'EXECUTED', 'date': '2019-08-19T16:30:41.967497', 'operationAmount': {'amount': '81150.87', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 17691325653939384901', 'to': 'Счет 49304996510329747621'}, {'id': 490100847, 'state': 'EXECUTED', 'date': '2018-12-22T02:02:49.564873', 'operationAmount': {'amount': '56516.63', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Gold 8326537236216459', 'to': 'MasterCard 6783917276771847'}, {'id': 179194306, 'state': 'EXECUTED', 'date': '2019-05-19T12:51:49.023880', 'operationAmount': {'amount': '6381.58', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'МИР 5211277418228469', 'to': 'Счет 58518872592028002662'}, {'id': 921286598, 'state': 'EXECUTED', 'date': '2018-03-09T23:57:37.537412', 'operationAmount': {'amount': '25780.71', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Счет 26406253703545413262', 'to': 'Счет 20735820461482021315'}, {'id': 957763565, 'state': 'EXECUTED', 'date': '2019-01-05T00:52:30.108534', 'operationAmount': {'amount': '87941.37', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 46363668439560358409', 'to': 'Счет 18889008294666828266'}, {'id': 667307132, 'state': 'EXECUTED', 'date': '2019-07-13T18:51:29.313309', 'operationAmount': {'amount': '97853.86', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'Maestro 1308795367077170', 'to': 'Счет 96527012349577388612'}]