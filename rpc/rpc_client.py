# client
import rpyc

if __name__ == "__main__":
    conn = rpyc.connect("localhost", 18861)
    print(conn.root.greet("World"))
    print(conn.root.bye("World"))