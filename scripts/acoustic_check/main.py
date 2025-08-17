#!/usr/bin/env python3
"""
Main program of audio real-time monitoring and drawing system
Based on Qt GUI + Matplotlib + UDP receiving + AFSK decoding string
"""

import sys
import asyncio
from graphic import main

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("程序被用户中断")
    except Exception as e:
        print(f"程序执行出错: {e}")
        sys.exit(1)
