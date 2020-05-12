import psycopg2
import logging
import connect as con
# cur = connect.cursor;

def save_docs(doc,label):
        conn = con.connet_to_host(con.host, con.user, con.dbname, con.password)
        cur = conn.cursor()
        cur.execute(f"INSERT INTO score (doc,label) VALUES ({doc},{label}) ")
        conn.commit()
        cur.close()
        conn.close()


def get_docs():
        con.print_tables("""SELECT * FROM all_docs""")

def get_doc_by_label(label):
         con.print_tables(f"""SELECT docs, label FROM all_docs WHERE label= '{label}';""")

def save_tfidf(list_of_dictionaries):
    conn = con.connet_to_host(con.host, con.user, con.dbname, con.password)
    cur = conn.cursor()
    for dictionaries in list_of_dictionaries:
        term = list(dictionaries.keys())[0]
        cur.execute(f"""SELECT term FROM score WHERE term = '{term}';""")
        if cur.rowcount == 0:
            cur.execute(f"INSERT INTO score (term,{dictionaries[term][0]}) VALUES ({term},{dictionaries[term][1]}) ")
        else:
            cur.execute(f"""SELECT verison_{dictionaries[term][0]}, {dictionaries[term][0]} FROM score WHERE term = '{term}';""")
            current_verison = list(cur.fetchall()[0])
            if current_verison[0] is None:
                cur.execute( f"UPDATE score SET ({dictionaries[term][0]}, verison_{dictionaries[term][0]}) = ({dictionaries[term][1]},1) WHERE term = '{term}'")
            else:
                updade_verison = current_verison[0] + 1
                print((current_verison[0] * current_verison[1]) + dictionaries[term][1])
                current_avg =  ((current_verison[0] * current_verison[1]) + dictionaries[term][1]) / updade_verison
                print(current_avg)
                cur.execute( f"UPDATE score SET ({dictionaries[term][0]}, verison_{dictionaries[term][0]}) = ({current_avg},{updade_verison}) WHERE term = '{term}'")

    conn.commit()
    cur.close()
    conn.close()

def get_tfidf(**label):
    conn = con.connet_to_host(con.host, con.user, con.dbname, con.password)
    cur = conn.cursor()
    if not label:
        con.print_tables("""SELECT * FROM score""")
    else:
        t = list(label.keys())
        for i in t:
            if i == "term":
                try:
                    cur.execute(f"""SELECT * FROM score WHERE term = '{label[i]}';""")
                except:
                    logging.error("select failed")
                if cur.rowcount > 0 :
                    if len(label)==1:
                        con.print_tables(f"""SELECT * FROM score WHERE term = '{label[i]}';""")
                else:
                    print("The term does not exist in the table")
            elif i == "label":
                try:
                    con.print_tables(f"""SELECT term, {label[i]} FROM score;""""")
                except psycopg2.errors.UndefinedColumn as e:
                    print(e)
            else:
                print(f"{i} is not key Only label or term must be defined")
    conn.commit()
    cur.close()
    conn.close()

def get_count_doc(label):
    conn = con.connet_to_host(con.host, con.user, con.dbname, con.password)
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM all_docs WHERE label = '{label}';""")
    return cur.rowcount
    conn.commit()
    cur.close()
    conn.close()

get_tfidf()


