from DB_connection import *

def retrieve_names():
    names = []
    try:
        with engine.connect() as conn:
        # use engine to execute a SQL query
            results = conn.execute(text("SELECT * FROM places"))
        #iterate through return results from query
            for i in result:
                # adds name of place to the list of names
                names.append(i[1])
    except Exception as e:
        print(f"Error executing command: {e}")
    return names
