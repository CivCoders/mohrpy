# Mohrpy

Script for plotting Mohr's circle for a system of stess. Written in python using matplotlib package. For more details about Mohr's circle goto https://en.wikipedia.org/wiki/Mohr%27s_circle

![Screenshot](https://postimg.org/image/zcv4uqvx9)

Follow the instructions to run script

```bash
$ git clone https://github.com/CivCoders/mohrpy.git
$ pip install matplotlib
>> No need to run this if you already installed matplotlib on your machine.

$ python main.py

    ===================================================
    Mohrpy - Open source Mohr's Circle plotting program.
    ===================================================

    Enter value of different stress for system of stress.
    (-ve value for compressive stress.)
    Press Ctrl+C for exit.


>> Enter sigma_x: 100
>> Enter sigma_y: 100
>> Enter angle of inclination (in degrees): 0
  (Please enter 0 if tau_xy doesn't exists.)
>> Enter tau_xy: 0
```