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
                # 확정된 경우
                if current_tier == 6:
                    extra_str = show_extra.center(7)
                else:
                    extra_str = show_extra.center(8)
            else:
                # 확정되지 않은 경우: 무조건 8칸
                extra_str = show_extra.center(8)

            temp_result[line_indices[idx]] = f"|{display_queue[idx][1][0].center(6)}|{show_line.center(6)}|{(str(show_tier)+'티어').center(6)}|{extra_str}|"

        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "\n".join(temp_result))
        result_text.tag_add('center', '1.0', 'end')