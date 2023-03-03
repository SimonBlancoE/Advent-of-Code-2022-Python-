with open('simput') as f:
    inp = f.read().strip().split('\n')
hashtag = '#'
dot = '.'
sprite_list = [hashtag if i < 3 else dot for i in range(40)]
print(sprite_list)
sprite_pos = 1
cycle = []
for row in inp:
    try:
        _, n = row.split()
        sprite_pos += int(n)
        sprite_list = [hashtag if i in [sprite_pos - 1, sprite_pos, sprite_pos + 1] else dot for i in range(40)]
        print(f"add {n}")
        print(sprite_list)
        for _ in range(2):
            pass
    except ValueError:      # noop
        pass
