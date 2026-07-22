# hackropad-ver-1.0
This github repo has all the files I used to make a macropad for the average Hackclub user. My macropad contains an OLED and a 3x3 keypad.

The following is a schematic made on KiCAD.

<img width="525" height="361" alt="image" src="https://github.com/user-attachments/assets/7e93ce68-733f-4632-937f-c7f1aa9bd1d8" />

The following is the PCB made on KiCAD.

<img width="342" height="347" alt="image" src="https://github.com/user-attachments/assets/fc8561f9-5dba-4e2b-a11a-0c2a8073bb40" />

The following image is the final assembled version (CAD not the real one, I will update my readme.md once I finish building the actual Hackropad).

<img width="596" height="323" alt="image" src="https://github.com/user-attachments/assets/bba32df4-9e8c-4567-9d5a-633fdf05e9ed" />

The following is the BOM for the Hackropad

[Hack_Club_Macropad.csv](https://github.com/user-attachments/files/30129260/Hack_Club_Macropad.csv)

The following is a table of what the BOM is:
|Reference                          |Qty|Value                |Footprint                                                         |
|-----------------------------------|---|---------------------|------------------------------------------------------------------|
|D1,D2,D3,D4,D5,D6,D7,D8,D9         |9  |D                    |Diode_THT:D_DO-41_SOD81_P7.62mm_Horizontal                        |
|SW1,SW2,SW3,SW4,SW5,SW6,SW7,SW8,SW9|9  |SW_Push              |Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB                     |
|U1                                 |1  |MOUDLE-SEEEDUINO-XIAO|HackClub KiCAD Care Package:XIAO-Generic-Hybrid-14P-2.54-21X17.8MM|
|U2                                 |1  |ER_OLEDM0.91_1x-I2C  |Display:ER_OLEDM0.91_1x-I2C                                       |
The D is the diode, sw push are the keys, and U1 is the Moudle Seeduino Xiao (the main MCU), the U2 is the OLED.
