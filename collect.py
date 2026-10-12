#!/usr/bin/env python3
"""라즈베리파이 CPU 온도를 30초마다 읽어 data.csv에 기록한다."""

import csv
import os
import time
from datetime import datetime

TEMP_PATH = "/sys/class/thermal/thermal_zone0/temp"
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.csv")
INTERVAL_SEC = 30


def read_temp_c():
    with open(TEMP_PATH) as f:
        return int(f.read().strip()) / 1000.0  # 밀리도(m℃) → ℃


def append_row(timestamp, temp_c):
    write_header = not os.path.exists(CSV_PATH) or os.path.getsize(CSV_PATH) == 0
    with open(CSV_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["timestamp", "temp_c"])
        writer.writerow([timestamp, f"{temp_c:.1f}"])


def main():
    print(f"수집 시작: {INTERVAL_SEC}초 간격 → {CSV_PATH} (Ctrl+C로 종료)")
    while True:
        start = time.monotonic()
        try:
            timestamp = datetime.now().isoformat(timespec="seconds")
            temp_c = read_temp_c()
            append_row(timestamp, temp_c)
            print(f"{timestamp}  {temp_c:.1f}℃", flush=True)
        except Exception as e:
            # 어떤 오류가 나도 기록만 하고 다음 주기에 다시 시도한다
            print(f"[오류] {datetime.now().isoformat(timespec='seconds')} {e!r}", flush=True)
        elapsed = time.monotonic() - start
        time.sleep(max(0, INTERVAL_SEC - elapsed))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n수집 종료")
