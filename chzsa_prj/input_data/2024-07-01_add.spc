# doctype: python dict
# Структура файла: словарь, ключ Document - данные о документе (включая хеш содержимого), ключ Content - содержимое.
# В Context может быть обновление данных на машину или какой-либо другой узел (даже другой машины). (Как применять =?)

specification = {
    "Document": {
        "Document number": "0000",
        "Date": "2022-03-09",
        "Time": "09:00:00",
        "Timezone": "Europe/Moscow",
        "Author": "Чебоксарский завод силовых агрегатов",
        "Hash": {
            "Hashed area": "Content",
            "Hash algorithm": "SHA-256",
            "Hash presentation form": "hex.",
            "Hash": "8517e447c8337a134c8f97bea91d45219d3271a7bc97a38445057047905798d3",
            "Source of the check hash": "https://chzsa.ru/about/ext_up_docs"
        },
    },
    "Content": {
        "Machine": {
            "Model": "ПД1,5",
            "Serial number": "0017",
            "Nodes": {
                "Engine": {
                    "Model": "Kubota D1803",
                    "Serial number": "7ML1035",
                    "Produced date": "2022-03-01",
                    "Source time (h)": 3000
                },
                "Transmission": {
                    "Model": "10VA-00105",
                    "Serial number": "21D0108251",
                    "Produced date": "2022-03-01",
                    "Source time (h)": 3000
                },
                "Drive bridge": {
                    "Model": "20VA-00101",
                    "Serial number": "21D0107997",
                    "Produced date": "2022-03-01",
                    "Source time (h)": 3000
                },
                "Controlled bridge": {
                    "Model": "VS20-00001",
                    "Serial number": "21D0093265",
                    "Produced date": "2022-03-01",
                    "Source time (h)": 3000
                },
                "Complete set": {
                    "Position 1": {
                        "Description": "Hydraulic lines with quick-release connection",
                        "Serial number": "none",
                        "Source time": "none"
                    },
                    "Position 2": {
                        "Description": "Additional cabin installation",
                        "Serial number": "none",
                        "Source time": "none"
                    }
                }
            },
            "Operational information": {
                "Delivery agreement number": "none",
                "Shipment date": "2022-03-09",
                "End user": "ИП Трудников С.В.",
                "User address": "п. Знаменский, Респ. Марий Эл",
                "Client": "ИП Трудников С.В.",
                "Service company": "ООО Промышленная техника"
            }
        }
    }
}
