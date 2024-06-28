# привести путь к каноническому
# /home/../../tmp////usr1/../usr2/.//files//// -> /tmp/usr2/files

def do_canon(init_path: str)->str:
    out = ['/']
    for word in init_path.split('/'):
        if word != '..' and word != '.' and word != '':
            out.append(word)
        elif word == '..' and len(out) > 1:
            out.pop()
    return '/'.join(out)[1:]

if __name__=='__main__':
    assert do_canon('/home/../../tmp////usr1/../usr2/.////files////') == '/tmp/usr2/files'
    assert do_canon('/home/../new////usr1/../usr2/.////files////') == '/new/usr2/files'
    assert do_canon('/new////usr1/../usr2/.////files////') == '/new/usr2/files'
    assert do_canon('/new////usr1/../usr2/.////files////') == '/new/usr2/files'
    assert do_canon('/new////usr1/././///files////') == '/new/usr1/files'
 