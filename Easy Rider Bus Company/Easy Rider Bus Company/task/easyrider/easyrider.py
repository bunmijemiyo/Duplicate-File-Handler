
import json
import re
from datetime import datetime

class Bus:

    def __init__(self, bus_data):
        self.bus_data = bus_data
        self.bus_id = 0
        self.stop_id = 0
        self.stop_name = 0
        self.next_stop = 0
        self.stop_type = 0
        self.a_time = 0
        self.sum_of_errors = 0
        self.one_two_eight = 0
        self.two_five_six = 0
        self.five_one_two = 0
        self.one_two_four = 0

    def wrong_data(self):
        for data in self.bus_data:
            for key, value in data.items():
                if key == "bus_id":
                    if value is False or type(value) != int:
                        self.bus_id += bus_data.count(data)
                elif key == "stop_id":
                    if value is False or type(value) != int:
                        self.stop_id += bus_data.count(data)
                elif key == "stop_name":
                    if value != "" and type(value) == str:
                        pass
                    else:
                        self.stop_name += bus_data.count(data)
                elif key == "next_stop":
                    if value is False or type(value) != int:
                        self.next_stop += bus_data.count(data)
                elif key == "stop_type":
                    if value not in ["F", "O", "S", ""]:
                        self.stop_type += bus_data.count(data)
                elif key == "a_time":
                    if value != "" and type(value) == str:
                        pass
                    else:
                        self.a_time += bus_data.count(data)

    def result(self):
        self.sum_of_errors += sum(
            [self.bus_id, self.stop_id, self.stop_name, self.next_stop, self.stop_type, self.a_time])
        print(f"Type and required field validation: {self.sum_of_errors} errors")
        print(f"bus_id: {self.bus_id}\nstop_id: {self.stop_id}\nstop_name: {self.stop_name}\nnext_stop: "
              f"{self.next_stop}\nstop_type: {self.stop_type}\na_time: {self.a_time}")

    def wrong_format(self):
        for data in self.bus_data:
            for key, value in data.items():
                if key == "stop_name":
                    if value != "" and type(value) == str and re.match('[A-Z]', value)\
                            is not None and (value.endswith(" Street") or value.endswith(" Boulevard")
                                             or value.endswith(" Avenue") or value.endswith(" Road")):
                        pass
                    else:
                        self.stop_name += bus_data.count(data)
                elif key == "stop_type":
                    if value not in ["F", "O", "S", ""]:
                        self.stop_type += bus_data.count(data)
                elif key == "a_time":
                    if value != "" and type(value) == str and re.match('[0-2][0-9]:[0-5][0-9]$', value) is not None:
                        pass
                    else:
                        self.a_time += bus_data.count(data)

    def wrong_format_outcome(self):
        self.sum_of_errors += sum([self.stop_name, self.stop_type, self.a_time])
        print(f"Format validation: {self.sum_of_errors} errors")
        print(f"stop_name: {self.stop_name}\nstop_type: {self.stop_type}\na_time: {self.a_time}")

    def bus_line_info(self):
        for data in self.bus_data:
            for key, value in data.items():
                if key == "bus_id":
                    if value is False or type(value) != int:
                        pass
                    else:
                        if int(value) == 128:
                            self.one_two_eight += 1
                        elif int(value) == 256:
                            self.two_five_six += 1
                        elif int(value) == 512:
                            self.five_one_two += 1
                        elif int(value) == 1024:
                            self.one_two_four += 1

    def bus_line_printout(self):
        print("Line names and number of stops:")
        print(f"bus_id: 128, stops: {self.one_two_eight}\nbus_id: 256, stops: {self.two_five_six}\nbus_id: 512, stops: {self.five_one_two}\nbus_id: 1024, stops: {self.one_two_four}")

    def special_stops(self):
        see = []
        for i in self.bus_data:
            see.append([i["bus_id"], i["stop_name"], i["stop_type"]])
        box_128 = []
        box_256 = []
        box_512 = []
        for i in see:
            if i[0] == 128:
                box_128.append(i[2])
            elif i[0] == 256:
                box_256.append(i[2])
            elif i[0] == 512:
                box_512.append(i[2])
        if "S" not in box_128 or "F" not in box_128:
            print("There is no start or end stop for the line: 128.")
        elif "S" not in box_512 or "F" not in box_512:
            print("There is no start or end stop for the line: 512.")
        elif "S" not in box_256 or "F" not in box_256:
            print("There is no start or end stop for the line: 256.")

        else:
            start_stops = [i[1] for i in see if i[2] == "S"]
            journey_info = [i[1] for i in see]
            transfer_stops = {i: journey_info.count(i) for i in journey_info if journey_info.count(i) > 1}
            transfer_list = [k for k in transfer_stops]
            finish_stops = {i[1] for i in see if i[2] == "F"}
            finish_list = [k for k in finish_stops]
            print(f"Start stops: {len(start_stops)} {sorted(start_stops)}")
            print(f"Transfer stops: {len(transfer_list)} {sorted(transfer_list)}")
            print(f"Finish stops: {len(finish_list)} {sorted(finish_list)}")

    def arrival_info(self):
        d_bus_id = {}  # {512: {'S', 'F'}}
        flag = False
        print('Arrival time test:')
        trash = []
        for i in self.bus_data:
            current_time = datetime.strptime(i['a_time'], '%H:%M')
            if i['bus_id'] not in d_bus_id:
                d_bus_id[i['bus_id']] = [current_time]
            elif current_time > d_bus_id[i['bus_id']][-1]:
                d_bus_id[i['bus_id']].append(current_time)
            elif i['bus_id'] not in trash:
                print(f'bus_id line {i["bus_id"]}: wrong time on station {i["stop_name"]}')
                trash.append(i['bus_id'])
                flag = True
        if not flag:
            print('OK')

    def on_demand(self):
        see = []
        for i in self.bus_data:
            see.append([i["bus_id"], i["stop_name"], i["stop_type"]])
        print(see)
        box_128 = []
        box_256 = []
        box_512 = []
        result_box = []
        for i in see:
            if i[0] == 128:
                box_128.append(i[2])
            elif i[0] == 256:
                box_256.append(i[2])
            elif i[0] == 512:
                box_512.append(i[2])

        start_stops = [i[1] for i in see if i[2] == "S"]
        journey_info = [i[1] for i in see]
        transfer_stops = {i: journey_info.count(i) for i in journey_info if journey_info.count(i) > 1}
        transfer_list = [k for k in transfer_stops]
        finish_stops = {i[1] for i in see if i[2] == "F"}
        finish_list = [k for k in finish_stops]
        print("On demand stops test:")
        for i in see:
            if i[1] in finish_list or i[1] in transfer_list or i[1] in start_stops:
                if i[2] == "O":
                    result_box.append(i[1])
        if len(result_box) == 0:
            print("OK")
        else:
            print(f"Wrong stop type: {sorted(result_box)}")


bus_data = json.loads(input())
box = Bus(bus_data)
box.on_demand()
