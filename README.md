# NXP_IMXRT1050-EVKB_FreeRTOS


## Project Description

Progress : The project is incomplete . FreeRTOS is implementable , evkbimxrt1050_freertos_hello_practiceexample (1) is built and run successfully in board. Code provided in repository is modified from (1) , it can be built but does not run during debug sessions.

Following is the error encountered.
```bash
Program stopped.
0x60008394 in ShiftRows (state=0xe3df94dc) at ../source/aes.c:294
294	    (*state)[0][3] = (*state)[3][3];
Note: automatically using hardware breakpoints for read-only addresses.
```

Objective : Collect traces,plaintext and ciphertext for Side Channel Attack on AES128 encryption algorithm in ECB mode.The computer collects traces,plaintext and ciphertext for Side Channel Attack.

## Directions
Buil and run

## Resources
[Setting Up Environment and Project in MCUXpresso IDE](https://youtu.be/h94HkUv9Iq4)
