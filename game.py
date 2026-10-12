#!/usr/bin/env python3
"""1~100 사이 숫자 맞히기 게임 (표준 라이브러리만 사용)."""

import random

LOW, HIGH = 1, 100


def read_guess():
    while True:
        text = input(f"{LOW}~{HIGH} 사이의 숫자를 입력하세요: ").strip()
        try:
            guess = int(text)
        except ValueError:
            print("숫자만 입력해 주세요.")
            continue
        if not LOW <= guess <= HIGH:
            print(f"{LOW}부터 {HIGH} 사이의 숫자를 입력해 주세요.")
            continue
        return guess


def play_round():
    answer = random.randint(LOW, HIGH)
    attempts = 0
    print(f"\n{LOW}부터 {HIGH} 사이의 숫자를 하나 골랐어요. 맞혀 보세요!")
    while True:
        guess = read_guess()
        attempts += 1
        if guess < answer:
            print("더 크게!")
        elif guess > answer:
            print("더 작게!")
        else:
            print(f"정답입니다! {attempts}번 만에 맞혔어요.")
            return


def ask_again():
    while True:
        text = input("다시 하시겠어요? (y/n): ").strip().lower()
        if text in ("y", "yes", "ㅛ", "네", "예", "응"):
            return True
        if text in ("n", "no", "ㅜ", "아니오", "아니요", "아니"):
            return False
        print("y 또는 n으로 입력해 주세요.")


def main():
    print("=== 숫자 맞히기 게임 ===")
    try:
        while True:
            play_round()
            if not ask_again():
                break
    except (KeyboardInterrupt, EOFError):
        print()
    print("게임을 종료합니다. 고마워요!")


if __name__ == "__main__":
    main()
