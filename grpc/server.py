# server.py

import grpc
# 自动生成的消息类型
import server_pb2
# 自动生成的gRPC服务的客户端和服务器类
import server_pb2_grpc
try:
    from concurrent import futures
except ImportError:
    import futures
    
class Server(server_pb2_grpc.ServerServicer):
    # 实现proto中的handle方法
    def handler(self, request, context):
        # 获取request消息中的name字段，并返回reply类型的消息给客户端
        return server_pb2.reply(message=f"Hello, {request.name}!")

if __name__ == "__main__":
    # 获取server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 绑定服务
    server_pb2_grpc.add_ServerServicer_to_server(Server(), server)
    # 绑定地址
    server.add_insecure_port("[::]:50051")
    # 启动
    server.start()
    # 阻塞
    server.wait_for_termination()