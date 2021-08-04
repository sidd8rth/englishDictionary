import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)


def find_meaning(w):
    if w == 'q' or w == 'Q':
        exit()
    cursor = con.cursor()
    queryExpression = cursor.execute("SELECT Expression FROM Dictionary")
    expression = cursor.fetchall()
    exp = []
    for i in expression:
        exp.append(i[0])
    if w in exp:
        cursor = con.cursor()
        query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{w}'")
        results = cursor.fetchall()
        if results:
            for result in results:
                print(result[1])
    elif len(get_close_matches(w, exp, cutoff=0.8)) > 0:
        yn = input(
            f"Did you mean {get_close_matches(w, exp, cutoff=0.8)[0]} instead? Enter Y if yes or N for no : ").upper()
        if yn == 'Y':
            cursor = con.cursor()
            query = cursor.execute(
                f"SELECT * FROM Dictionary WHERE Expression = '{get_close_matches(w, exp, cutoff=0.8)[0]}'")
            res = cursor.fetchall()
            if res:
                for r in res:
                    print(r[1])
        elif yn == 'N':
            print("Sorry, The word you are trying to find meaning of, doesn't exist")
        else:
            print("Sorry, Can't understand your query")
    else:
        print("This word doesn't exist, Please double check you input and try again")


while True:
    w = input("Enter Word you want to search , or to exit enter Q : ")
    find_meaning(w)
