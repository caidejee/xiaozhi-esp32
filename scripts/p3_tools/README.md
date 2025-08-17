# P3 audio format conversion and playback tool

This directory contains two Python scripts for processing P3 format audio files.：

## 1. audio conversion tool (convert_audio_to_p3.py)

Converts a standard audio file to P3 format (a 4-byte header and a streaming structure of Opus packets) and performs loudness normalization.

### How to use

```bash
python convert_audio_to_p3.py <输入音频文件> <输出P3文件> [-l LUFS] [-d]
```

Among them, optional options`-l` Used to specify the target loudness for loudness normalization, the default is -16 LUFS; optional `-d` 可Loudness normalization can be disabled.

If the input audio file meets any of the following conditions, it is recommended to use `-d` Disable Loudness Normalization：
- Audio too short
- The audio has been adjusted for loudness
- Audio comes from default TTS（The default loudness of the TTS currently used by Xiaozhi is -16 LUFS）

For example：
```bash
python convert_audio_to_p3.py input.mp3 output.p3
```

## 2. P3 audio playback tool (play_p3.py)

Play P3 audio files。

### characteristic

- Decode and play P3 format audio files
- Apply a fade-out effect when playback ends or the user interrupts the playback to avoid audio distortion.
- Supports specifying the file to play via command-line parameters.

### How to use

```bash
python play_p3.py <P3文件路径>
```

For example：
```bash
python play_p3.py output.p3
```

## 3. Audio Reconversion Tool (convert_p3_to_audio.py)

Convert P3 format back to normal audio file。

### How to use

```bash
python convert_p3_to_audio.py <Import P3 file> <Output audio files>
```

The output audio file needs to have an extension。

For example：
```bash
python convert_p3_to_audio.py input.p3 output.wav
```
## 4. Audio/P3 batch conversion tool

A graphical tool that supports batch conversion of audio to P3 and P3 to audio

![](./img/img.png)

### How to use:
```bash
python batch_convert_gui.py
```

## Dependencies on installation

Before using these scripts, make sure you have the required Python libraries installed:

```bash
pip install librosa opuslib numpy tqdm sounddevice pyloudnorm soundfile
```

Or use the provided requirements.txt file：

```bash
pip install -r requirements.txt
```

## PP3 format description

The P3 format is a simple streaming audio format with the following structure:
- Each audio frame consists of a 4-byte header and an Opus-encoded data packet
- Header format: [1-byte type, 1-byte reserved, 2-byte length]
- The sampling rate is fixed at 16000 Hz, mono
- Each frame is 60ms long
