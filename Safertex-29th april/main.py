from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the query with JOIN
@app.route('/query_with_join')
def query_with_join_route():
    results = query_with_join()
    if results:
        return render_template('results.html', results=results)
    else:
        return "No results found"

# Route to handle the query without JOIN
@app.route('/query_without_join')
def query_without_join_route():
    results = query_without_join()
    if results:
        return render_template('results.html', results=results)
    else:
        return "No results found"

def query_with_join():
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    # Create tables
    cur.execute('''CREATE TABLE locations (
                        location_id INTEGER PRIMARY KEY,
                        street_address TEXT,
                        postal_code TEXT,
                        city TEXT,
                        state_province TEXT,
                        country_id TEXT
                    )''')

    cur.execute('''CREATE TABLE countries (
                        country_id TEXT PRIMARY KEY,
                        country_name TEXT,
                        region_id INTEGER
                    )''')

    # Insert values into the countries table
    countries_data = [
        ('AR', 'Argentina', 2),
        ('AU', 'Australia', 3),
        ('BE', 'Belgium', 1),
        ('BR', 'Brazil', 2),
        ('CA', 'Canada', 2),
        ('CH', 'Switzerland', 1),
        ('CN', 'China', 3),
        ('DE', 'Germany', 1)
    ]

    cur.executemany("INSERT INTO countries VALUES (?, ?, ?)", countries_data)

    # Insert values into the locations table
    locations_data = [
        (1000, '1297 Via Cola di Rie', '989', 'Roma', 'IT', 'CA'),
        (1100, '93091 Calle della Te', '10934', 'Venice', 'IT', 'CA'),
        (1200, '2017 Shinjuku-ku', '1689', 'Tokyo', 'Tokyo Prefecture', 'JP'),
        (1300, '9450 Kamiya-cho', '6823', 'Hiroshima', 'Hiroshima', '2P'),
        (1400, '2014 Jabberwocky Rd', '26192', 'Southlake', 'Texas', 'US'),
        (1500, '2011 Interiors Blvd', '99236', 'South San South Brun', 'California', 'US'),
        (1600, '2007 Zagora St', '50090', 'New Jersey', 'New Jersey', 'US'),
        (1700, '2004 Charade Rd', '98199', 'Seattle', 'Washington', 'US'),
        (1800, '147 Spadina Ave', 'MSV 2L7', 'Toronto', 'Ontario', 'CA')
    ]

    cur.executemany("INSERT INTO locations VALUES (?, ?, ?, ?, ?, ?)", locations_data)

    # Commit the transaction
    conn.commit()

    # Query to find the address of Canada using JOIN
    cur.execute('''SELECT l.location_id, l.street_address, l.postal_code, l.city, l.state_province, c.country_name
                    FROM locations l
                    JOIN countries c ON l.country_id = c.country_id
                    WHERE c.country_name = 'Canada' ''')

    print("With Join")
    # Fetch and print results
    results = cur.fetchall()

    # Close cursor and connection
    cur.close()
    conn.close()

    return results

def query_without_join():
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    # Create tables
    cur.execute('''CREATE TABLE locations (
                        location_id INTEGER PRIMARY KEY,
                        street_address TEXT,
                        postal_code TEXT,
                        city TEXT,
                        state_province TEXT,
                        country_id TEXT
                    )''')

    cur.execute('''CREATE TABLE countries (
                        country_id TEXT PRIMARY KEY,
                        country_name TEXT,
                        region_id INTEGER
                    )''')

    # Insert values into the countries table
    countries_data = [
        ('AR', 'Argentina', 2),
        ('AU', 'Australia', 3),
        ('BE', 'Belgium', 1),
        ('BR', 'Brazil', 2),
        ('CA', 'Canada', 2),
        ('CH', 'Switzerland', 1),
        ('CN', 'China', 3),
        ('DE', 'Germany', 1)
    ]

    cur.executemany("INSERT INTO countries VALUES (?, ?, ?)", countries_data)

    # Insert values into the locations table
    locations_data = [
        (1000, '1297 Via Cola di Rie', '989', 'Roma', 'IT', 'CA'),
        (1100, '93091 Calle della Te', '10934', 'Venice', 'IT', 'CA'),
        (1200, '2017 Shinjuku-ku', '1689', 'Tokyo', 'Tokyo Prefecture', 'JP'),
        (1300, '9450 Kamiya-cho', '6823', 'Hiroshima', 'Hiroshima', '2P'),
        (1400, '2014 Jabberwocky Rd', '26192', 'Southlake', 'Texas', 'US'),
        (1500, '2011 Interiors Blvd', '99236', 'South San South Brun', 'California', 'US'),
        (1600, '2007 Zagora St', '50090', 'New Jersey', 'New Jersey', 'US'),
        (1700, '2004 Charade Rd', '98199', 'Seattle', 'Washington', 'US'),
        (1800, '147 Spadina Ave', 'MSV 2L7', 'Toronto', 'Ontario', 'CA')
    ]

    cur.executemany("INSERT INTO locations VALUES (?, ?, ?, ?, ?, ?)", locations_data)

    # Commit the transaction
    conn.commit()

    # Query data without JOIN
    cur.execute('''SELECT location_id, street_address, postal_code, city, state_province
                    FROM locations
                    WHERE country_id = 'CA' ''')

    # Fetch results
    without_results = cur.fetchall()

    # Close cursor and connection
    cur.close()
    conn.close()

    return without_results

if __name__ == '__main__':
    app.run(debug=True)
