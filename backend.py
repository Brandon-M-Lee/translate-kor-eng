import os

os.system('pip install -r requirements.txt')
from variable import *
from unicode import join_jamos
from jamo import h2j, j2hcj

def kor_to_eng(s):
    """
    Convert Korean to English
    """
    jamo_str = j2hcj(h2j(s))
    eng_str = ""

    for c in jamo_str:
        if c == ' ':
            eng_str += ' '
        for i in range(1, 52):
            if kor_index[i] == c:
                eng_str += krindex2eng[i]
                break
    
    return eng_str

def eng_to_kor(s):
    """
    Convert English to Korean
    """
    kor_str = ""
    flag = False

    for i in range(len(s)):
        if flag:
            flag = False
            continue
        if s[i] == ' ':
            kor_str += ' '
        elif s[i] == 'h':
            if s[i+1] == 'k':
                kor_str += kor_index[eng2krindex['hk']]
                flag = True
            elif s[i+1] == 'o':
                kor_str += kor_index[eng2krindex['ho']]
                flag = True
            elif s[i+1] == 'l':
                kor_str += kor_index[eng2krindex['hl']]
                flag = True
            else:
                kor_str += kor_index[eng2krindex['h']]
        elif s[i] == 'n':
            if s[i+1] == 'j':
                kor_str += kor_index[eng2krindex['nj']]
                flag = True
            elif s[i+1] == 'p':
                kor_str += kor_index[eng2krindex['np']]
                flag = True
            elif s[i+1] == 'l':
                kor_str += kor_index[eng2krindex['nl']]
                flag = True
            else:
                kor_str += kor_index[eng2krindex['n']]
        elif s[i] == 'm':
            if s[i+1] == 'l':
                kor_str += kor_index[eng2krindex['ml']]
                flag = True
            else:
                kor_str += kor_index[eng2krindex['m']]
        # 여기부터 쌍자음 받침 처리
        elif s[i] == 'r' and s[i+2] in consonant:
            if s[i+1] == 't':
                kor_str += kor_index[eng2krindex['rt']]
                flag = True
            else:
                kor_str += kor_index[eng2krindex['r']]
        elif s[i] == 's' and s[i+2] in consonant:
            if s[i+1] == 'w':
                kor_str += kor_index[eng2krindex['sw']]
                flag = True
            elif s[i+1] == 'g':
                kor_str += kor_index[eng2krindex['sg']]
                flag = True
            else:
                kor_str += kor_index[eng2krindex['s']]
        elif s[i] == 'f' and s[i+2] in consonant:
            if s[i+1] == 'r':
                kor_str += kor_index[eng2krindex['fr']]
                flag = True
            elif s[i+1] == 'a':
                kor_str += kor_index[eng2krindex['fa']]
                flag = True
            elif s[i+1] == 'q':
                kor_str += kor_index[eng2krindex['fq']]
                flag = True
            elif s[i+1] == 't':
                kor_str += kor_index[eng2krindex['ft']]
                flag = True
            elif s[i+1] == 'x':
                kor_str += kor_index[eng2krindex['fx']]
                flag = True
            elif s[i+1] == 'v':
                kor_str += kor_index[eng2krindex['fv']]
                flag = True
            elif s[i+1] == 'g':
                kor_str += kor_index[eng2krindex['fg']]
                flag = True
            else:
                kor_str += kor_index[eng2krindex['f']]
        elif s[i] == 'q' and s[i+2] in consonant:
            if s[i+1] == 't':
                kor_str += kor_index[eng2krindex['qt']]
                flag = True
            else:
                kor_str += kor_index[eng2krindex['q']]
        else:
            kor_str += kor_index[eng2krindex[s[i]]]
    
    return join_jamos(kor_str)

