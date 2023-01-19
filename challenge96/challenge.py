#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL= "https://opentdb.com/api.php?amount=3&category=10&difficulty=easy&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    print(data["results"])
    print('\n')
    answers = []
    
    for qna in data["results"]:

        print(qna["question"])
        answers.append(qna["correct_answer"])
        print("\n")
        for i in qna["incorrect_answers"]:
            answers.append(i)
        
        for ans in answers:
            print(ans)


        print("\n")


        answers = []
if __name__ == "__main__":
    main()

