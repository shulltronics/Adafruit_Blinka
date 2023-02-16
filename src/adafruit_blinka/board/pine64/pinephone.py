# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""Pin definitions for the Pine64."""

from adafruit_blinka.microcontroller.allwinner.a64 import pin

#RED_LED   = pin.PD19
#GREEN_LED = pin.PD18
#BLUE_LED  = pin.PD20
MOTOR     = pin.PD2
FLASH     = pin.PC3
INT       = pin.PL12

# TODO: find pin map for rear pogo connectors
# SDA = D2
# SCL = D3
# INT = ?

# TODO: maybe these could be mapped to headphone UART?
# UART_TX = D14
# UART_RX = D15
# UART3_TX = pin.PD0
# UART3_RX = pin.PD1
# UART4_TX = pin.PD2
# UART4_RX = pin.PD3
