pins.digital_write_pin(DigitalPin.P2, 0)
pins.digital_write_pin(DigitalPin.P11, 0)
pins.digital_write_pin(DigitalPin.P8, 0)
pins.digital_write_pin(DigitalPin.P5, 0)
pins.set_pull(DigitalPin.P16, PinPullMode.PULL_DOWN)
pins.set_pull(DigitalPin.P15, PinPullMode.PULL_DOWN)
pins.set_pull(DigitalPin.P14, PinPullMode.PULL_DOWN)
pins.set_pull(DigitalPin.P13, PinPullMode.PULL_DOWN)

def on_forever():
    pins.digital_write_pin(DigitalPin.P2, 0)
    while pins.digital_read_pin(DigitalPin.P16) == 0:
        basic.show_string("1")
    while pins.digital_read_pin(DigitalPin.P15) == 0:
        basic.show_string("4")
    while pins.digital_read_pin(DigitalPin.P14) == 0:
        basic.show_string("7")
    while pins.digital_read_pin(DigitalPin.P13) == 0:
        basic.show_string("*")
    pins.digital_write_pin(DigitalPin.P2, 1)
    pins.digital_write_pin(DigitalPin.P11, 0)
    while pins.digital_read_pin(DigitalPin.P16) == 0:
        basic.show_string("2")
    while pins.digital_read_pin(DigitalPin.P15) == 0:
        basic.show_string("5")
    while pins.digital_read_pin(DigitalPin.P14) == 0:
        basic.show_string("8")
    while pins.digital_read_pin(DigitalPin.P13) == 0:
        basic.show_string("0")
    pins.digital_write_pin(DigitalPin.P11, 1)
    pins.digital_write_pin(DigitalPin.P8, 0)
    while pins.digital_read_pin(DigitalPin.P16) == 0:
        basic.show_string("3")
    while pins.digital_read_pin(DigitalPin.P15) == 0:
        basic.show_string("6")
    while pins.digital_read_pin(DigitalPin.P14) == 0:
        basic.show_string("9")
    while pins.digital_read_pin(DigitalPin.P13) == 0:
        basic.show_string("#")
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.digital_write_pin(DigitalPin.P5, 0)
    while pins.digital_read_pin(DigitalPin.P16) == 0:
        basic.show_string("A")
    while pins.digital_read_pin(DigitalPin.P15) == 0:
        basic.show_string("B")
    while pins.digital_read_pin(DigitalPin.P14) == 0:
        basic.show_string("C")
    while pins.digital_read_pin(DigitalPin.P13) == 0:
        basic.show_string("D")
    pins.digital_write_pin(DigitalPin.P5, 1)
    basic.pause(20)
basic.forever(on_forever)
