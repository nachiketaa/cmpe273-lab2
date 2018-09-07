# -*- coding: utf-8 -*-

from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc

def run():
	with grpc.insecure_channel('localhost:50052') as channel:
		#stub = calculator_pb2_grpc.CalculatorStub(channel)
		#response = stub.AddAB(calculator_pb2.NumberRequest(a=12,b=13))
		#print(response.value)
		print("Sum of a=12 and b =13 is : ", calculator_pb2_grpc.CalculatorStub(channel).AddAB(calculator_pb2.NumberRequest(a=12,b=13)).value)
		#print(stub.MulAB(calculator_pb2.NumberRequest(a=12,b=13)).value)

if __name__ == '__main__':
    run()
