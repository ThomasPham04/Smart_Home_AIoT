from aiot_ir_receiver import *
from aiot_lcd1602 import LCD1602
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
import time
import music
from mqtt import *
from machine import RTC
import ntptime
from event_manager import *
import sys
import uselect
from aiot_rgbled import RGBLed
from machine import Pin, SoftI2C
from aiot_dht20 import DHT20

aiot_ir_rx = IR_RX(Pin(pin1.pin, Pin.IN)); aiot_ir_rx.start();

aiot_lcd1602 = LCD1602()

# Mô tả hàm này...
def Ki_C3_AAm_Tra_M_E1_BA_ADt_M_C3_A3():
  global cmd, PASS, ADMIN, STATUS, count, led, aiot_lcd1602, aiot_dht20, aiot_ir_rx, tiny_rgb
  if aiot_ir_rx.get_code() == IR_REMOTE_1:
    PASS = str(PASS) + '1'
    aiot_lcd1602.move_to(count, 1)
    aiot_lcd1602.putstr('*')
    count = (count if isinstance(count, (int, float)) else 0) + 1
  if aiot_ir_rx.get_code() == IR_REMOTE_2:
    PASS = str(PASS) + '2'
    aiot_lcd1602.move_to(count, 1)
    aiot_lcd1602.putstr('*')
    count = (count if isinstance(count, (int, float)) else 0) + 1
  if aiot_ir_rx.get_code() == IR_REMOTE_3:
    PASS = str(PASS) + '3'
    aiot_lcd1602.move_to(count, 1)
    aiot_lcd1602.putstr('*')
    count = (count if isinstance(count, (int, float)) else 0) + 1
  if aiot_ir_rx.get_code() == IR_REMOTE_3:
    ADMIN = str(ADMIN) + '3'
    aiot_lcd1602.move_to(count, 1)
    aiot_lcd1602.putstr('*')
    count = (count if isinstance(count, (int, float)) else 0) + 1
  if aiot_ir_rx.get_code() == IR_REMOTE_4:
    ADMIN = str(ADMIN) + '4'
    aiot_lcd1602.move_to(count, 1)
    aiot_lcd1602.putstr('*')
    count = (count if isinstance(count, (int, float)) else 0) + 1
  if aiot_ir_rx.get_code() == IR_REMOTE_5:
    ADMIN = str(ADMIN) + '5'
    aiot_lcd1602.move_to(count, 1)
    aiot_lcd1602.putstr('*')
    count = (count if isinstance(count, (int, float)) else 0) + 1
  if aiot_ir_rx.get_code() == IR_REMOTE_6:
    ADMIN = str(ADMIN) + '6'
    aiot_lcd1602.move_to(count, 1)
    aiot_lcd1602.putstr('*')
    count = (count if isinstance(count, (int, float)) else 0) + 1
  if aiot_ir_rx.get_code() == IR_REMOTE_F:
    if PASS == ADMIN:
      pin3.servo_write(90)
      time.sleep_ms(2000)
      pin3.servo_write(0)
      pin3.servo_release()
    else:
      pin3.servo_write(0)
      PASS = '0'
      pin3.servo_release()
    aiot_lcd1602.move_to(9, 1)
    aiot_lcd1602.putstr('______')
  aiot_ir_rx.clear_code()

