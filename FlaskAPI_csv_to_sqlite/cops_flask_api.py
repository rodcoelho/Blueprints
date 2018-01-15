from flask import Flask, jsonify
from sqlalchemy import create_engine
import pandas as pd
import sqlite3

app = Flask(__name__)
df = pd.read_csv('cpuo.csv')
# Year,Ranking,Precinct,Complaints,Number_of_officers
disk_engine = create_engine('sqlite:///data_cops.db')
df.to_sql('table1', disk_engine, if_exists='append')

@app.route('/most_complaints_per_officer/<int:year>/')
def get_ratio(year):
    connection = sqlite3.connect('data_cops.db')
    cursor = connection.cursor()
    cursor.execute("""
                    SELECT Precinct, Complaints, Number_of_officers
                    FROM table1 
                    WHERE year = "{}" 
                    ORDER BY Complaints/Number_of_officers
                    ASC LIMIT 1;
                    """.format(year))
    result = cursor.fetchall()
    precinct = result[0][0]
    ratio = result[0][1] / result[0][2]
    print(result)
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(
        precinct = precinct,
        ratio = ratio
    )

@app.route('/')
def home():
    return """<p>Try the following urls:</p>
    <p>/most_complaints_per_officer/<int:year>/</p>
    <p>/least_complaints/<int:year>/</p>
    <p>/most_complaints/<int:year>/</p>
    <p>/most_cops/<int:year>/</p>
    """

@app.route('/least_complaints/<int:year>/')
def get_least_complaints_by_year(year):
    connection = sqlite3.connect('data_cops.db')
    cursor = connection.cursor()
    cursor.execute("""
                    SELECT Precinct, Complaints 
                    FROM table1 
                    WHERE year = "{}" 
                    ORDER BY Complaints 
                    ASC LIMIT 1;
                    """.format(year))
    result = cursor.fetchall()
    precinct = result[0][0]
    complaints = result[0][1]
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(
        precinct = precinct,
        complaints = complaints
    )

@app.route('/most_complaints/<int:year>/')
def get_most_complaints_by_year(year):
    connection = sqlite3.connect('data_cops.db')
    cursor = connection.cursor()
    cursor.execute("""
                    SELECT Precinct, Complaints 
                    FROM table1 
                    WHERE year = "{}" 
                    ORDER BY Complaints 
                    DESC LIMIT 1;
                    """.format(year))
    result = cursor.fetchall()
    precinct = result[0][0]
    complaints = result[0][1]
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(
        precinct = precinct,
        complaints = complaints
    )

@app.route('/most_cops/<int:year>/')
def get_most_cops_by_year(year):
    connection = sqlite3.connect('data_cops.db')
    cursor = connection.cursor()
    cursor.execute("""
                    SELECT Precinct, Number_of_officers 
                    FROM table1 
                    WHERE year = "{}" 
                    ORDER BY Number_of_officers 
                    DESC LIMIT 1;
                    """.format(year))
    result = cursor.fetchall()
    precinct = result[0][0]
    Number_of_officers = result[0][1]
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(
        precinct = precinct,
        Number_of_officers = Number_of_officers
    )

if __name__ == "__main__":
    app.run(debug=True)