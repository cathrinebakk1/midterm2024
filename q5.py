def find_pattern(text):
    pattern_start = 'C'
    pattern_end = 'jeb'
    count = 0
    i = 0

    while i < len(text):
        # Find the start 'C'
        start_index = text.find(pattern_start, i)

        if start_index != -1:
            # Look for 'jeb' after 'C'
            end_index = text.find(pattern_end, start_index)

            if end_index != -1:
                # Check if 'C' directly precedes 'jeb'
                if text[start_index:end_index].startswith(pattern_start) and text[start_index:end_index + len(
                        pattern_end)].endswith(pattern_end):
                    count += 1
                    i = end_index + len(pattern_end) - 1
            i += 1
        else:
            # No more 'C's found, break
            break

    return count
