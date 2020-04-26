import pandas as pd

def knock17():
    """
    17. １列目の文字列の異なり
    1列目の文字列の種類（異なる文字列の集合）を求めよ．
    確認にはcut, sort, uniqコマンドを用いよ．
    """
    df = pd.read_csv('../data/popular-names.txt', sep='\t', header=None)
    print(df.iloc[:, 0].nunique())

def knock18():
    """
    18. 各行を3コラム目の数値の降順にソート
    各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
    確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
    """
    df = pd.read_csv('../data/popular-names.txt', sep='\t', header=None)
    print(df.sort_values(2, ascending=False))

def knock19():
    """
    19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
    各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
    確認にはcut, uniq, sortコマンドを用いよ．
    """
    df = pd.read_csv('../data/popular-names.txt', sep='\t', header=None)
    print(df.iloc[:, 0].value_counts())


def main():
    print('17:')
    knock17()
    print('18:')
    knock18()
    print('19:')
    knock19()

if __name__ == "__main__":
    main()
