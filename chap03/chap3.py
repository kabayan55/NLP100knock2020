"""
Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．

1行に1記事の情報がJSON形式で格納される
各行には記事名が”title”キーに，記事本文が”text”キーの辞書オブジェクトに格納され，
そのオブジェクトがJSON形式で書き出される
ファイル全体はgzipで圧縮される
以下の処理を行うプログラムを作成せよ．
"""
import re
import pandas as pd

def knock20():
    """
    20. JSONデータの読み込み
    Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
    問題21-29では，ここで抽出した記事本文に対して実行せよ．
    """
    df = pd.read_json('../data/jawiki-country.json.gz', lines=True)
    uk_text = df.query('title=="イギリス"')['text'].values[0]
    return uk_text

def knock21(uk_text):
    """
    21. カテゴリ名を含む行を抽出
    記事中でカテゴリ名を宣言している行を抽出せよ．
    """
    list_uk_text = uk_text.split('\n')
    rows_cat_name = list(filter(lambda x: 'Category:' in x, list_uk_text))
    return rows_cat_name


def knock22(rows_cat_name):
    """
    22. カテゴリ名の抽出
    記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
    """
    category = re.compile('\[\[Category:.*')
    cat_name = [cat.replace('[[Category:', '').replace('|*', '').replace(']]', '')
                for cat in rows_cat_name if category.search(cat)]
    return cat_name

def knock23(uk_text):
    """
    23. セクション構造
    記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．
    """
    for section in re.findall(r'(=+)([^=]+)\1\n', uk_text):
        print(f'{section[1].strip()}\t{len(section[0]) - 1}')


def knock24(uk_text):
    """
    24. ファイル参照の抽出
    記事から参照されているメディアファイルをすべて抜き出せ．
    """
    for file in re.findall(r'\[\[(ファイル|File):([^]|]+?)(\|.*?)+\]\]', uk_text):
        print(file[1])

def knock25(uk_text):
    """
    25. テンプレートの抽出
    記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
    辞書オブジェクトとして格納せよ．
    """

def knock26(uk_text):
    """
    26. 強調マークアップの除去
    25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
    （弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
    （参考: マークアップ早見表）．
    """

def knock27(uk_text):
    """
    27. 内部リンクの除去
    26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，
    テキストに変換せよ（参考: マークアップ早見表）．
    """

def knock28(uk_text):
    """
    28. MediaWikiマークアップの除去
    27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，
    国の基本情報を整形せよ．
    """

def knock29(uk_text):
    """
    29. 国旗画像のURLを取得する
    テンプレートの内容を利用し，国旗画像のURLを取得せよ．
    （ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
    """

def main():
    print('20:')
    uk_text = knock20()
    print(uk_text)
    print('21:')
    rows_cat_name = knock21(uk_text)
    print(rows_cat_name)
    print('22:')
    cat_name = knock22(rows_cat_name)
    print(cat_name)
    print('23:')
    knock23(uk_text)
    print('24:')
    knock24(uk_text)

if __name__ == "__main__":
    main()
