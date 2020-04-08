import random

from collections import defaultdict

def knock00():
    """
    00. 文字列の逆順
    文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
    """
    str1 = "stressed"
    return str1[::-1]

def knock01():
    """
    01. 「パタトクカシーー」
    「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
    """
    str1 = "パタトクカシーー"
    return str1[::2]

def knock02():
    """
    02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
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
    03. 円周率
    "Now I need a drink, alcoholic of course,
    after the heavy lectures involving quantum mechanics."
    という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
    """
    txt = "Now I need a drink, alcoholic of course, \
           after the heavy lectures involving quantum mechanics."
    words = txt.translate(str.maketrans('', '', ',.'))
    ans = [len(w) for w in words.split()]
    return ans

def knock04():
    """
    04. 元素記号
    "Hi He Lied Because Boron Could Not Oxidize Fluorine.
    New Nations Might Also Sign Peace Security Clause. Arthur King Can."
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

def ngram(text, n):
    if len(text) >= n:
        ngram_list = [text[i:i+n] for i in range(len(text) - n + 1)]
    return ngram_list


def knock05():
    """
    05. n-gram
    与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
    この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
    """
    text = "I am an NLPer"
    word_ngram = ngram(text, 2)
    char_ngram = ngram(text.split(' '), 2)
    return word_ngram, char_ngram

def knock06():
    """
    06. 集合
    "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
    それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
    さらに，'seと'いうbi-gramがXおよびYに含まれるかどうかを調べよ．
    """
    X_text = 'paraparaparadise'
    Y_text = 'paragraph'
    X = ngram(X_text, 2)
    Y = ngram(Y_text, 2)

    print('06: \n')
    print('union: ', set(X) | set(Y))
    print('intersection: ', set(X) & set(Y))
    print('difference: ', set(X) - set(Y))
    if 'se' in set(X) & set(Y):
        print('se is in X&Y')
    else:
        print('se is NOT in X&Y')

def temperature(x, y, z):
    return f'{x}時の{y}は{z}'

def knock07():
    """
    07. テンプレートによる文生成
    引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
    さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
    """
    x = 12
    y = '気温'
    z = 22.4
    return temperature(x, y, z)

def cipher(words):
    text = [chr(219 - ord(word)) if word.islower() else word for word in words]
    return text

def knock08():
    """
    08. 暗号文
    与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

    英小文字ならば(219 - 文字コード)の文字に置換
    その他の文字はそのまま出力
    この関数を用い，英語のメッセージを暗号化・復号化せよ．
    """
    words = 'Encrypt English sentence and then decrypt it.'
    print('08: \n')
    encrypt_txt = cipher(words)
    print('encrypt_txt:', encrypt_txt)
    decrypt_txt = cipher(encrypt_txt)
    print('decrypt_txt:', decrypt_txt)

def shuffle_word(word):
    if len(word) <= 4:
        return word
    start = word[0]
    end = word[-1]
    others = random.sample(list(word[1:-1]), len(word[1:-1]))
    return ''.join([start] + others + [end])

def knock09():
    """
    09. Typoglycemia
    スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
    それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
    ただし，長さが４以下の単語は並び替えないこととする．
    適当な英語の文（例えば"I couldn’t believe that I could actually understand
    what I was reading : the phenomenal power of the human mind .""）を与え，
    その実行結果を確認せよ．
    """
    text = 'I couldn’t believe that I could actually understand \
            what I was reading : the phenomenal power of the human mind.'
    print('09: \n')
    res = [shuffle_word(word) for word in text.split()]
    print(res)

def main():
    print('00: \n', knock00())
    print('01: \n', knock01())
    print('02: \n', knock02())
    print('03: \n', knock03())
    print('04: \n', knock04())
    word_ngram, char_ngram = knock05()
    print('05 word ngram: \n', word_ngram)
    print('05 char ngram: \n', char_ngram)
    knock06()
    print('07: \n', knock07())
    knock08()
    knock09()


if __name__ == "__main__":
    main()
