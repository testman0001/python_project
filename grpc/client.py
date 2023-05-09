# client.py

import grpc
import server_pb2
import server_pb2_grpc

if __name__ == "__main__":
    # 建立连接
    channel = grpc.insecure_channel("localhost:50051")
    stub = server_pb2_grpc.ServerStub(channel)
    # 调用grpc服务器的handler方法
    response = stub.handler(server_pb2.request(name="yang"))
    # 打印返回的结果
    print(response.message)