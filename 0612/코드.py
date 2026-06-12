import tkinter as tk
import calendar
from datetime import date
from korean_lunar_calendar import KoreanLunarCalendar

# 양력 날짜를 음력 날짜로 변환하는 함수
def get_lunar(year, month, day):
    lunar = KoreanLunarCalendar()

    # 양력 날짜 설정
    lunar.setSolarDate(year, month, day)

    # 음력 월, 일 반환
    return lunar.lunarMonth, lunar.lunarDay


# 달력을 출력하는 함수
def show_calendar():

    # 기존에 출력된 달력 삭제
    for widget in calendar_frame.winfo_children():
        widget.destroy()

    # 사용자가 입력한 연도와 월 가져오기
    year = int(year_entry.get())
    month = int(month_entry.get())

    # 요일 목록
    days = ["월", "화", "수", "목", "금", "토", "일"]

    # 요일 출력
    for col, d in enumerate(days):
        tk.Label(
            calendar_frame,
            text=d,
            width=12,
            height=2,
            relief="solid",
            bg="lightgray"
        ).grid(row=0, column=col)

    # 해당 월의 달력 데이터 생성
    month_data = calendar.monthcalendar(year, month)

    # 오늘 날짜 저장
    today = date.today()

    # 주 단위로 달력 출력
    for row, week in enumerate(month_data, start=1):
        for col, day in enumerate(week):

            # 빈 칸 처리
            if day == 0:
                text = ""
                bg = "white"

            else:
                # 양력을 음력으로 변환
                lunar_month, lunar_day = get_lunar(
                    year,
                    month,
                    day
                )

                # 양력 날짜와 음력 날짜 표시
                text = f"{day}\n음 {lunar_month}/{lunar_day}"

                bg = "white"

                # 오늘 날짜면 노란색으로 강조
                if (
                    year == today.year
                    and month == today.month
                    and day == today.day
                ):
                    bg = "yellow"

            # 기본 글자색
            fg = "black"

            # 토요일은 파란색
            if col == 5:
                fg = "blue"

            # 일요일은 빨간색
            elif col == 6:
                fg = "red"

            # 날짜 칸 생성
            tk.Label(
                calendar_frame,
                text=text,
                width=12,
                height=5,
                relief="solid",
                justify="center",
                fg=fg,
                bg=bg,
                font=("맑은 고딕", 10)
            ).grid(row=row, column=col)


# ==========================
# 메인 GUI 생성
# ==========================

window = tk.Tk()

# 창 제목 설정
window.title("양력 · 음력 달력")

# 창 크기 설정
window.geometry("900x550")

# 입력 영역 프레임 생성
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

# 연도 입력 라벨
tk.Label(
    input_frame,
    text="연도"
).pack(side="left")

# 연도 입력창
year_entry = tk.Entry(
    input_frame,
    width=8
)
year_entry.pack(side="left")

# 현재 연도를 기본값으로 설정
year_entry.insert(
    0,
    str(date.today().year)
)

# 월 입력 라벨
tk.Label(
    input_frame,
    text="월"
).pack(side="left")

# 월 입력창
month_entry = tk.Entry(
    input_frame,
    width=5
)
month_entry.pack(side="left")

# 현재 월을 기본값으로 설정
month_entry.insert(
    0,
    str(date.today().month)
)

# 달력 출력 버튼
tk.Button(
    input_frame,
    text="달력 출력",
    command=show_calendar
).pack(side="left", padx=10)

# 달력이 표시될 프레임
calendar_frame = tk.Frame(window)
calendar_frame.pack()

# 프로그램 시작 시 현재 달력 자동 출력
show_calendar()

# GUI 실행
window.mainloop()
