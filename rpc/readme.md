## RPC

### 简介

RPC（Remote Procedure Call，远程过程调用）是一种计算机通信协议，它允许一个计算机程序调用另一个计算机程序（通常在远程计算机上）的过程，就像调用本地的函数一样。RPC通常用于构建分布式系统，可以让不同的计算机程序在网络上进行通信，从而实现分布式计算、分布式存储、分布式处理等应用场景。

### 优点

可以让不同的计算机程序在网络上进行通信，从而实现分布式计算、分布式存储、分布式处理等应用场景。RPC还可以提高系统的可扩展性和可维护性，使得系统更加灵活和可靠。

### 基本原理

客户端向服务器发送一个请求消息，请求调用服务器上的某个过程（即远程过程）。服务器接收到请求消息后，执行相应的过程，并将执行结果返回给客户端。

RPC的实现通常包括以下几个步骤：

1. 客户端调用本地的代理对象，代理对象将请求消息打包并发送给服务器。
2. 服务器接收到请求消息后，将其解包并执行相应的过程。
3. 服务器将执行结果打包成响应消息，发送给客户端。
4. 客户端接收到响应消息后，将其解包并返回执行结果。

### demo说明

基于rpyc实现
