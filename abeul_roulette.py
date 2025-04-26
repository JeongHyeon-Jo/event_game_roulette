import tkinter as tk
from tkinter import messagebox
import random

# 라인 종류
lines = ['상단', '정글', '미드', '원딜', '서폿']

# 팀 이름 저장 리스트
team1_entries = []
team2_entries = []

# 색상 설정
background_color = 'black'
text_color = '#FF6B81'  # 코럴핑크
entry_bg_color = '#333333'  # 입력창 어두운 회색
entry_fg_color = 'white'

# 2글자 입력 제한 함수
def limit_input_length(P):
    return len(P) <= 2

# 결과 출력
def start_roulette():
    team1 = [entry.get() for entry in team1_entries]
    team2 = [entry.get() for entry in team2_entries]

    if '' in team1 or '' in team2:
        messagebox.showerror("오류", "모든 이름을 입력해주세요!")
        return

    result_text.delete('1.0', tk.END)  # 결과창 초기화

    def assign_roles(team):
        assigned = []
        available_lines = lines.copy()
        random.shuffle(available_lines)
        for name in team:
            line = available_lines.pop()
            tier = random.randint(1, 6)
            if tier == 6:
                other_lines = [l for l in lines if l != line]
                extra_line = random.choice(other_lines)
                assigned.append((name, line, tier, extra_line))
            else:
                assigned.append((name, line, tier, ""))
        return assigned

    team1_result = assign_roles(team1)
    team2_result = assign_roles(team2)

    def print_team_result(team_name, team_result):
        result_text.insert(tk.END, f"=============== {team_name} ===============\n")
        result_text.insert(tk.END, f"| {'팀원'.center(4)} | {'라인'.center(4)} | {'티어'.center(4)} | {'6티어'.center(4)} |\n")
        result_text.insert(tk.END, f"===================================\n")
        for member in team_result:
            name, line, tier, extra_line = member
            name_str = str(name).center(6)
            line_str = str(line).center(6)
            tier_str = f"{tier}티어".center(6)
            extra_line_str = str(extra_line).center(7) if extra_line else " ".center(8)
            result_text.insert(tk.END, f"|{name_str}|{line_str}|{tier_str}|{extra_line_str}|\n")
        result_text.insert(tk.END, "\n")

    print_team_result("1팀", team1_result)
    print_team_result("2팀", team2_result)

    # 결과 전체를 가운데 정렬
    result_text.tag_add('center', "1.0", "end")

# 메인 창 만들기
root = tk.Tk()
root.title("팀 룰렛 프로그램")
root.configure(bg=background_color)

# 이름 입력 영역
frame = tk.Frame(root, bg=background_color)
frame.pack(pady=10)

team1_label = tk.Label(frame, text="1팀", fg=text_color, bg=background_color, font=('Arial', 14, 'bold'))
team1_label.grid(row=0, column=0, pady=5)

team2_label = tk.Label(frame, text="2팀", fg=text_color, bg=background_color, font=('Arial', 14, 'bold'))
team2_label.grid(row=0, column=2, pady=5)

# 2글자 입력 제한 등록
vcmd = (root.register(limit_input_length), '%P')

for i in range(5):
    entry1 = tk.Entry(frame, bg=entry_bg_color, fg=entry_fg_color, insertbackground='white',
                      validate="key", validatecommand=vcmd)
    entry1.grid(row=i+1, column=0, padx=10, pady=5)
    team1_entries.append(entry1)

    if i == 2:
        vs_label = tk.Label(frame, text="VS", fg=text_color, bg=background_color, font=('Arial', 12, 'bold'))
        vs_label.grid(row=i+1, column=1)
    else:
        empty_label = tk.Label(frame, text="", bg=background_color)
        empty_label.grid(row=i+1, column=1)

    entry2 = tk.Entry(frame, bg=entry_bg_color, fg=entry_fg_color, insertbackground='white',
                      validate="key", validatecommand=vcmd)
    entry2.grid(row=i+1, column=2, padx=10, pady=5)
    team2_entries.append(entry2)

# 룰렛 시작 버튼
start_button = tk.Button(root, text="룰렛 돌리기", command=start_roulette,
                         bg="#FF4C68", fg='white', font=('Arial', 12, 'bold'))
start_button.pack(pady=10)

# 결과 출력 창
result_text = tk.Text(root, width=50, height=20,
                      bg=background_color,
                      fg=text_color,
                      insertbackground='white',
                      font=('Courier New', 12, 'bold'),
                      wrap="none",
                      padx=10, pady=10)
result_text.pack(pady=10)
result_text.tag_configure('center', justify='center')

# 결과 복사 함수
def copy_result():
    result = result_text.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(result)
    root.update()
    messagebox.showinfo("복사 완료", "결과가 클립보드에 복사되었습니다!")

# 결과 복사 버튼
copy_button = tk.Button(root, text="결과 복사", command=copy_result,
                        bg="#FF4C68", fg='white', font=('Arial', 12, 'bold'))
copy_button.pack(pady=5)

# 창 실행
root.mainloop()
