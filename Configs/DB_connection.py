from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://neondb_owner:npg_N0eOop5btgCV@ep-damp-sun-a8sfb2go-pooler.eastus2.azure.neon.tech/BA-database?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

if __name__ == "__main__":
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM places"))
            for i in result:
                print(f"The name retrieved is {i[1]}")
    except Exception as e:
        print(f"Connection Failed, More details with the follwing: {e}")
