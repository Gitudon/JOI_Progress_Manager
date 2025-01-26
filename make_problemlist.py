import requests
from bs4 import BeautifulSoup
import problems as pb
import time

def url_to_problem_name(url):
    #urlから問題名を取得する
    if url=="":
        return ""
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    #問題名のタイトルが4から始まる場合はエラーなのでその旨を表示
    for tag in soup.select("title"):
        while True:
            if tag.text[0] != "4":
                print(tag.text)
                time.sleep(1)
                return tag.text

def main():
    problem_names={}
    problem_categories = {
        "A_calc": pb.A_calc,
        # "A_if": pb.A_if,
        # "B_string": pb.B_string,
        # "B_for": pb.B_for,
        # "C_list": pb.C_list,
        # "C_kakomon": pb.C_kakomon,
        # "S1_while": pb.S1_while,
        # "S1_multi": pb.S1_multi,
        # "S1_multi_list": pb.S1_multi_list,
        # "S2_Built_in_functions": pb.S2_Built_in_functions,
        # "S2_Built_in_functions_Advance": pb.S2_Built_in_functions_Advance,
        # "S2_sort": pb.S2_sort,
        # "S2_sort_Advance": pb.S2_sort_Advance,
        # "S3_function": pb.S3_function,
        # "S3_recursive": pb.S3_recursive,
        # "S3_recursive_Advance": pb.S3_recursive_Advance
    }
    for category, urls in problem_categories.items():
        for url in urls:
            problem_names[url] = url_to_problem_name(url)
    print(problem_names)

if __name__=="__main__":
    main()
