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
text_color = '#FF6B81'
entry_bg_color = '#333333'
entry_fg_color = 'white'

# 2글자 입력 제한 함수
def limit_input_length(P):
    return len(P) <= 2

# 역할 랜덤 배정 함수
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

def start_roulette_with_effect():
    global spin_timer
    spin_timer = None

    root.focus()  # 포커스 해제

    team1 = [entry.get() for entry in team1_entries]
    team2 = [entry.get() for entry in team2_entries]

    if '' in team1 or '' in team2:
        messagebox.showerror("오류", "모든 이름을 입력해주세요!")
        return

    result_text.delete('1.0', tk.END)

    team1_result = assign_roles(team1)
    team2_result = assign_roles(team2)
    total_result = [("1팀", team1_result), ("2팀", team2_result)]

    display_queue = []
    for team_name, team_result in total_result:
        for member in team_result:
            display_queue.append((team_name, member))

    template_lines = []
    template_lines.append("\n\u2728 1팀 \u2728")
    template_lines.append("\u2501" * 34)
    template_lines.append(f"| {'팀원'.center(4)} | {'라인'.center(4)} | {'티어'.center(4)} | {'6티어'.center(5)} |")
    template_lines.append("\u2501" * 34)
    for i in range(5):
        template_lines.append(f"|{team1[i].center(6)}|{' '.center(7)}|{' '.center(7)}|{' '.center(8)}|")
    template_lines.append("\n\U0001F525 2팀 \U0001F525")
    template_lines.append("\u2501" * 34)
    template_lines.append(f"| {'팀원'.center(4)} | {'라인'.center(4)} | {'티어'.center(4)} | {'6티어'.center(5)} |")
    template_lines.append("\u2501" * 34)
    for i in range(5):
        template_lines.append(f"|{team2[i].center(6)}|{' '.center(7)}|{' '.center(7)}|{' '.center(8)}|")

    result_text.insert(tk.END, "\n".join(template_lines))
    result_text.tag_add('center', '1.0', 'end')

    lines_content = result_text.get("1.0", tk.END).splitlines()

    line_indices = []
    for idx, line in enumerate(lines_content):
        if line.startswith("|") and len(line) > 10:
            if not any(word in line for word in ['팀원', '라인']):
                line_indices.append(idx)

    temp_display = {}
    current_index = 0

    def spin_line_tier_extra():
        if current_index >= len(display_queue):
            return

        temp_result = lines_content.copy()
        for idx in range(current_index + 1):
            name, true_line, true_tier, true_extra = display_queue[idx][1]

            random_line = random.choice(lines)
            random_tier = random.randint(1, 6)
            random_extra = random.choice(lines)

            show_line = temp_display.get(idx, {}).get('line', random_line)
            show_tier = temp_display.get(idx, {}).get('tier', random_tier)
            show_extra = temp_display.get(idx, {}).get('extra', random_extra)

            current_tier = temp_display.get(idx, {}).get('tier')
            if current_tier is not None:
                if current_tier == 6:
                    extra_str = show_extra.center(7)
                else:
                    extra_str = ' '.center(8)
            else:
                extra_str = show_extra.center(7)

            temp_result[line_indices[idx]] = f"|{display_queue[idx][1][0].center(6)}|{show_line.center(6)}|{(str(show_tier)+'티어').center(6)}|{extra_str}|"

        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "\n".join(temp_result))
        result_text.tag_add('center', '1.0', 'end')

    def reveal_line():
        global spin_timer
        temp_display[current_index] = {'line': display_queue[current_index][1][1]}
        spin_timer = root.after(1000, reveal_tier)

    def reveal_tier():
        global spin_timer
        temp_display[current_index]['tier'] = display_queue[current_index][1][2]

        if display_queue[current_index][1][2] == 6:
            spin_timer = root.after(1000, reveal_extra)
        else:
            temp_display[current_index]['extra'] = ''
            spin_timer = root.after(350, next_person)

    def reveal_extra():
        global spin_timer
        temp_display[current_index]['extra'] = display_queue[current_index][1][3]
        spin_timer = root.after(350, next_person)

    def next_person():
        global spin_timer
        nonlocal current_index
        current_index += 1
        if current_index >= len(display_queue):
            if spin_timer:
                root.after_cancel(spin_timer)
            return
        root.after(500, process_person)

    def process_person():
        global spin_timer
        spin_timer = root.after(50, spin_loop)
        root.after(1000, reveal_line)

    def spin_loop():
        spin_line_tier_extra()
        global spin_timer
        spin_timer = root.after(50, spin_loop)

    process_person()

def reset_all():
    global spin_timer
    if spin_timer:
        root.after_cancel(spin_timer)
        spin_timer = None

    for entry in team1_entries + team2_entries:
        entry.delete(0, tk.END)

    result_text.delete('1.0', tk.END)
    root.focus()

# Tkinter 기본 창 세팅
root = tk.Tk()
root.title("이벤트 내전 룰렛 프로그램 v1.1.0 made by 조아블")
root.configure(bg=background_color)

frame = tk.Frame(root, bg=background_color)
frame.pack(pady=10)

team1_label = tk.Label(frame, text="1팀", fg=text_color, bg=background_color, font=('Arial', 14, 'bold'))
team1_label.grid(row=0, column=0, pady=5)

team2_label = tk.Label(frame, text="2팀", fg=text_color, bg=background_color, font=('Arial', 14, 'bold'))
team2_label.grid(row=0, column=2, pady=5)

vcmd = (root.register(limit_input_length), '%P')

for i in range(5):
    entry1 = tk.Entry(frame, bg=entry_bg_color, fg=entry_fg_color, insertbackground='white', validate="key", validatecommand=vcmd)
    entry1.grid(row=i+1, column=0, padx=10, pady=5)
    team1_entries.append(entry1)

    if i == 2:
        vs_label = tk.Label(frame, text="VS", fg=text_color, bg=background_color, font=('Arial', 12, 'bold'))
        vs_label.grid(row=i+1, column=1)
    else:
        empty_label = tk.Label(frame, text="", bg=background_color)
        empty_label.grid(row=i+1, column=1)

    entry2 = tk.Entry(frame, bg=entry_bg_color, fg=entry_fg_color, insertbackground='white', validate="key", validatecommand=vcmd)
    entry2.grid(row=i+1, column=2, padx=10, pady=5)
    team2_entries.append(entry2)

# 룰렛 돌리기 + 초기화 버튼 같이 묶기
button_frame = tk.Frame(root, bg=background_color)
button_frame.pack(pady=5)

start_button = tk.Button(button_frame, text="룰렛 돌리기", command=start_roulette_with_effect,
                         bg="#E0435C", fg='white', font=('Arial', 12, 'bold'))
start_button.pack(side='left', padx=(0, 15))

reset_button = tk.Button(button_frame, text="초기화", command=reset_all,
                         bg="#E0435C", fg='white', font=('Arial', 12))
reset_button.pack(side='left')

result_text = tk.Text(root, width=50, height=20,
                      bg=background_color,
                      fg=text_color,
                      insertbackground='white',
                      font=('Courier New', 12, 'bold'),
                      wrap="none",
                      padx=10, pady=10)
result_text.pack(pady=10)
result_text.tag_configure('center', justify='center')

def copy_result():
    result = result_text.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(result)
    root.update()
    messagebox.showinfo("복사 완료", "결과가 클립보드에 복사되었습니다!")

copy_button = tk.Button(root, text="결과 복사", command=copy_result,
                        bg="#E0435C", fg='white', font=('Arial', 12, 'bold'))
copy_button.pack(pady=5)

root.mainloop()
