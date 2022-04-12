def solution(new_id):
    nid = new_id
    # 1
    for ch in new_id:
        if ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            nid = nid.replace(ch, ch.lower())
    
    new_id = nid
    # 2
    for ch in new_id:
        if ch not in 'abcdefghijklmnopqrstuvwxyz0123456789-_.':
            nid = nid.replace(ch, '')
    
    new_id = nid
    # 3
    while(True):
        if '..' in new_id:
            new_id = new_id.replace('..','.')
        else:
            break
    # 3, 5, 20, 21 실패
    # tmp = ''
    # for ch in new_id:
    #     if ch == '.':
    #         tmp += ch
    #     elif tmp != '':
    #         nid = nid.replace(tmp,'.')
    #         tmp = ''
    # if tmp != '':
    #     nid = nid.replace(tmp,'.')
    
    # new_id = nid
    # 4
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
        
    #5
    if not new_id:
        new_id = 'a'
        
    #6
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    #7
    while(len(new_id) < 3):
        new_id += new_id[-1]
        
    return new_id