# Mô tả hàm này...
def Thay__C4_90_E1_BB_95i_M_E1_BA_ADt_M_C3_A3():
  global cmd, PASS, ADMIN, STATUS, count, led, aiot_lcd1602, aiot_dht20, aiot_ir_rx, tiny_rgb
  if aiot_ir_rx.get_code() == IR_REMOTE_1:
    music.play(['C3:1'], wait=True)
    ADMIN = str(ADMIN) + '1'
    aiot_lcd1602.move_to(count, 0)
    aiot_lcd1602.putstr('*')
    count = (count if isinstance(count, (int, float)) else 0) + 1
  if aiot_ir_rx.get_code() == IR_REMOTE_2:
    music.play(['C3:1'], wait=True)
    ADMIN = str(ADMIN) + '2'
    count = (count if isinstance(count, (int, float)) else 0) + 1
  if aiot_ir_rx.get_code() == IR_REMOTE_3:
    music.play(['C3:1'], wait=True)
    ADMIN = str(ADMIN) + '3'
    count = (count if isinstance(count, (int, float)) else 0) + 1
  if aiot_ir_rx.get_code() == IR_REMOTE_4:
    music.play(['C3:1'], wait=True)
    ADMIN = str(ADMIN) + '4'
    count = (count if isinstance(count, (int, float)) else 0) + 1
  if aiot_ir_rx.get_code() == IR_REMOTE_5:
    music.play(['C3:1'], wait=True)
    ADMIN = str(ADMIN) + '5'
    count = (count if isinstance(count, (int, float)) else 0) + 1
  if aiot_ir_rx.get_code() == IR_REMOTE_6:
    music.play(['C3:1'], wait=True)
    ADMIN = str(ADMIN) + '6'
    count = (count if isinstance(count, (int, float)) else 0) + 1
  if aiot_ir_rx.get_code() == IR_REMOTE_F:
    count = 0
    STATUS = 0
    PASS = ''
    aiot_lcd1602.move_to(9, 1)
    aiot_lcd1602.putstr('______')
  aiot_ir_rx.clear_code()

event_manager.reset()

# Mô tả hàm này...
def Hi_E1_BB_83n_th_E1_BB_8B():
  global cmd, PASS, ADMIN, STATUS, count, led, aiot_lcd1602, aiot_dht20, aiot_ir_rx, tiny_rgb
  aiot_lcd1602.move_to(0, 0)
  aiot_lcd1602.putstr(('%0*d' % (2, RTC().datetime()[4])))
  aiot_lcd1602.move_to(2, 0)
  aiot_lcd1602.putstr(':')
  aiot_lcd1602.move_to(3, 0)
  aiot_lcd1602.putstr(('%0*d' % (2, RTC().datetime()[5])))
  aiot_lcd1602.move_to(5, 0)
  aiot_lcd1602.putstr(':')
  aiot_lcd1602.move_to(6, 0)
  aiot_lcd1602.putstr(('%0*d' % (2, RTC().datetime()[6])))
  aiot_lcd1602.move_to(10, 0)
  aiot_lcd1602.putstr(('%0*d' % (2, RTC().datetime()[2])))
  aiot_lcd1602.move_to(12, 0)
  aiot_lcd1602.putstr('/')
  aiot_lcd1602.move_to(13, 0)
  aiot_lcd1602.putstr(('%0*d' % (2, RTC().datetime()[1])))

def on_event_timer_callback_I_b_T_h_d():
  global cmd, PASS, ADMIN, STATUS, count, led
  if STATUS == 0:
    Ki_C3_AAm_Tra_M_E1_BA_ADt_M_C3_A3()
  else:
    Thay__C4_90_E1_BB_95i_M_E1_BA_ADt_M_C3_A3()
  if count > '6':
    count = 9

event_manager.add_timer_event(100, on_event_timer_callback_I_b_T_h_d)

def read_terminal_input():
  spoll=uselect.poll()        # Set up an input polling object.
  spoll.register(sys.stdin, uselect.POLLIN)    # Register polling object.

  input = ''
  if spoll.poll(0):
    input = sys.stdin.read(1)

    while spoll.poll(0):
      input = input + sys.stdin.read(1)

  spoll.unregister(sys.stdin)
  return input

tiny_rgb = RGBLed(pin0.pin, 4)

