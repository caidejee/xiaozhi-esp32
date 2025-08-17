# Sound testing
This GUI is used to test the conversion of `pcm` sent back by Xiaozhi device via `udp` to time domain/frequency domain. It can save the sound of window length and be used to judge the frequency distribution of noise and test the accuracy of ASCII transmission of sound waves.

Firmware testing requires enabling `USE_AUDIO_DEBUGGER` and setting `AUDIO_DEBUG_UDP_SERVER` to the local address.
Sound wave `demod` can be used to output sound wave tests using `sonic_wifi_config.html` or by uploading it to PinMe's [Xiaozhi Sonic Wave Network Configuration](https://iqf7jnhi.pinit.eth.limo).

# Sound Decoding Test Record

> `✓` indicates successful decoding when receiving raw PCM signals via I2S DIN, `x` indicates stable decoding requires noise reduction or additional processing, and `X` indicates poor decoding even after noise reduction (partial decoding may be possible but will be very unstable).
> Some ADCs require more refined noise reduction adjustments during the I2C configuration phase. Due to the lack of universality of the device, we are currently testing only according to the config provided in the boards. 

| Board | ADC | MIC | Effect | Notes |
| ---- | ---- | --- | --- | ---- |
| bread-compact | INMP441 | Integrated MEMEMIC | ✓ |
| atk-dnesp32s3-box | ES8311 | | ✓ |
| magiclick-2p5 | ES8311 | | ✓ |
| lichuang-dev  | ES7210 | | △ | INPUT_REFERENCE needs to be turned off during testing
| kevin-box-2 | ES7210 | | △ | INPUT_REFERENCE needs to be turned off during testing
| m5stack-core-s3 | ES7210 | | △ | INPUT_REFERENCE needs to be turned off during testing
| xmini-c3 | ES8311 | | △ | Noise reduction required
| atoms3r-echo-base | ES8311 | | △ | Noise reduction required
| atk-dnesp32s3-box0 | ES8311 | | X | Can receive and decode, but the packet loss rate is very high
| movecall-moji-esp32s3 | ES8311 | | X | Can receive and decode, but the packet loss rate is very high
