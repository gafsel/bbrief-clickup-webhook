import datetime as dt
import db.database



def insert(service: str, type: str, content: str, timestamp: dt.datetime, url: str):
    database = db.database.new()

    print(f"Inserting event {content}")

    with database.engine.begin() as conn:
        conn.execute(
            text(
                f"""
                INSERT INTO main.event(id, service, type, content, timestamp, url)
                values(nextval('seq_event'), :service, :type, :content, :timestamp, :url)
                """
            ),
            {
                "service": service, 
                "type": type, 
                "content": content,
                "timestamp": timestamp,
                "url": url,
            }
        )