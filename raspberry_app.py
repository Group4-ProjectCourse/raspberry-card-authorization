import time
import interneting as web
leds = __import__("leds-codes")
channel = __import__("arduino-communicator")

while True:
    msg = channel.read_message()
    print("[ARDUINO]: " + msg)
    if "/uuid" in msg:
        uuid = msg.split()[1]
        res_json = web.verify_uuid(uuid)
        channel.write_message(res_json['status'])
        print("[REST SERVER]: Message: " + str(res_json['message']) + "\n[REST SERVER]: Status: " + str(res_json['status']))
    elif "/password" in msg:
        splitted_text = msg.split()
        uuid = splitted_text[1]
        password = splitted_text[2]
        res_json = web.verify_card(uuid, password)
        channel.write_message(res_json['status'])
        print("[REST SERVER]: Message: " + str(res_json['message']) + "\n[REST SERVER]: Status: " + str(res_json['status']))
    elif "/led" in msg:
        color = msg.split()[1]
        if color == "green":
            leds.flash_on_green()
            time.sleep(3)
            leds.flash_off_green()
        elif color == "yellow":
            counter = 0
            while counter < 5:
                leds.flash_on_yellow()
                time.sleep(1)
                leds.flash_off_yellow()
                counter++
        elif color == "red":
            leds.flash_on_red()
            time.sleep(3)
            leds.flash_off_red()
            
            