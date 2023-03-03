with open('simput') as f:
    inp = f.read().strip().split('\n')
hashtag = '#'
dot = '.'
sprite_list = [hashtag if i < 3 else dot for i in range(40)]
print(sprite_list)
sprite_pos = 1
solution = []
end_of_row = [40, 80, 120, 160, 200, 240]
cycle = 1
crt_row = []
crt_pixel = 0
for row in inp:
    try:
        _, n = row.split()
    except ValueError:      # noop
        n = 0
    finally:
        if cycle == any(end_of_row):
            solution.append(crt_row)
            crt_row.clear()
            crt_pixel = 0
        if n:
            sprite_pos += int(n)
            for _ in range(2):
                if sprite_list[crt_pixel] == hashtag:
                    crt_row.append(hashtag)
                else:
                    crt_row.append(dot)
                crt_pixel += 1
            sprite_list = [hashtag if i in [sprite_pos - 1, sprite_pos, sprite_pos + 1] else dot for i in range(40)]
        else:            # CRT draws pixel at next position
            if sprite_list[crt_pixel] == hashtag:
                crt_row.append(hashtag)
            else:
                crt_row.append(dot)
            crt_pixel += 1

for row in solution:
    print(row)