from collections import defaultdict

def knock00():
    """
    00. 文字列の逆順Permalink
    文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
    """
    str = "stressed"
    return str[::-1]

def knock01():
    """
    01. 「パタトクカシーー」Permalink
    「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
    """
    str1 = "パタトクカシーー"
    return str1[::2]

def knock02():
    """
    02. 「パトカー」＋「タクシー」＝「パタトクカシーー」Permalink
    「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
    """
    str1 = "パトカー"
    str2 = "タクシー"
    res = ""
    for char1, char2 in zip(str1, str2):
        res += char1 + char2
    return res

def knock03():
    """
    03. 円周率Permalink
    “Now I need a drink, alcoholic of course,
    after the heavy lectures involving quantum mechanics.”
    という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
    """
    txt = "Now I need a drink, alcoholic of course, \
           after the heavy lectures involving quantum mechanics."
    words = txt.translate(str.maketrans('', '', ',.'))
    ans = [len(w) for w in words.split()]
    return ans

def knock04():
    """
    04. 元素記号Permalink
    “Hi He Lied Because Boron Could Not Oxidize Fluorine.
    New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
    という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
    それ以外の単語は先頭に2文字を取り出し，
    取り出した文字列から単語の位置（先頭から何番目の単語か）への
    連想配列（辞書型もしくはマップ型）を作成せよ．
    """
    atomic_symbols = defaultdict(lambda: 0)
    txt = "Hi He Lied Because Boron Could Not Oxidize Fluorine. \
           New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    words = txt.translate(str.maketrans('', '', ',.'))
    i = 0
    for word in words.split():
        if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
            atomic_symbols[word[:1]] = i
        else:
            atomic_symbols[word[:2]] = i
        i += 1
    return atomic_symbols

def main():
    print('00: \n', knock00())
    print('01: \n', knock01())
    print('02: \n', knock02())
    print('03: \n', knock03())
    print('04: \n', knock04())


if __name__ == "__main__":
    main()