def on_event_timer_callback_y_q_a_g_S():
  global cmd, PASS, ADMIN, STATUS, count, led
  cmd = read_terminal_input()
  if cmd == '0':
    tiny_rgb.show(0, hex_to_rgb('#000000'))
    led = 0
  if cmd == '1':
    tiny_rgb.show(0, hex_to_rgb('#ffffff'))
    led = 1
  if led == 1:
    if cmd == '2':
      tiny_rgb.show(0, hex_to_rgb('#0000ff'))
    if cmd == '3':
      tiny_rgb.show(0, hex_to_rgb('#ff0000'))
    if cmd == '4':
      tiny_rgb.show(0, hex_to_rgb('#00ff00'))
    if cmd == '5':
      tiny_rgb.show(0, hex_to_rgb('#ffff00'))
  if cmd == '6':
    pin3.servo_write(90)
    time.sleep_ms(2000)
    pin3.servo_write(0)
    pin3.servo_release()
    aiot_lcd1602.move_to(0, 1)
    aiot_lcd1602.putstr('OPENED')
  if cmd == '7':
    pin3.servo_write(0)
    pin3.servo_release()
    aiot_lcd1602.move_to(0, 1)
    aiot_lcd1602.putstr('CLOSED')
  if cmd == '8':
    pin14.write_analog(round(translate(0, 0, 100, 0, 1023)))
  if cmd == '9':
    pin14.write_analog(round(translate(10, 0, 100, 0, 1023)))
  if cmd == '10':
    pin14.write_analog(round(translate(20, 0, 100, 0, 1023)))
  if cmd == '11':
    pin14.write_analog(round(translate(30, 0, 100, 0, 1023)))
  if cmd == '12':
    pin14.write_analog(round(translate(40, 0, 100, 0, 1023)))
  if cmd == '13':
    pin14.write_analog(round(translate(50, 0, 100, 0, 1023)))
  if cmd == '14':
    pin14.write_analog(round(translate(60, 0, 100, 0, 1023)))
  if cmd == '15':
    pin14.write_analog(round(translate(70, 0, 100, 0, 1023)))
  if cmd == '16':
    pin14.write_analog(round(translate(80, 0, 100, 0, 1023)))
  if cmd == '17':
    pin14.write_analog(round(translate(90, 0, 100, 0, 1023)))
  if cmd == '18':
    pin14.write_analog(round(translate(100, 0, 100, 0, 1023)))
  if cmd == 'F':
    Thay__C4_90_E1_BB_95i_M_E1_BA_ADt_M_C3_A3()

event_manager.add_timer_event(200, on_event_timer_callback_y_q_a_g_S)

aiot_dht20 = DHT20()

def on_event_timer_callback_f_u_G_H_k():
  global cmd, PASS, ADMIN, STATUS, count, led
  aiot_dht20.read_dht20()
  print((''.join([str(x) for x in ['!1:TEMP:', aiot_dht20.dht20_temperature(), '#', '!1:HUMID:', aiot_dht20.dht20_humidity(), '#', '!1:LIGHT:', round(translate((pin2.read_analog()), 0, 4095, 0, 100)), '#']])), end =' ')

event_manager.add_timer_event(30000, on_event_timer_callback_f_u_G_H_k)

if True:
  mqtt.connect_wifi('ACLAB', 'ACLAB2023')
  mqtt.connect_broker(server='io.adafruit.com', port=1883, username='thuyenpham', password='aio_ZRGu75gBUsCfaAQX0xesrjGKmyNp')
  ntptime.settime()
  (year, month, mday, week_of_year, hour, minute, second, milisecond) = RTC().datetime()
  RTC().init((year, month, mday, week_of_year, hour+7, minute, second, milisecond))
  PASS = '123'
  led = 0
  count = 9
  ADMIN = '123'
  STATUS = 0
  display.scroll('OK')
  aiot_lcd1602.move_to(0, 1)
  aiot_lcd1602.putstr('CLOSED')
  aiot_lcd1602.move_to(9, 1)
  aiot_lcd1602.putstr('______')

while True:
  Hi_E1_BB_83n_th_E1_BB_8B()
  mqtt.check_message()
  event_manager.run()
  time.sleep_ms(1000)
  time.sleep_ms(10)
