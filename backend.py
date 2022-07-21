import os

os.system('pip install -r requirements.txt')
from variable import *
from unicode import join_jamos
from jamo import h2j, j2hcj
import clipboard

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
        if s[i] == 'h' and i < len(s)-1:
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
        elif s[i] == 'n' and i < len(s)-1:
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
        elif s[i] == 'm' and i < len(s)-1:
            if s[i+1] == 'l':
                kor_str += kor_index[eng2krindex['ml']]
                flag = True
            else:
                kor_str += kor_index[eng2krindex['m']]
        # 여기부터 쌍자음 받침 처리
        elif s[i] == 'r':
            if i < len(s)-2:
                if s[i+1] == 't' and s[i+2] in consonant:
                    kor_str += kor_index[eng2krindex['rt']]
                    flag = True
                else:
                    kor_str += kor_index[eng2krindex[s[i]]]
            elif i == len(s)-2:
                if s[i+1] == 't':
                    kor_str += kor_index[eng2krindex['rt']]
                    flag = True
            else:
                kor_str += kor_index[eng2krindex[s[i]]]
        elif s[i] == 's':
            if i < len(s)-2:
                if s[i+1] == 'w' and s[i+2] in consonant:
                    kor_str += kor_index[eng2krindex['sw']]
                    flag = True
                elif s[i+1] == 'g' and s[i+2] in consonant:
                    kor_str += kor_index[eng2krindex['sg']]
                    flag = True
                else:
                    kor_str += kor_index[eng2krindex[s[i]]]
            elif i == len(s)-2:
                if s[i+1] == 'w':
                    kor_str += kor_index[eng2krindex['sw']]
                    flag = True
                elif s[i+1] == 'g':
                    kor_str += kor_index[eng2krindex['sg']]
                    flag = True
                else:
                    kor_str += kor_index[eng2krindex[s[i]]]
            else:
                kor_str += kor_index[eng2krindex[s[i]]]
        elif s[i] == 'f':
            if i < len(s)-2:
                if s[i+1] == 'r' and s[i+2] in consonant:
                    kor_str += kor_index[eng2krindex['fr']]
                    flag = True
                elif s[i+1] == 'a' and s[i+2] in consonant:
                    kor_str += kor_index[eng2krindex['fa']]
                    flag = True
                elif s[i+1] == 'q' and s[i+2] in consonant:
                    kor_str += kor_index[eng2krindex['fq']]
                    flag = True
                elif s[i+1] == 't' and s[i+2] in consonant:
                    kor_str += kor_index[eng2krindex['ft']]
                    flag = True
                elif s[i+1] == 'x' and s[i+2] in consonant:
                    kor_str += kor_index[eng2krindex['fx']]
                    flag = True
                elif s[i+1] == 'v' and s[i+2] in consonant:
                    kor_str += kor_index[eng2krindex['fv']]
                    flag = True
                elif s[i+1] == 'g' and s[i+2] in consonant:
                    kor_str += kor_index[eng2krindex['fg']]
                    flag = True
                else:
                    kor_str += kor_index[eng2krindex[s[i]]]
            elif i == len(s)-2:
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
                    kor_str += kor_index[eng2krindex[s[i]]]
            else:
                kor_str += kor_index[eng2krindex[s[i]]]
        elif s[i] == 'q':
            if i < len(s)-2:
                if s[i+1] == 't' and s[i+2] in consonant:
                    kor_str += kor_index[eng2krindex['qt']]
                    flag = True
                else:
                    kor_str += kor_index[eng2krindex[s[i]]]
            elif i == len(s)-2:
                if s[i+1] == 't':
                    kor_str += kor_index[eng2krindex['qt']]
                    flag = True
                else:
                    kor_str += kor_index[eng2krindex[s[i]]]
            else:
                kor_str += kor_index[eng2krindex[s[i]]]
        else:
            kor_str += kor_index[eng2krindex[s[i]]]
    
    return join_jamos(kor_str)

def copy_to_clipboard(s):
    clipboard.copy(s)
